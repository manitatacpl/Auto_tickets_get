import requests
import json
import os
import sys
import time   
import dotenv           
import logging
import datetime
import pandas as pd
import concurrent.futures
from group_maping import get_group_name_by_id
from status_mapping import get_status_name_by_id
from source_maping import get_source_name_by_id
from department_mapping import get_department_name_by_id  

dotenv.load_dotenv() 

FRESHSERVICE_DOMAIN = os.getenv("Domain")
FRESHSERVICE_API_KEY = os.getenv("api_key")

url = f"{FRESHSERVICE_DOMAIN}/api/v2/tickets"
TICKET_FORM_FIELDS_URL = f"{FRESHSERVICE_DOMAIN}/api/v2/ticket_form_fields"

def response_code(url):
    response = requests.get(url, auth=(FRESHSERVICE_API_KEY, "X"), headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        print("Response Code: 200 OK")
    else:
        print(f"Response Code: {response.status_code} - {response.reason}")

response_code(url)

def get_tickets():
    response = requests.get(url, auth=(FRESHSERVICE_API_KEY, "X"), headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        tickets = response.json().get('tickets', [])
        return tickets
    else:
        print(f"Failed to fetch tickets: {response.status_code} - {response.reason}")
        return []

def get_six_months_ago_iso():
    six_months_ago = datetime.datetime.now() - datetime.timedelta(days=180)
    return six_months_ago.strftime('%Y-%m-%dT%H:%M:%SZ')

def get_all_tickets_past_6_months():
    tickets = []
    page = 1
    per_page = 100
    six_months_ago = get_six_months_ago_iso()
    while True:
        params = {
            "updated_since": six_months_ago,
            "page": page,
            "per_page": per_page
        }
        response = requests.get(
            url,
            auth=(FRESHSERVICE_API_KEY, "X"),
            headers={"Content-Type": "application/json"},
            params=params
        )
        if response.status_code != 200:
            print(f"Failed to fetch tickets: {response.status_code} - {response.reason}")
            break
        page_tickets = response.json().get('tickets', [])
        if not page_tickets:
            break
        tickets.extend(page_tickets)
        if len(page_tickets) < per_page:
            break
        page += 1
    return tickets

def get_requester_info(requester_id):
    REQUESTER_API_URL = f"{FRESHSERVICE_DOMAIN}/api/v2/requesters"
    url = f"{REQUESTER_API_URL}/{requester_id}"
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, auth=(FRESHSERVICE_API_KEY, "X"), headers=headers, timeout=10)
        if response.status_code == 200:
            requester_data = response.json()
            return requester_data
        else:
            return None
    except Exception:
        return None

def extract_ticket_info(ticket):
    department_id = ticket.get('department_id', None)
    department_name = get_department_name_by_id(department_id) if department_id else "N/A"
    group_id = ticket.get('group_id', None)
    group_name = get_group_name_by_id(group_id) if group_id else "N/A"
    status_id = ticket.get('status', None)
    status_name = get_status_name_by_id(status_id) if status_id else "N/A"
    source_id = ticket.get('source', None)
    source_name = get_source_name_by_id(source_id) if source_id else "N/A"
    requester_id = ticket.get('requester_id', None)
    requester_email = 'N/A'
    requester_location = 'N/A'
    requester_name = 'N/A'
    requester_job_title = 'N/A'
    requester_mobile = 'N/A'
    if requester_id:
        try:
            requester_info = get_requester_info(requester_id)
            if requester_info and 'requester' in requester_info:
                r = requester_info['requester']
                requester_email = r.get('primary_email', 'N/A')
                requester_location = r.get('location_name', r.get('address', 'N/A'))
                requester_name = f"{r.get('first_name', '')} {r.get('last_name', '')}".strip()
                requester_job_title = r.get('job_title', 'N/A')
                requester_mobile = r.get('mobile_phone_number', 'N/A')
        except Exception:
            pass
    return {
        "Department": department_name,
        "Description": ticket.get('description', 'N/A'),
        "Group": group_name,
        "Requester Email": requester_email,
        "Requester Location": requester_location,
        "Source": source_name,
        "Subject": ticket.get('subject', 'N/A')
    }

# Parallelize ticket info extraction
tickets = get_all_tickets_past_6_months()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    ticket_data = list(executor.map(extract_ticket_info, tickets))

# Ensure column order
columns = ["Department", "Description", "Group", "Requester Email", "Requester Location", "Source", "Subject"]
df = pd.DataFrame(ticket_data, columns=columns)
output_file = "ticket_info.xlsx"
df.to_excel(output_file, index=False)
print(f"Saved {len(df)} tickets to {output_file}")