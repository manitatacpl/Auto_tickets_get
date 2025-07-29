# import requests

# FRESHSERVICE_API_KEY = "EXHRMlmZPfust7PElttj"
# FRESHSERVICE_DOMAIN = "https://060helpdesk.freshservice.com"
# TICKET_FORM_FIELDS_URL = f"{FRESHSERVICE_DOMAIN}/api/v2/ticket_form_fields"
# DEPARTMENT_FIELD_ID = 56000121618

# def get_department_choices(field_id=DEPARTMENT_FIELD_ID):
#     headers = {
#         "Content-Type": "application/json"
#     }
#     response = requests.get(TICKET_FORM_FIELDS_URL, auth=(FRESHSERVICE_API_KEY, "X"), headers=headers, timeout=10)
#     if response.status_code != 200:
#         print(f"Failed to fetch ticket form fields. Status Code: {response.status_code}")
#         print(f"Response: {response.text}")
#         return []
#     data = response.json()
#     for field in data.get("ticket_fields", []):
#         if field.get("id") == field_id and "choices" in field:
#             return field["choices"]
#     return []

# def get_department_value_by_id(choice_id, field_id=DEPARTMENT_FIELD_ID):
#     choices = get_department_choices(field_id)
#     for choice in choices:
#         if choice.get("id") == choice_id:
#             return choice.get("value")
#     return "N/A"

# def get_department_id_by_value(value, field_id=DEPARTMENT_FIELD_ID):
#     choices = get_department_choices(field_id)
#     for choice in choices:
#         if choice.get("value").lower() == value.lower():
#             return choice.get("id")
#     return None

# # Example usage:
# if __name__ == "__main__":
   
#     print("Value for id=56000289107:", get_department_value_by_id(56000289107))

