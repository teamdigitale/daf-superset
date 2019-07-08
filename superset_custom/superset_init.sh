#!/bin/env bash

set -e

# Create a local admin user
fabmanager create-admin --app superset --firstname ${SUPERSET_ADMIN_FIRST_NAME} --lastname ${SUPERSET_ADMIN_LAST_NAME} --email ${SUPERSET_ADMIN_EMAIL} --username ${SUPERSET_ADMIN_USER} --password ${SUPERSET_ADMIN_PASS}

# Initialize the database
superset db upgrade

# Load some data to play with (disabled by default)
# superset load_examples

# Create default roles and permissions
superset init
