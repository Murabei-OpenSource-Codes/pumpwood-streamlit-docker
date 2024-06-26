"""Register Dashboard on Auth App."""
import os
from pumpwood_communication.microservices import PumpWoodMicroService

# Microservice
MICROSERVICE_NAME = os.getenv("MICROSERVICE_NAME")
MICROSERVICE_URL = os.getenv("MICROSERVICE_URL")
MICROSERVICE_USERNAME = os.getenv("MICROSERVICE_USERNAME")
MICROSERVICE_PASSWORD = os.getenv("MICROSERVICE_PASSWORD")

# Kong and Streamlit configs
SERVICE_URL = os.getenv("SERVICE_URL")
DASHBOARD_NAME = os.getenv("DASHBOARD_NAME")

# Creating Microservice
print("## Log in PumpWoodMicroService")
microservice = PumpWoodMicroService(
    name=MICROSERVICE_NAME, server_url=MICROSERVICE_URL,
    username=MICROSERVICE_USERNAME, password=MICROSERVICE_PASSWORD)
microservice.login()

# Register Service
print("## Registering streamlit dashboard: [{}]".format(DASHBOARD_NAME))
service_object = microservice.save({
    "model_class": "KongService",
    'service_url': SERVICE_URL,
    'service_name': "streamlit-" + DASHBOARD_NAME,
    'description': "Streamlit Dashboard | " + DASHBOARD_NAME,
    'notes': "Service to serve streamlit Dashboard" + DASHBOARD_NAME,
    'dimensions': {
        "microservice": "pumpwood-streamlit-app",
        "dashboard_name": "DASHBOARD_NAME"},
})

route_object = {
    "model_class": "KongRoute",
    "service_id": service_object["pk"],
    "route_url": "/streamlit/" + DASHBOARD_NAME,
    "route_name": "streamlit-" + DASHBOARD_NAME,
    "route_type": "datavis",
    "description": "streamlit dashboard end-point: " + DASHBOARD_NAME,
    "notes": "",
    "dimensions": {
        "microservice": "pumpwood-streamlit-app",
        "dashboard_name": DASHBOARD_NAME},
    "icon": None,
    "extra_info": {}}
microservice.save(route_object)