DEPARTMENT_MAPPINGS = [
    {
          "id": 56000289107,
          "value": "3P Mfg Ops"
        },
        {
          "id": 56000289169,
          "value": "8120  Packaging"
        },
        {
          "id": 56000288938,
          "value": "Accounting"
        },
        {
          "id": 56000289254,
          "value": "Accounting (ACC_D_TCVCL)"
        },
        {
          "id": 56000288988,
          "value": "Accounts"
        },
        {
          "id": 56000289405,
          "value": "Accounts & Audit"
        },
        {
          "id": 56000289406,
          "value": "Accounts & Procurement"
        },
        {
          "id": 56000289401,
          "value": "Accounts & TAX"
        },
        {
          "id": 56000288971,
          "value": "Accounts Department"
        },
        {
          "id": 56000289315,
          "value": "Accounts Payable"
        },
        {
          "id": 56000288992,
          "value": "Admin"
        },
        {
          "id": 56000289111,
          "value": "ADMIN & HR"
        },
        {
          "id": 56000288885,
          "value": "Admin & Safety"
        },
        {
          "id": 56000289420,
          "value": "Admin Office Operation Support"
        },
        {
          "id": 56000289156,
          "value": "Admin&Safety"
        },
        {
          "id": 56000288911,
          "value": "Administration"
        },
        {
          "id": 56000289249,
          "value": "Administration (Admin_D_TCL)"
        },
        {
          "id": 56000288883,
          "value": "Alternate Channels"
        },
        {
          "id": 56000289084,
          "value": "Alternate Channels (Alternate_Channels)"
        },
        {
          "id": 56000288986,
          "value": "Analytical"
        },
        {
          "id": 56000289241,
          "value": "Analytical (Analytical)"
        },
        {
          "id": 56000289000,
          "value": "Anamallaisgroup Factories"
        },
        {
          "id": 56000289438,
          "value": "Associate - Health & Safety"
        },
        {
          "id": 56000288963,
          "value": "Balmany Estate"
        },
        {
          "id": 56000289102,
          "value": "Blending unit"
        },
        {
          "id": 56000289279,
          "value": "Brand & E-Commerce"
        },
        {
          "id": 56000289104,
          "value": "Branded Business Operations"
        },
        {
          "id": 56000289278,
          "value": "Business Development"
        },
        {
          "id": 56000289280,
          "value": "Business Development, Brand & E-Commerce"
        },
        {
          "id": 56000288902,
          "value": "Business Excellence"
        },
        {
          "id": 56000289263,
          "value": "Business Excellence (BE_D_TCL)"
        },
        {
          "id": 56000288878,
          "value": "Business Finance"
        },
        {
          "id": 56000289168,
          "value": "Business Finance (Business_Finance)"
        },
        {
          "id": 56000288919,
          "value": "Business Head"
        },
        {
          "id": 56000288891,
          "value": "Business HR"
        },
        {
          "id": 56000288915,
          "value": "Business HR (Business_HR)"
        },
        {
          "id": 56000289340,
          "value": "Business Integration and Transfer"
        },
        {
          "id": 56000289347,
          "value": "Business_Finance"
        },
        {
          "id": 56000289100,
          "value": "Business_Integration_and_Transf"
        },
        {
          "id": 56000289163,
          "value": "BusinessFinance"
        },
        {
          "id": 56000289172,
          "value": "BusinessHR"
        },
        {
          "id": 56000289271,
          "value": "BusinessServices"
        },
        {
          "id": 56000289151,
          "value": "Call Center MIS"
        },
        {
          "id": 56000289048,
          "value": "Cannoncadoo Estate"
        },
        {
          "id": 56000289421,
          "value": "CEO"
        },
        {
          "id": 56000289160,
          "value": "CFA"
        },
        {
          "id": 56000289331,
          "value": "Channel Development"
        },
        {
          "id": 56000288935,
          "value": "Cluster Operations"
        },
        {
          "id": 56000289234,
          "value": "Cluster Operations (CLO_D_TCL)"
        },
        {
          "id": 56000288918,
          "value": "Coffee Buying & Blending"
        },
        {
          "id": 56000289044,
          "value": "Coffee Section"
        },
        {
          "id": 56000289077,
          "value": "Commercial"
        },
        {
          "id": 56000289285,
          "value": "Commercial - Branded Finance"
        },
        {
          "id": 56000288905,
          "value": "Commercial / Branded Finance"
        },
        {
          "id": 56000288961,
          "value": "Commercial & Logistics"
        },
        {
          "id": 56000289250,
          "value": "Commercial & Logistics (Comm_D_TCL)"
        },
        {
          "id": 56000288975,
          "value": "Commercial Finance"
        },
        {
          "id": 56000288896,
          "value": "Commodity Sourcing & Management Organization"
        },
        {
          "id": 56000289343,
          "value": "Commodity_Sourcing_&_Mgmt_Org"
        },
        {
          "id": 56000289152,
          "value": "CommoditySourcing&ManagementOrganization"
        },
        {
          "id": 56000288996,
          "value": "Company Secretarial"
        },
        {
          "id": 56000289256,
          "value": "Company Secretarial (Company_Secretarial)"
        },
        {
          "id": 56000289181,
          "value": "Company Secretarial & Legal"
        },
        {
          "id": 56000289070,
          "value": "Conference Room"
        },
        {
          "id": 56000289081,
          "value": "Consumer Insights"
        },
        {
          "id": 56000289245,
          "value": "Consumer Insights (Consumer_Insights)"
        },
        {
          "id": 56000288888,
          "value": "Consumer Planning & Insights"
        },
        {
          "id": 56000289220,
          "value": "Consumer Planning & Insights (Consumer_Planning_&_Insights)"
        },
        {
          "id": 56000289130,
          "value": "Contract"
        },
        {
          "id": 56000289075,
          "value": "Coovercolly Estate"
        },
        {
          "id": 56000288932,
          "value": "Corporate - MD's office"
        },
        {
          "id": 56000289061,
          "value": "Corporate Communications"
        },
        {
          "id": 56000289145,
          "value": "Corporate Communications (HBCC_D_TCL)"
        },
        {
          "id": 56000288968,
          "value": "Corporate Finance"
        },
        {
          "id": 56000288943,
          "value": "Corporate HR"
        },
        {
          "id": 56000289095,
          "value": "Corporate HR (Corporate_HR)"
        },
        {
          "id": 56000288989,
          "value": "Corporate Social Responsibility"
        },
        {
          "id": 56000289243,
          "value": "Corporate Social Responsibility (CSR_D_TCL)"
        },
        {
          "id": 56000289179,
          "value": "CorporateHR"
        },
        {
          "id": 56000289038,
          "value": "Cottabetta Estate"
        },
        {
          "id": 56000289078,
          "value": "CPB"
        },
        {
          "id": 56000289079,
          "value": "CPB - COMMERCIAL"
        },
        {
          "id": 56000289393,
          "value": "CSMO"
        },
        {
          "id": 56000288931,
          "value": "Curing"
        },
        {
          "id": 56000289231,
          "value": "Curing (Curi_D_TCL)"
        },
        {
          "id": 56000288925,
          "value": "Customer Care"
        },
        {
          "id": 56000289422,
          "value": "Customer Fulfilment"
        },
        {
          "id": 56000289204,
          "value": "Customer Operations"
        },
        {
          "id": 56000289356,
          "value": "Customer Relationship Management"
        },
        {
          "id": 56000288865,
          "value": "Customer Support"
        },
        {
          "id": 56000289342,
          "value": "D2C"
        },
        {
          "id": 56000289306,
          "value": "DELETE"
        },
        {
          "id": 56000288863,
          "value": "Development"
        },
        {
          "id": 56000289335,
          "value": "Digita"
        },
        {
          "id": 56000288872,
          "value": "Digital"
        },
        {
          "id": 56000289547,
          "value": "Digital - Analytics"
        },
        {
          "id": 56000289476,
          "value": "Digital - Data & Analytics"
        },
        {
          "id": 56000289462,
          "value": "Digital - Delivery"
        },
        {
          "id": 56000289465,
          "value": "Digital - Transformation"
        },
        {
          "id": 56000288874,
          "value": "Digital (Digital)"
        },
        {
          "id": 56000289397,
          "value": "Digital Application"
        },
        {
          "id": 56000289396,
          "value": "Digital Infrastructure"
        },
        {
          "id": 56000289276,
          "value": "Digital Marketing"
        },
        {
          "id": 56000289132,
          "value": "Digital Marketing, Foods"
        },
        {
          "id": 56000289435,
          "value": "Digital SAP STS SUPPORT"
        },
        {
          "id": 56000289433,
          "value": "Digital SAP SUPPORT"
        },
        {
          "id": 56000289432,
          "value": "Digital SAP SUPPORT?"
        },
        {
          "id": 56000289426,
          "value": "Digital SAP SUPPORT�"
        },
        {
          "id": 56000289362,
          "value": "Digital- cyber security"
        },
        {
          "id": 56000289357,
          "value": "Digital-EUC"
        },
        {
          "id": 56000289339,
          "value": "Digital-TCS"
        },
        {
          "id": 56000289323,
          "value": "Digital, Analytics, Digital"
        },
        {
          "id": 56000289369,
          "value": "Digital, Nourishco & Tata Coffee"
        },
        {
          "id": 56000289274,
          "value": "Disha  Tailoring unit"
        },
        {
          "id": 56000289424,
          "value": "Dispatch"
        },
        {
          "id": 56000289425,
          "value": "Dispatch & Billing"
        },
        {
          "id": 56000289032,
          "value": "Diversification"
        },
        {
          "id": 56000289445,
          "value": "Diversification - Cafe Outlet"
        },
        {
          "id": 56000288964,
          "value": "Diversification - Pepper & Bought Coffee"
        },
        {
          "id": 56000289242,
          "value": "Diversification - Pepper & Bought Coffee (DPBC_D_TCL)"
        },
        {
          "id": 56000289208,
          "value": "Diversification (DIVERS_D_TCL)"
        },
        {
          "id": 56000294585,
          "value": "DT Leads"
        },
        {
          "id": 56000289383,
          "value": "E-Commerce"
        },
        {
          "id": 56000289063,
          "value": "East Zone Sales"
        },
        {
          "id": 56000289410,
          "value": "EBO"
        },
        {
          "id": 56000289316,
          "value": "Ecommerce"
        },
        {
          "id": 56000289320,
          "value": "EHS Technical lead"
        },
        {
          "id": 56000289136,
          "value": "Eight O'Clock Coffee Company (EOCC)"
        },
        {
          "id": 56000289292,
          "value": "Empirical"
        },
        {
          "id": 56000289394,
          "value": "Employee Onboarding Team"
        },
        {
          "id": 56000288966,
          "value": "Engineering"
        },
        {
          "id": 56000289434,
          "value": "Engineering & Projects"
        },
        {
          "id": 56000289268,
          "value": "Engineering & Safety"
        },
        {
          "id": 56000288922,
          "value": "Engineering & Special Projects"
        },
        {
          "id": 56000289230,
          "value": "Engineering & Special Projects (Engi_D_TCL)"
        },
        {
          "id": 56000289305,
          "value": "Engineering Department"
        },
        {
          "id": 56000289293,
          "value": "Engineering Projects"
        },
        {
          "id": 56000289043,
          "value": "Engineering Pulp"
        },
        {
          "id": 56000289301,
          "value": "Enginnering Department"
        },
        {
          "id": 56000289269,
          "value": "EO"
        },
        {
          "id": 56000289082,
          "value": "EO Support"
        },
        {
          "id": 56000288952,
          "value": "ESD"
        },
        {
          "id": 56000289304,
          "value": "ESD Department"
        },
        {
          "id": 56000288995,
          "value": "Establishment"
        },
        {
          "id": 56000289042,
          "value": "Estate Common ID"
        },
        {
          "id": 56000289014,
          "value": "Estate Factory"
        },
        {
          "id": 56000289015,
          "value": "Estate Office"
        },
        {
          "id": 56000288926,
          "value": "Estate Operations"
        },
        {
          "id": 56000289155,
          "value": "Estate Operations (ESTO_DTCL)"
        },
        {
          "id": 56000288947,
          "value": "Estate Supplies Division"
        },
        {
          "id": 56000289246,
          "value": "Estate Supplies Division (ESD_D_TCL)"
        },
        {
          "id": 56000289282,
          "value": "EstateOperations"
        },
        {
          "id": 56000289359,
          "value": "EUC"
        },
        {
          "id": 56000289423,
          "value": "Exclusive Brand Outlets"
        },
        {
          "id": 56000289554,
          "value": "Executive - HR"
        },
        {
          "id": 56000288892,
          "value": "Executive Committee"
        },
        {
          "id": 56000289187,
          "value": "Executive Committee (Executive_Committee)"
        },
        {
          "id": 56000289060,
          "value": "Executive Committee Support"
        },
        {
          "id": 56000289266,
          "value": "Executive Committee Support (Executive_Committee_Support)"
        },
        {
          "id": 56000288949,
          "value": "Executive Department"
        },
        {
          "id": 56000289360,
          "value": "Executive Director"
        },
        {
          "id": 56000289361,
          "value": "Executive Director & Chief Operating Officer"
        },
        {
          "id": 56000289381,
          "value": "Export"
        },
        {
          "id": 56000288904,
          "value": "Facilities"
        },
        {
          "id": 56000289429,
          "value": "Field Sales"
        },
        {
          "id": 56000288866,
          "value": "Finance"
        },
        {
          "id": 56000289066,
          "value": "Finance -  Accounts & MIS"
        },
        {
          "id": 56000289236,
          "value": "Finance -  Accounts & MIS (FIN&MIS_D_TCL)"
        },
        {
          "id": 56000288889,
          "value": "Finance -  Accounts & Taxation"
        },
        {
          "id": 56000288942,
          "value": "Finance -  Accounts & Taxation (Fina_D_TCL)"
        },
        {
          "id": 56000289338,
          "value": "Finance - Accounts & MIS"
        },
        {
          "id": 56000289550,
          "value": "Finance - Accounts & Taxation"
        },
        {
          "id": 56000289444,
          "value": "Finance - Ama Trails"
        },
        {
          "id": 56000289052,
          "value": "Finance - Branded Business Operations"
        },
        {
          "id": 56000288974,
          "value": "Finance - Instant Coffee"
        },
        {
          "id": 56000289219,
          "value": "Finance - Instant Coffee (FIC_D_TCL)"
        },
        {
          "id": 56000288983,
          "value": "Finance - Internal Audit"
        },
        {
          "id": 56000289232,
          "value": "Finance - Internal Audit (FINI_D_TCL)"
        },
        {
          "id": 56000288875,
          "value": "Finance - Plantations"
        },
        {
          "id": 56000289185,
          "value": "Finance - Plantations (FINP_D_TCL)"
        },
        {
          "id": 56000288903,
          "value": "Finance - Risk & Hedging"
        },
        {
          "id": 56000289247,
          "value": "Finance - Risk & Hedging (FRH_D_TCL)"
        },
        {
          "id": 56000288924,
          "value": "Finance - Taxation"
        },
        {
          "id": 56000289255,
          "value": "Finance - Taxation (FINNTX_D_TCL)"
        },
        {
          "id": 56000289191,
          "value": "Finance (FIN_D_TCVCL)"
        },
        {
          "id": 56000289069,
          "value": "Finance (SA OTC)"
        },
        {
          "id": 56000289159,
          "value": "Finance & Accounts"
        },
        {
          "id": 56000289184,
          "value": "Finance & Accounts (Fina_D_TCL)"
        },
        {
          "id": 56000289090,
          "value": "Finance & Legal"
        },
        {
          "id": 56000289399,
          "value": "Finance & Procurement"
        },
        {
          "id": 56000289460,
          "value": "Finance & Supply Chain Management - Finance"
        },
        {
          "id": 56000289374,
          "value": "Finance and Accounts"
        },
        {
          "id": 56000289110,
          "value": "Finance PR/PO"
        },
        {
          "id": 56000289197,
          "value": "Finance Support"
        },
        {
          "id": 56000289552,
          "value": "Finance Taxation"
        },
        {
          "id": 56000289162,
          "value": "Finance-Accounts&MIS"
        },
        {
          "id": 56000289157,
          "value": "Finance-Plantations"
        },
        {
          "id": 56000289419,
          "value": "Finance, Legal"
        },
        {
          "id": 56000289413,
          "value": "Finance, Legal & IT"
        },
        {
          "id": 56000289127,
          "value": "Finance&Legal"
        },
        {
          "id": 56000288957,
          "value": "Financial Planning & Analysis"
        },
        {
          "id": 56000289251,
          "value": "Financial Planning & Analysis (Financial_Planning_&_Analysis)"
        },
        {
          "id": 56000289354,
          "value": "Financial_Planning_&_Analysis"
        },
        {
          "id": 56000289391,
          "value": "Food Safety & Quality"
        },
        {
          "id": 56000289375,
          "value": "Food Safety and Quality"
        },
        {
          "id": 56000289390,
          "value": "Food Services"
        },
        {
          "id": 56000289277,
          "value": "Foods"
        },
        {
          "id": 56000289020,
          "value": "Forest Resource Management ANAM"
        },
        {
          "id": 56000289036,
          "value": "Forest Resource Management Hassan"
        },
        {
          "id": 56000288939,
          "value": "Forest Resources Management"
        },
        {
          "id": 56000288934,
          "value": "Forest Resources Management (Forest_Res_Dept)"
        },
        {
          "id": 56000289358,
          "value": "FS - CMDB"
        },
        {
          "id": 56000289365,
          "value": "FS-CMDB-BRANDSITES"
        },
        {
          "id": 56000289363,
          "value": "FS-CMDB-Datalake"
        },
        {
          "id": 56000289364,
          "value": "FS-CMDB-SAP"
        },
        {
          "id": 56000289367,
          "value": "FS-CMDB-SuccessFactors"
        },
        {
          "id": 56000289299,
          "value": "GB Commercial Finance"
        },
        {
          "id": 56000289298,
          "value": "GB Strategy and Planning"
        },
        {
          "id": 56000288913,
          "value": "General Hospital"
        },
        {
          "id": 56000289093,
          "value": "General Management"
        },
        {
          "id": 56000289549,
          "value": "General Management - Safety, Health and Environment"
        },
        {
          "id": 56000288948,
          "value": "General Management (GM_D_TCVCL)"
        },
        {
          "id": 56000288881,
          "value": "General Trade"
        },
        {
          "id": 56000288907,
          "value": "General Trade (General_Trade)"
        },
        {
          "id": 56000289346,
          "value": "General_Trade"
        },
        {
          "id": 56000289318,
          "value": "GeneralTrade"
        },
        {
          "id": 56000289138,
          "value": "Global Finance"
        },
        {
          "id": 56000289314,
          "value": "Global Human Resources"
        },
        {
          "id": 56000289004,
          "value": "Global Research & Development"
        },
        {
          "id": 56000289071,
          "value": "Goorghully Estate"
        },
        {
          "id": 56000288909,
          "value": "Green Beans Procurement"
        },
        {
          "id": 56000289257,
          "value": "Green Beans Procurement (Gree_D_TCL)"
        },
        {
          "id": 56000288929,
          "value": "Green Beans Sales"
        },
        {
          "id": 56000289258,
          "value": "Green Beans Sales (GBS_D_TCL)"
        },
        {
          "id": 56000289325,
          "value": "Green Coffee"
        },
        {
          "id": 56000288900,
          "value": "Greenford (Facility)"
        },
        {
          "id": 56000288871,
          "value": "Group Finance"
        },
        {
          "id": 56000288873,
          "value": "Group Finance (Group_Finance)"
        },
        {
          "id": 56000289349,
          "value": "Group_Finance"
        },
        {
          "id": 56000289118,
          "value": "GroupFinance"
        },
        {
          "id": 56000289051,
          "value": "Gubgull Estate"
        },
        {
          "id": 56000288991,
          "value": "High Range Hospital"
        },
        {
          "id": 56000289183,
          "value": "High Range Hospital (High_Range_Hospital)"
        },
        {
          "id": 56000288937,
          "value": "High Range school"
        },
        {
          "id": 56000289229,
          "value": "High Range School (High_Range_School)"
        },
        {
          "id": 56000289294,
          "value": "High Range Strawberry Preserve unit"
        },
        {
          "id": 56000289344,
          "value": "High_Range_Hospital"
        },
        {
          "id": 56000289175,
          "value": "HighRangeHospital"
        },
        {
          "id": 56000289324,
          "value": "HighRangeSchool"
        },
        {
          "id": 56000288867,
          "value": "HR"
        },
        {
          "id": 56000289133,
          "value": "HR & Admin"
        },
        {
          "id": 56000289411,
          "value": "HR, Training & Admin"
        },
        {
          "id": 56000288930,
          "value": "Human Resource"
        },
        {
          "id": 56000289205,
          "value": "Human Resource (HR_D_TCL)"
        },
        {
          "id": 56000289385,
          "value": "Human Resource & administration"
        },
        {
          "id": 56000289105,
          "value": "Human Resources"
        },
        {
          "id": 56000289222,
          "value": "Human Resources (HR_D_TCVCL)"
        },
        {
          "id": 56000289380,
          "value": "Human Resources & Administration"
        },
        {
          "id": 56000289373,
          "value": "Human Resources and Administration"
        },
        {
          "id": 56000289311,
          "value": "HUMAN RESOURCES DEPT"
        },
        {
          "id": 56000289150,
          "value": "HumanResources"
        },
        {
          "id": 56000288940,
          "value": "ICD - Commercial"
        },
        {
          "id": 56000288910,
          "value": "ICD - Purchase Department"
        },
        {
          "id": 56000289289,
          "value": "ICD - Vending Business"
        },
        {
          "id": 56000289286,
          "value": "ICD, Corporate - ICD"
        },
        {
          "id": 56000289176,
          "value": "India Sales"
        },
        {
          "id": 56000289463,
          "value": "India Sales - Alternate Channels"
        },
        {
          "id": 56000289453,
          "value": "India Sales - General Trade"
        },
        {
          "id": 56000289458,
          "value": "India Sales - Sales Enabling Organization"
        },
        {
          "id": 56000288914,
          "value": "Industrial Relations"
        },
        {
          "id": 56000289221,
          "value": "Industrial Relations (IR_D_TCL)"
        },
        {
          "id": 56000289137,
          "value": "IndustrialRelations"
        },
        {
          "id": 56000289450,
          "value": "INFINITI"
        },
        {
          "id": 56000289259,
          "value": "Information Technology"
        },
        {
          "id": 56000288977,
          "value": "Information Technology (IT_D_TCL)"
        },
        {
          "id": 56000289372,
          "value": "Information Technology and Systems"
        },
        {
          "id": 56000288970,
          "value": "Instant Coffee & Curing Operations"
        },
        {
          "id": 56000289264,
          "value": "Instant Coffee & Curing Operations (ICCO_D_TCL)"
        },
        {
          "id": 56000289018,
          "value": "Instant Coffee Division Operations"
        },
        {
          "id": 56000288967,
          "value": "Instant Coffee Division Operations (ICD _D_TCL)"
        },
        {
          "id": 56000289003,
          "value": "Instant Coffee Sales"
        },
        {
          "id": 56000289238,
          "value": "Instant Coffee Sales (ICD_D_TCL)"
        },
        {
          "id": 56000289428,
          "value": "Institutional Sales"
        },
        {
          "id": 56000289165,
          "value": "Integrated Finance"
        },
        {
          "id": 56000289470,
          "value": "Integrated Finance - Business Finance"
        },
        {
          "id": 56000289520,
          "value": "Integrated Finance - Company Secretarial"
        },
        {
          "id": 56000289548,
          "value": "Integrated Finance - Finance Trainee"
        },
        {
          "id": 56000289466,
          "value": "Integrated Finance - Group Finance"
        },
        {
          "id": 56000289478,
          "value": "Integrated Finance - Internal Audit"
        },
        {
          "id": 56000289500,
          "value": "Integrated Finance - Investor Relations & Communication"
        },
        {
          "id": 56000289471,
          "value": "Integrated Finance - Legal"
        },
        {
          "id": 56000289494,
          "value": "Integrated Finance - Strategy and M&A"
        },
        {
          "id": 56000289173,
          "value": "Integrated HR"
        },
        {
          "id": 56000289167,
          "value": "Integrated Human Resources"
        },
        {
          "id": 56000289510,
          "value": "Integrated Human Resources - Admin & Safety"
        },
        {
          "id": 56000289472,
          "value": "Integrated Human Resources - Business HR"
        },
        {
          "id": 56000289455,
          "value": "Integrated Human Resources - Corporate HR"
        },
        {
          "id": 56000289518,
          "value": "Integrated Human Resources - Sustainability"
        },
        {
          "id": 56000289486,
          "value": "Integrated Operations - BIT"
        },
        {
          "id": 56000289469,
          "value": "Integrated Operations - CSMO"
        },
        {
          "id": 56000289544,
          "value": "Integrated Operations - Export"
        },
        {
          "id": 56000289452,
          "value": "Integrated Operations - PSO"
        },
        {
          "id": 56000289464,
          "value": "Integrated Operations - QARA"
        },
        {
          "id": 56000289503,
          "value": "Integrated Operations - Solubles Business"
        },
        {
          "id": 56000289527,
          "value": "Integrated Operations - Tea Extraction"
        },
        {
          "id": 56000289049,
          "value": "Integrated Operations & Business Transformation"
        },
        {
          "id": 56000289553,
          "value": "Integrated Operations and Business transformation"
        },
        {
          "id": 56000289341,
          "value": "Integration and Transformation Management"
        },
        {
          "id": 56000288906,
          "value": "Internal Audit"
        },
        {
          "id": 56000289174,
          "value": "Internal Audit (Internal_Audit)"
        },
        {
          "id": 56000289322,
          "value": "InternalAudit"
        },
        {
          "id": 56000289196,
          "value": "International Business"
        },
        {
          "id": 56000289524,
          "value": "International Business - Admin & Safety"
        },
        {
          "id": 56000289490,
          "value": "International Business - Business Finance"
        },
        {
          "id": 56000289505,
          "value": "International Business - Business Head"
        },
        {
          "id": 56000289521,
          "value": "International Business - Company Secretarial"
        },
        {
          "id": 56000289497,
          "value": "International Business - E-Commerce"
        },
        {
          "id": 56000289545,
          "value": "International Business - Ethnic Sales"
        },
        {
          "id": 56000289543,
          "value": "International Business - Export"
        },
        {
          "id": 56000289498,
          "value": "International Business - Marketing"
        },
        {
          "id": 56000289502,
          "value": "International Business - Middle East"
        },
        {
          "id": 56000289480,
          "value": "International Business - PSO"
        },
        {
          "id": 56000289534,
          "value": "International Business - QARA"
        },
        {
          "id": 56000289454,
          "value": "International Business - Sales"
        },
        {
          "id": 56000289530,
          "value": "International Business - Sustainability & Communication"
        },
        {
          "id": 56000289506,
          "value": "International Business - Tea Buying & Blending"
        },
        {
          "id": 56000289528,
          "value": "International Business - Transfomation"
        },
        {
          "id": 56000289404,
          "value": "Inventory & Store"
        },
        {
          "id": 56000289010,
          "value": "Inventory Dept"
        },
        {
          "id": 56000289094,
          "value": "Investor Relations & Communication"
        },
        {
          "id": 56000289223,
          "value": "Investor Relations & Communication (Investor_Relations_&_Comm)"
        },
        {
          "id": 56000289350,
          "value": "Investor_Relations_&_Comm"
        },
        {
          "id": 56000289188,
          "value": "InvestorRelations&Communication"
        },
        {
          "id": 56000289073,
          "value": "IR - Pollibetta"
        },
        {
          "id": 56000288869,
          "value": "IT"
        },
        {
          "id": 56000288972,
          "value": "ITO"
        },
        {
          "id": 56000289085,
          "value": "ITO Munnar"
        },
        {
          "id": 56000288921,
          "value": "Jamoor estate"
        },
        {
          "id": 56000289307,
          "value": "Jumboor Estate"
        },
        {
          "id": 56000289328,
          "value": "Junior Assistant"
        },
        {
          "id": 56000288956,
          "value": "JV - Bangladesh"
        },
        {
          "id": 56000289239,
          "value": "JV - Bangladesh (JV_Bangladesh)"
        },
        {
          "id": 56000289006,
          "value": "JV - Teapigs"
        },
        {
          "id": 56000289442,
          "value": "JV Teapigs"
        },
        {
          "id": 56000289353,
          "value": "JV_Teapigs"
        },
        {
          "id": 56000289040,
          "value": "Kushalnagar Works"
        },
        {
          "id": 56000288898,
          "value": "Legal"
        },
        {
          "id": 56000289214,
          "value": "Legal (Legal)"
        },
        {
          "id": 56000289288,
          "value": "Legal & Secretarial Affairs"
        },
        {
          "id": 56000289371,
          "value": "Legal and Secreterial"
        },
        {
          "id": 56000288899,
          "value": "Logistics"
        },
        {
          "id": 56000289308,
          "value": "Logistics - Planning"
        },
        {
          "id": 56000289215,
          "value": "Logistics (LOG_D_TCVCL)"
        },
        {
          "id": 56000288982,
          "value": "Logistics (North)"
        },
        {
          "id": 56000289166,
          "value": "Logistics, warehousing & CFA"
        },
        {
          "id": 56000289005,
          "value": "Logsitics"
        },
        {
          "id": 56000289029,
          "value": "Maintenance"
        },
        {
          "id": 56000289047,
          "value": "Maintenance (Main_D_TCL)"
        },
        {
          "id": 56000289154,
          "value": "Maintenance (MAIN_D_TCVCL)"
        },
        {
          "id": 56000289400,
          "value": "Maintenece"
        },
        {
          "id": 56000289140,
          "value": "Management Trainee"
        },
        {
          "id": 56000289224,
          "value": "Management Trainee (Management_Trainee)"
        },
        {
          "id": 56000289050,
          "value": "Manufacturing"
        },
        {
          "id": 56000288879,
          "value": "Marketing"
        },
        {
          "id": 56000288993,
          "value": "Marketing - Kochi"
        },
        {
          "id": 56000289207,
          "value": "Marketing (Marketing)"
        },
        {
          "id": 56000289416,
          "value": "Marketing & CRM"
        },
        {
          "id": 56000289317,
          "value": "Marketing & NPD"
        },
        {
          "id": 56000289388,
          "value": "Marketing C02416"
        },
        {
          "id": 56000289067,
          "value": "Marketing Innovation"
        },
        {
          "id": 56000289213,
          "value": "Marketing Innovation (Marketing_Innovation)"
        },
        {
          "id": 56000289351,
          "value": "Marketing_Innovation"
        },
        {
          "id": 56000289144,
          "value": "MarketingInnovation"
        },
        {
          "id": 56000289022,
          "value": "Materials"
        },
        {
          "id": 56000289024,
          "value": "Materials HO"
        },
        {
          "id": 56000289028,
          "value": "Matron"
        },
        {
          "id": 56000289449,
          "value": "Mavic"
        },
        {
          "id": 56000289418,
          "value": "MD Office"
        },
        {
          "id": 56000289072,
          "value": "Media Planning & Buying"
        },
        {
          "id": 56000289076,
          "value": "Media Planning & Buying (Media_Planning_&_Buying)"
        },
        {
          "id": 56000289059,
          "value": "Medical"
        },
        {
          "id": 56000289012,
          "value": "Medical (Medi_D_TCL)"
        },
        {
          "id": 56000289281,
          "value": "Meetin Room ID"
        },
        {
          "id": 56000289296,
          "value": "Meeting Room"
        },
        {
          "id": 56000289287,
          "value": "Meeting Room ID"
        },
        {
          "id": 56000288997,
          "value": "Merthikhan estate"
        },
        {
          "id": 56000288955,
          "value": "Middle East"
        },
        {
          "id": 56000289387,
          "value": "Moderen Trade"
        },
        {
          "id": 56000289376,
          "value": "Modern Trade"
        },
        {
          "id": 56000289262,
          "value": "Monsooning Operations"
        },
        {
          "id": 56000289135,
          "value": "Monsooning Operations (Mons_D_TCL)"
        },
        {
          "id": 56000289386,
          "value": "New Product Development"
        },
        {
          "id": 56000288998,
          "value": "Non-branded Operations"
        },
        {
          "id": 56000289443,
          "value": "Nourishco & Tata Coffee"
        },
        {
          "id": 56000289194,
          "value": "NourishCo Business"
        },
        {
          "id": 56000289170,
          "value": "NPD"
        },
        {
          "id": 56000289227,
          "value": "NPD (NPD_D_TCL)"
        },
        {
          "id": 56000289026,
          "value": "Nullore Estate"
        },
        {
          "id": 56000288887,
          "value": "OCS"
        },
        {
          "id": 56000289378,
          "value": "off roll employee(Finance)"
        },
        {
          "id": 56000289377,
          "value": "off roll employee(Finance) -C02723"
        },
        {
          "id": 56000289113,
          "value": "Office"
        },
        {
          "id": 56000289116,
          "value": "Office/Accounts"
        },
        {
          "id": 56000289055,
          "value": "OOH Marketing"
        },
        {
          "id": 56000289153,
          "value": "Opeations Support"
        },
        {
          "id": 56000289384,
          "value": "Operation & Supply Chain Management"
        },
        {
          "id": 56000289139,
          "value": "Operation Support"
        },
        {
          "id": 56000288978,
          "value": "Operational Support"
        },
        {
          "id": 56000288868,
          "value": "Operations"
        },
        {
          "id": 56000289389,
          "value": "Operations -"
        },
        {
          "id": 56000289512,
          "value": "Operations - Production"
        },
        {
          "id": 56000289539,
          "value": "Operations - Warehouse"
        },
        {
          "id": 56000288920,
          "value": "Operations (OPR_D_TCL)"
        },
        {
          "id": 56000289392,
          "value": "Operations and SCM"
        },
        {
          "id": 56000289379,
          "value": "Operations and Supply Chain Management"
        },
        {
          "id": 56000289407,
          "value": "Operations and supply chain managment"
        },
        {
          "id": 56000288901,
          "value": "Operations Support"
        },
        {
          "id": 56000289395,
          "value": "Operations/Manufacturing"
        },
        {
          "id": 56000289436,
          "value": "Organic India"
        },
        {
          "id": 56000289114,
          "value": "Packaged Beverages"
        },
        {
          "id": 56000289507,
          "value": "Packaged Beverages - Consumer Planning & Insights"
        },
        {
          "id": 56000289523,
          "value": "Packaged Beverages - JV - Bangladesh"
        },
        {
          "id": 56000289475,
          "value": "Packaged Beverages - Marketing"
        },
        {
          "id": 56000289504,
          "value": "Packaged Beverages - Marketing Innovation"
        },
        {
          "id": 56000289529,
          "value": "Packaged Beverages - Media Planning & Buying"
        },
        {
          "id": 56000289147,
          "value": "Packaged Foods"
        },
        {
          "id": 56000289513,
          "value": "Packaged Foods - Consumer Insights"
        },
        {
          "id": 56000289468,
          "value": "Packaged Foods - Marketing"
        },
        {
          "id": 56000289481,
          "value": "Packaged Foods - Marketing Innovation"
        },
        {
          "id": 56000289122,
          "value": "Packaging"
        },
        {
          "id": 56000289178,
          "value": "Packaging (Pack_D_TCL)"
        },
        {
          "id": 56000289099,
          "value": "Packaging Development"
        },
        {
          "id": 56000289011,
          "value": "Packaging Development (Packaging_Development)"
        },
        {
          "id": 56000289112,
          "value": "Packaging Store"
        },
        {
          "id": 56000289182,
          "value": "PackagingDevelopment"
        },
        {
          "id": 56000289330,
          "value": "Pakaged foods"
        },
        {
          "id": 56000289002,
          "value": "Payroll & Taxation"
        },
        {
          "id": 56000289141,
          "value": "Pepper Production (PeppProd_D_TCL)"
        },
        {
          "id": 56000289046,
          "value": "Pepper Sale"
        },
        {
          "id": 56000289218,
          "value": "Pepper Sale (PeppSale_D_TCL)"
        },
        {
          "id": 56000289056,
          "value": "PF Department"
        },
        {
          "id": 56000289295,
          "value": "PICQ"
        },
        {
          "id": 56000289106,
          "value": "Pivot"
        },
        {
          "id": 56000289439,
          "value": "PKM & Store"
        },
        {
          "id": 56000289417,
          "value": "Planning & People"
        },
        {
          "id": 56000289551,
          "value": "Plant Operations"
        },
        {
          "id": 56000288990,
          "value": "Plantation - Pollibetta"
        },
        {
          "id": 56000288917,
          "value": "Plantation Trails"
        },
        {
          "id": 56000288927,
          "value": "Plantation Trails (PlanTrails_D_TCL)"
        },
        {
          "id": 56000289526,
          "value": "Plantation-Estates - Cluster Operations"
        },
        {
          "id": 56000289482,
          "value": "Plantation-Estates - Operations"
        },
        {
          "id": 56000289461,
          "value": "Plantation-Estates - Plantations"
        },
        {
          "id": 56000289546,
          "value": "Plantation-Estates - Tea Factory Operations"
        },
        {
          "id": 56000289535,
          "value": "Plantation-Estates - Tea Operations"
        },
        {
          "id": 56000288951,
          "value": "Plantations"
        },
        {
          "id": 56000289201,
          "value": "Plantations - Estates - Plantations"
        },
        {
          "id": 56000289533,
          "value": "Plantations - KNW - Curing"
        },
        {
          "id": 56000289536,
          "value": "Plantations - KNW - Operations"
        },
        {
          "id": 56000289499,
          "value": "Plantations - KNW - Quality Control"
        },
        {
          "id": 56000288923,
          "value": "Plantations - Operations"
        },
        {
          "id": 56000289253,
          "value": "Plantations - Operations (PLO_D_TCL)"
        },
        {
          "id": 56000289492,
          "value": "Plantations - Support Diversification - Cafe Outlet"
        },
        {
          "id": 56000289522,
          "value": "Plantations - Support Diversification & Bought Coffee"
        },
        {
          "id": 56000289515,
          "value": "Plantations - Support Diversification R&D and Bought Coffee"
        },
        {
          "id": 56000289532,
          "value": "Plantations - Support Engineering & Special Projects"
        },
        {
          "id": 56000289538,
          "value": "Plantations - Support Engineering Special Projects Procurement"
        },
        {
          "id": 56000289537,
          "value": "Plantations - Support Estate Supplies Division"
        },
        {
          "id": 56000289493,
          "value": "Plantations - Support Finance -  Accounts & Taxation"
        },
        {
          "id": 56000289519,
          "value": "Plantations - Support Finance - Ama Trails"
        },
        {
          "id": 56000289496,
          "value": "Plantations - Support Finance - Plantations"
        },
        {
          "id": 56000289531,
          "value": "Plantations - Support Forest Resources Management"
        },
        {
          "id": 56000289457,
          "value": "Plantations - Support Human Resource"
        },
        {
          "id": 56000289484,
          "value": "Plantations - Support Medical"
        },
        {
          "id": 56000289459,
          "value": "Plantations - Support Monsooning Operations"
        },
        {
          "id": 56000289511,
          "value": "Plantations - Support Plantation Trails"
        },
        {
          "id": 56000289514,
          "value": "Plantations - Support Procurement"
        },
        {
          "id": 56000289477,
          "value": "Plantations - Support Research and Development"
        },
        {
          "id": 56000289483,
          "value": "Plantations - Support Safety"
        },
        {
          "id": 56000289541,
          "value": "Plantations - Support Secretarial & Legal"
        },
        {
          "id": 56000289540,
          "value": "Plantations - Support SHE"
        },
        {
          "id": 56000289474,
          "value": "Plantations - Support Sustainability"
        },
        {
          "id": 56000289542,
          "value": "Plantations - Support Tea Sales"
        },
        {
          "id": 56000289209,
          "value": "Plantations (Plan_D_TCL)"
        },
        {
          "id": 56000289525,
          "value": "Plantations Support - Operations"
        },
        {
          "id": 56000288908,
          "value": "Procurement"
        },
        {
          "id": 56000289237,
          "value": "Procurement (Mate_D_TCL)"
        },
        {
          "id": 56000288897,
          "value": "Procurement & ESD"
        },
        {
          "id": 56000289252,
          "value": "Procurement & ESD (PRO&ESD_D_TCL)"
        },
        {
          "id": 56000289366,
          "value": "Procurement UK"
        },
        {
          "id": 56000289337,
          "value": "Product  Supply Organization"
        },
        {
          "id": 56000289149,
          "value": "Product Supply Organisation"
        },
        {
          "id": 56000288876,
          "value": "Product Supply Organization"
        },
        {
          "id": 56000288933,
          "value": "Product Supply Organization (Product_Supply_Organization)"
        },
        {
          "id": 56000289348,
          "value": "Product_Supply_Organization"
        },
        {
          "id": 56000288944,
          "value": "Production"
        },
        {
          "id": 56000289058,
          "value": "Production (Aurangabad)"
        },
        {
          "id": 56000289054,
          "value": "Production (Bangalore)"
        },
        {
          "id": 56000289309,
          "value": "Production (Indore)"
        },
        {
          "id": 56000289283,
          "value": "Production (Kellyden)"
        },
        {
          "id": 56000289210,
          "value": "Production (Prod_D_TCL)"
        },
        {
          "id": 56000289089,
          "value": "Production (PROD_D_TCVCL)"
        },
        {
          "id": 56000289302,
          "value": "Production (Pullivasal PC)"
        },
        {
          "id": 56000289441,
          "value": "Production & Dispatch"
        },
        {
          "id": 56000289131,
          "value": "Production-Production"
        },
        {
          "id": 56000289148,
          "value": "ProductSupplyOrganization"
        },
        {
          "id": 56000289319,
          "value": "Project"
        },
        {
          "id": 56000289134,
          "value": "Project Concord"
        },
        {
          "id": 56000289291,
          "value": "Project Office"
        },
        {
          "id": 56000288962,
          "value": "Projects Office"
        },
        {
          "id": 56000289142,
          "value": "PSO"
        },
        {
          "id": 56000289448,
          "value": "PSO and CSMO"
        },
        {
          "id": 56000289013,
          "value": "Pullivasal Packeting Centre"
        },
        {
          "id": 56000289064,
          "value": "Purchase"
        },
        {
          "id": 56000289021,
          "value": "Purchase Department"
        },
        {
          "id": 56000289087,
          "value": "Purchasing"
        },
        {
          "id": 56000289119,
          "value": "Purchasing (PURC_D_TCVCL)"
        },
        {
          "id": 56000289037,
          "value": "QA"
        },
        {
          "id": 56000289332,
          "value": "QA & RA"
        },
        {
          "id": 56000289345,
          "value": "QA_&_Regulatory_Affairs"
        },
        {
          "id": 56000289333,
          "value": "QA&RA"
        },
        {
          "id": 56000289414,
          "value": "QC & QA"
        },
        {
          "id": 56000288946,
          "value": "QM"
        },
        {
          "id": 56000288928,
          "value": "Quality"
        },
        {
          "id": 56000289097,
          "value": "QUALITY ASSURANCE"
        },
        {
          "id": 56000288880,
          "value": "Quality Assurance & Regulatory Affairs"
        },
        {
          "id": 56000289129,
          "value": "Quality Assurance & Regulatory Affairs (QA_&_Regulatory_Affairs)"
        },
        {
          "id": 56000288941,
          "value": "Quality Control"
        },
        {
          "id": 56000289125,
          "value": "Quality Control (QC_D_TCVCL)"
        },
        {
          "id": 56000289211,
          "value": "Quality Control (Qual_D_TCL)"
        },
        {
          "id": 56000289053,
          "value": "Quality Department"
        },
        {
          "id": 56000288976,
          "value": "QUALITY MANAGEMENT"
        },
        {
          "id": 56000289161,
          "value": "R & D"
        },
        {
          "id": 56000288950,
          "value": "R & D department"
        },
        {
          "id": 56000288981,
          "value": "R&D"
        },
        {
          "id": 56000289321,
          "value": "R&D (Innocenter)"
        },
        {
          "id": 56000289216,
          "value": "R&D (R&D)"
        },
        {
          "id": 56000288979,
          "value": "R&D Beverages"
        },
        {
          "id": 56000289226,
          "value": "R&D Beverages (R&D_Beverages)"
        },
        {
          "id": 56000289057,
          "value": "R&D Foods"
        },
        {
          "id": 56000289206,
          "value": "R&D Foods (R&D_Foods)"
        },
        {
          "id": 56000289001,
          "value": "R&D RTD"
        },
        {
          "id": 56000289225,
          "value": "R&D RTD (R&D_RTD)"
        },
        {
          "id": 56000289109,
          "value": "R&D Soulfull"
        },
        {
          "id": 56000289192,
          "value": "R&DBeverages"
        },
        {
          "id": 56000289143,
          "value": "R&DFoods"
        },
        {
          "id": 56000289120,
          "value": "R&DRTD"
        },
        {
          "id": 56000289027,
          "value": "R&G Department"
        },
        {
          "id": 56000329411,
          "value": "RAF Catalog Access"
        },
        {
          "id": 56000289310,
          "value": "Raw Tea"
        },
        {
          "id": 56000289440,
          "value": "Raw tea and Blending"
        },
        {
          "id": 56000288890,
          "value": "Regional Human Resources"
        },
        {
          "id": 56000289017,
          "value": "Regional_HR_Water"
        },
        {
          "id": 56000289203,
          "value": "Research & Development"
        },
        {
          "id": 56000289509,
          "value": "Research & Development - Analytical"
        },
        {
          "id": 56000289491,
          "value": "Research & Development - Beverages"
        },
        {
          "id": 56000289487,
          "value": "Research & Development - Foods"
        },
        {
          "id": 56000289517,
          "value": "Research & Development - Packaging Development"
        },
        {
          "id": 56000289479,
          "value": "Research & Development - RTD"
        },
        {
          "id": 56000289501,
          "value": "Research & Development - Soulfull"
        },
        {
          "id": 56000288969,
          "value": "Research and Development"
        },
        {
          "id": 56000289244,
          "value": "Research and Development (R&D _D_TCL)"
        },
        {
          "id": 56000289290,
          "value": "Resource"
        },
        {
          "id": 56000289415,
          "value": "Retail"
        },
        {
          "id": 56000289412,
          "value": "ROW"
        },
        {
          "id": 56000288893,
          "value": "RTD"
        },
        {
          "id": 56000289495,
          "value": "RTD - Finance & Legal"
        },
        {
          "id": 56000289508,
          "value": "RTD - Human Resources"
        },
        {
          "id": 56000289516,
          "value": "RTD - Procurement"
        },
        {
          "id": 56000289467,
          "value": "RTD - Sales"
        },
        {
          "id": 56000289456,
          "value": "RTD - Supply Chain"
        },
        {
          "id": 56000289473,
          "value": "RTD - Technical Operations"
        },
        {
          "id": 56000289485,
          "value": "RTD - Water Marketing"
        },
        {
          "id": 56000289228,
          "value": "RTD (RTD)"
        },
        {
          "id": 56000289334,
          "value": "RTR Associate"
        },
        {
          "id": 56000289041,
          "value": "S&OP"
        },
        {
          "id": 56000289062,
          "value": "Safety"
        },
        {
          "id": 56000289171,
          "value": "Safety (Safe_D_TCL)"
        },
        {
          "id": 56000289260,
          "value": "Safety, Health and Environment"
        },
        {
          "id": 56000288864,
          "value": "Sales"
        },
        {
          "id": 56000289092,
          "value": "Sales - MIS"
        },
        {
          "id": 56000289146,
          "value": "Sales (Sales)"
        },
        {
          "id": 56000288954,
          "value": "Sales & Marketing"
        },
        {
          "id": 56000289190,
          "value": "Sales & Marketing (Sale_D_TCL)"
        },
        {
          "id": 56000289034,
          "value": "Sales & Marketing Support"
        },
        {
          "id": 56000289447,
          "value": "Sales and Marketing"
        },
        {
          "id": 56000288886,
          "value": "Sales Enabling Organization"
        },
        {
          "id": 56000289086,
          "value": "Sales Enabling Organization (Sales_Enabling_Organization)"
        },
        {
          "id": 56000289327,
          "value": "Sales- Alternate Channels"
        },
        {
          "id": 56000289198,
          "value": "Sales- Value Business"
        },
        {
          "id": 56000289427,
          "value": "Sales/Customer Service"
        },
        {
          "id": 56000289430,
          "value": "Sales�"
        },
        {
          "id": 56000289409,
          "value": "SAP"
        },
        {
          "id": 56000288953,
          "value": "SBUX Project"
        },
        {
          "id": 56000288936,
          "value": "SDC-Maintenance"
        },
        {
          "id": 56000288916,
          "value": "Secretarial & Legal"
        },
        {
          "id": 56000289235,
          "value": "Secretarial & Legal (Secr_D_TCL)"
        },
        {
          "id": 56000289023,
          "value": "Security"
        },
        {
          "id": 56000289408,
          "value": "Service"
        },
        {
          "id": 56000289437,
          "value": "Service, Vending Business"
        },
        {
          "id": 56000289083,
          "value": "Shared Service"
        },
        {
          "id": 56000289261,
          "value": "SHE"
        },
        {
          "id": 56000289284,
          "value": "SIPO DOCTORS"
        },
        {
          "id": 56000289326,
          "value": "Softpack"
        },
        {
          "id": 56000289398,
          "value": "Solubles Business"
        },
        {
          "id": 56000289431,
          "value": "Solubles Bussiness"
        },
        {
          "id": 56000289488,
          "value": "Soulfull Business - Marketing"
        },
        {
          "id": 56000289108,
          "value": "Soulfull Business Support"
        },
        {
          "id": 56000289300,
          "value": "Southern MJV - Plannnig"
        },
        {
          "id": 56000288985,
          "value": "Special Projects Office"
        },
        {
          "id": 56000289164,
          "value": "Speciality"
        },
        {
          "id": 56000289297,
          "value": "SRISHTI -A PUBLIC CHARITABLE TRUST"
        },
        {
          "id": 56000289265,
          "value": "Srishti Trust Office"
        },
        {
          "id": 56000289446,
          "value": "Store"
        },
        {
          "id": 56000289117,
          "value": "Store-Packing Material"
        },
        {
          "id": 56000289019,
          "value": "Stores"
        },
        {
          "id": 56000288895,
          "value": "Strategy and M&A"
        },
        {
          "id": 56000289180,
          "value": "Strategy and M&A (Strategy_and_M&A)"
        },
        {
          "id": 56000289199,
          "value": "StrategyandM&A"
        },
        {
          "id": 56000288973,
          "value": "Sunticoppa Estate"
        },
        {
          "id": 56000288999,
          "value": "Supply & Support"
        },
        {
          "id": 56000289096,
          "value": "Supply Chain"
        },
        {
          "id": 56000289186,
          "value": "Supply Chain - HO"
        },
        {
          "id": 56000289007,
          "value": "Supply Chain Management"
        },
        {
          "id": 56000289126,
          "value": "SupplyChain"
        },
        {
          "id": 56000289103,
          "value": "Sustainability"
        },
        {
          "id": 56000289193,
          "value": "Sustainability (Sustainability)"
        },
        {
          "id": 56000288884,
          "value": "Sustainability & Communication"
        },
        {
          "id": 56000288945,
          "value": "Swastha"
        },
        {
          "id": 56000289200,
          "value": "System"
        },
        {
          "id": 56000289382,
          "value": "System1"
        },
        {
          "id": 56000289031,
          "value": "System2"
        },
        {
          "id": 56000289158,
          "value": "System3"
        },
        {
          "id": 56000289080,
          "value": "System4"
        },
        {
          "id": 56000289329,
          "value": "System5"
        },
        {
          "id": 56000289025,
          "value": "Tata Cha"
        },
        {
          "id": 56000289555,
          "value": "Tata Consumer Products Limited"
        },
        {
          "id": 56000289267,
          "value": "Tata High Range Hospital"
        },
        {
          "id": 56000289123,
          "value": "Tata Nutrikart - Bill Verification"
        },
        {
          "id": 56000288980,
          "value": "Tata Tetley Operations"
        },
        {
          "id": 56000289303,
          "value": "TB&B Support"
        },
        {
          "id": 56000289039,
          "value": "TBB - Kolkata"
        },
        {
          "id": 56000288984,
          "value": "TBB-Finance"
        },
        {
          "id": 56000288987,
          "value": "TBB-Planning"
        },
        {
          "id": 56000289074,
          "value": "TC Stores Pollibetta"
        },
        {
          "id": 56000289313,
          "value": "TCL HO Dispensary"
        },
        {
          "id": 56000288870,
          "value": "TCP IT"
        },
        {
          "id": 56000289370,
          "value": "TCPL US"
        },
        {
          "id": 56000289368,
          "value": "TCPL_US"
        },
        {
          "id": 56000289035,
          "value": "Tea Blending"
        },
        {
          "id": 56000288894,
          "value": "Tea Buying"
        },
        {
          "id": 56000288877,
          "value": "Tea Buying & Blending"
        },
        {
          "id": 56000288882,
          "value": "Tea Buying & Blending."
        },
        {
          "id": 56000289008,
          "value": "Tea Estate"
        },
        {
          "id": 56000288959,
          "value": "Tea Extraction"
        },
        {
          "id": 56000289233,
          "value": "Tea Extraction (Tea_Extraction)"
        },
        {
          "id": 56000289098,
          "value": "Tea Extraction Business"
        },
        {
          "id": 56000288912,
          "value": "Tea Factory Operations"
        },
        {
          "id": 56000289217,
          "value": "Tea Factory Operations (TFO_D_TCL)"
        },
        {
          "id": 56000288965,
          "value": "Tea Operations"
        },
        {
          "id": 56000289248,
          "value": "Tea Operations (TEOP_D_TCL)"
        },
        {
          "id": 56000288994,
          "value": "Tea Sales"
        },
        {
          "id": 56000289336,
          "value": "Tea Sales (TeaSales _D_TCL)"
        },
        {
          "id": 56000289121,
          "value": "TeaBuying & Blending"
        },
        {
          "id": 56000289189,
          "value": "TeaBuying&Blending"
        },
        {
          "id": 56000289312,
          "value": "Tech Operations"
        },
        {
          "id": 56000289195,
          "value": "Technical Operations"
        },
        {
          "id": 56000289091,
          "value": "Technical_Operations"
        },
        {
          "id": 56000289202,
          "value": "Test"
        },
        {
          "id": 56000289270,
          "value": "The High Range School  High Range Education Trust"
        },
        {
          "id": 56000289115,
          "value": "The High Range School – High Range Education Trust"
        },
        {
          "id": 56000289045,
          "value": "Timber Department"
        },
        {
          "id": 56000289065,
          "value": "Time Office"
        },
        {
          "id": 56000289128,
          "value": "TPM & Safety"
        },
        {
          "id": 56000289403,
          "value": "Treasury & Admin"
        },
        {
          "id": 56000289101,
          "value": "TTEI Ops"
        },
        {
          "id": 56000289451,
          "value": "TTP"
        },
        {
          "id": 56000289033,
          "value": "Ubban Estate"
        },
        {
          "id": 56000289030,
          "value": "Unit Head(SFS)"
        },
        {
          "id": 56000289402,
          "value": "VAT & Accounts"
        },
        {
          "id": 56000288958,
          "value": "Warehouse"
        },
        {
          "id": 56000289088,
          "value": "Warehouse (WARE_D_TCVCL)"
        },
        {
          "id": 56000289273,
          "value": "warehousing & CFA"
        },
        {
          "id": 56000289068,
          "value": "Water Marketing"
        },
        {
          "id": 56000289212,
          "value": "Water Marketing (Water_Marketing)"
        },
        {
          "id": 56000289355,
          "value": "Water Vertical - Personnel & Admin"
        },
        {
          "id": 56000289016,
          "value": "Water Vertical - Personnel & Admin."
        },
        {
          "id": 56000289009,
          "value": "Welfare"
        },
        {
          "id": 56000289489,
          "value": "Welfare - High Range Hospital"
        },
        {
          "id": 56000288960,
          "value": "Woshully Estate"
        }
      
]

def get_department_name_by_id(department_id):
    for dept in DEPARTMENT_MAPPINGS:
        if dept["id"] == department_id:
            return dept["value"]
    return "N/A"

def get_department_id_by_name(name):
    for dept in DEPARTMENT_MAPPINGS:
        if dept["value"].lower() == name.lower():
            return dept["id"]
    return None

