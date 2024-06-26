#!/bin/bash
echo "*******************"
echo "StreamLit Dashboard"
echo "*******************"
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
source "${SCRIPTPATH}/wait-for-auth.sh"

echo "# Registering service and routes"
python -u register_dashboards.py

echo "# Starting Streamlit"
cd dashboard/
streamlit run --server.headless="true" --server.address="0.0.0.0" --server.port="5000" --server.enableCORS="false" --server.enableXsrfProtection=false --browser.gatherUsageStats="false" --client.toolbarMode="viewer" --server.baseUrlPath "streamlit/$DASHBOARD_NAME" app.py
