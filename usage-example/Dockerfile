FROM docker.io/andrebaceti/pumpwood-streamlit-app:0.0

ENV DASHBOARD_NAME="change-dashboard-codes"
#################################

COPY requirements/requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

# Copy dashboard to docker image
COPY dashboard /code/dashboard
