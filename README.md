# pumpwood-streamlit-docker
Base docker image to create Streamlit dashboards associated with
Pumpwood Systems.

<p align="center" width="60%">
  <img src="doc/sitelogo-horizontal.png" /> <br>

  <a href="https://en.wikipedia.org/wiki/Cecropia">
    Pumpwood is a native brasilian tree
  </a> which has a symbiotic relation with ants (Murabei)
</p>

# Usage of the docker image
This image can be used as base to create new dashboards. Example of
docker image.

```
# User pumpwood-streamlit-app as base image
FROM docker.io/andrebaceti/pumpwood-streamlit-app:[version]

# Set a dashboard name, this will be registered at kong using route
# /streamlit/$DASHBOARD_NAME
ENV DASHBOARD_NAME="change-dashboard-codes"
#################################

# Install any other python requirements used with
# streamlit to create dashboard
COPY requirements/requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

# Copy dashboard codes to image
COPY dashboard /code/dashboard
```

It is necessary to set `MICROSERVICE_URL`, `MICROSERVICE_USERNAME` and
`MICROSERVICE_PASSWORD` to log in server user on Pumpwood to register
the routes on pumpwood-auth.

## Environment variables
- **SERVICE_URL:** URL of the service that will serve the dashboard,
  use only the service base url starting with http and tralling `/`. Example:
  `http://pumpwood-streamlit-app:5000/`.
- **MICROSERVICE_URL:** Correpond to URL that will be called for Pumpwood
  end-points. It is usually the end-point correponding to Kong service mesh,
  example: `http://load-balancer:8000/`.
- **MICROSERVICE_USERNAME:** Username for the Pumpwood user used to register
  streamlit service and rote on Pumpwood. It is usually not set with default
  value `microservice--streamlit`.
- **MICROSERVICE_PASSWORD:** Password for Pumpwood used to register
  streamlit service and rote on Pumpwood. For develoment it is as default
  set as `microservice--streamlit`. **CHANGE THIS VALUE AT PRODUCTION**.
- **DASHBOARD_NAME:** Name of the dashboard that will be deployed. Name
  must comply with URL format, use snake-case without spaces and especial
  characters. container will serve route with base url as
  `streamlit/$DASHBOARD_NAME` with port 5000.

## Dashboard codes
Dashboard codes need at least two files `app.py` and `dashboard.py`.

### app.py
Entry point for Streamlit, it is normally just a simple code. Example:
```python
import os
from dashboard import Dashboard
from pumpwood_communication.microservices import PumpWoodMicroService

##########################################################################
# Read env variables to be used on local test of the dashboard.          #
# Passing a logged microservice to dashboard will disable authentication #
# !!! DO NOT USE AUTHENTICATED MICROSERVICE IN PRODUCTION DASHBOARDS !!! #
MICROSERVICE_URL = os.getenv('MICROSERVICE_URL')
MICROSERVICE_DASHBOARD_USERNAME = os.getenv('MICROSERVICE_DASHBOARD_USERNAME')
MICROSERVICE_DASHBOARD_PASSWORD = os.getenv('MICROSERVICE_DASHBOARD_PASSWORD')

microservice = None
if MICROSERVICE_DASHBOARD_USERNAME is not None:
    microservice = PumpWoodMicroService(
        name="dashboard-microservice",
        server_url=MICROSERVICE_URL,
        username=MICROSERVICE_DASHBOARD_USERNAME,
        password=MICROSERVICE_DASHBOARD_PASSWORD,)
    microservice.login()

dash_obj = Dashboard(microservice=microservice)
dash_obj.run()
```

### dashboard.py
Code responsible for render dashboard. Dashboard inherit from abstract
class `PumpwoodStreamlitDashboard` from package `pumpwood_streamlit`, it
is necessary to implement `set_page_config` and `main_view` functions.

Code example:
```python
import os
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from pumpwood_streamlit.dashboard import PumpwoodStreamlitDashboard


class Dashboard(PumpwoodStreamlitDashboard):
    def set_page_config(self):
        #######################
        # Page configuration
        st.set_page_config(
            page_title="US Population Dashboard",
            page_icon="🏂",
            layout="wide",
            initial_sidebar_state="expanded")

    def main_view(self):
        alt.themes.enable("dark")

        #######################
        # Load data
        st.title('O dash mudou!')
```
