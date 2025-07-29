STATUS_MAPPINGS = [
    {"id": 2, "value": "Open"},
    {"id": 6, "value": "Assigned"},
    {"id": 7, "value": "In Progress"},
    {"id": 8, "value": "Pending with User"},
    {"id": 9, "value": "Awaiting Approval"},
    {"id": 10, "value": "Pending Monitoring/observation Incident"},
    {"id": 11, "value": "Pending with Vendor"},
    {"id": 12, "value": "Change Initiated"},
    {"id": 13, "value": "Cancelled"},
    {"id": 4, "value": "Resolved"},
    {"id": 5, "value": "Closed"},
    {"id": 3, "value": "Pending"}
]

def get_status_name_by_id(id):
    for status in STATUS_MAPPINGS:
        if status["id"] == id:
            return status["value"]
    return "N/A"

def get_status_id_by_name(name):
    for status in STATUS_MAPPINGS:
        if status["value"].lower() == name.lower():
            return status["id"]
    return None
