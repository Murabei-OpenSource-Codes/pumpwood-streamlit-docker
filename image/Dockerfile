FROM python:3.8-slim-bullseye

# Install packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential \
    unixodbc-dev \
    curl \
    gnupg2 \
    libpq-dev
RUN apt-get clean

# Kong load balancer
ENV SERVICE_URL="http://pumpwood-streamlit-app:5000/"

# Microservice
ENV MICROSERVICE_NAME='microservice--streamlit'
ENV MICROSERVICE_URL="http://load-balancer:8000/"
ENV MICROSERVICE_USERNAME='microservice--streamlit'
ENV MICROSERVICE_PASSWORD='microservice--streamlit'
ENV MICROSERVICE_SSL='False'

# Streamlit Configuration
ENV DASHBOARD_NAME="example-dashboard"
#################################

COPY requirements/requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

COPY code /code
WORKDIR /code/

CMD ["bash", "/code/start_server.sh"]
