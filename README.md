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
FROM docker.io/andrebaceti/pumpwood-streamlit-app:0.0

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

## Dashboard codes
Dashboard codes need at least two files `app.py` and `dashboard.py`.

### app.py
Entry point for streamlit, it is normally just a simple code. Example:
```python
from dashboard import Dashboard

dash_obj = Dashboard()
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
