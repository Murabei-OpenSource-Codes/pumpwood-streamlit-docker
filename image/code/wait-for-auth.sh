#!/bin/bash
set -e

until curl -sSf ${MICROSERVICE_URL}health-check/pumpwood-auth-app/ > /dev/null; do
  >&2 echo "${MICROSERVICE_URL}health-check/pumpwood-auth-app/ is unavailable"
  sleep 1
done
echo "${MICROSERVICE_URL}health-check/pumpwood-auth-app/ is ok!"
