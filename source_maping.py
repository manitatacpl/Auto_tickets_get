SOURCE_MAPPINGS = [
    {"id": 2, "value": "Portal"},
    {"id": 1, "value": "Email"},
    {"id": 3, "value": "Phone"},
    {"id": 9, "value": "Walk-up"},
    {"id": 12, "value": "Workplace"},
    {"id": 14, "value": "Alerts"},
    {"id": 15, "value": "MS Teams"},
    {"id": 1001, "value": "IN APP"},
    {"id": 16, "value": "Freshdesk"},
    {"id": 1002, "value": "Digital Assistant"}
]

def get_source_name_by_id(id):
    for source in SOURCE_MAPPINGS:
        if source["id"] == id:
            return source["value"]
    return "N/A"

def get_source_id_by_name(name):
    for source in SOURCE_MAPPINGS:
        if source["value"].lower() == name.lower():
            return source["id"]
    return None
