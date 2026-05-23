import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERVICENOW_INSTANCE = os.getenv("SERVICENOW_INSTANCE")
SERVICENOW_USERNAME = os.getenv("SERVICENOW_USERNAME")
SERVICENOW_PASSWORD = os.getenv("SERVICENOW_PASSWORD")


def search_knowledge_articles(query):
    if not SERVICENOW_INSTANCE:
        raise ValueError("SERVICENOW_INSTANCE is missing from .env")

    url = f"{SERVICENOW_INSTANCE}/api/now/table/kb_knowledge"

    params = {
        "sysparm_limit": 5,
        "sysparm_fields": "number,short_description,text,workflow_state,sys_created_on",
        "sysparm_query": (
            f"short_descriptionLIKE{query}"
            f"^ORtextLIKE{query}"
            f"^ORshort_descriptionLIKEVPN"
            f"^ORshort_descriptionLIKEpassword"
            f"^ORshort_descriptionLIKEemail"
            f"^ORshort_descriptionLIKEnetwork"
        )
    }

    response = requests.get(
        url,
        auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD),
        params=params,
        timeout=20
    )

    response.raise_for_status()

    return response.json()["result"]