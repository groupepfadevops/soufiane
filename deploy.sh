#!/bin/bash

echo "Starting deployment..."

# Define the deployment directory
DEPLOY_DIR="/path/to/deployment/directory"

# Create the deployment directory if it doesn't exist
mkdir -p $DEPLOY_DIR

# Copy the application files to the deployment directory
cp -r src/* $DEPLOY_DIR

echo "Deployment completed. Files have been copied to $DEPLOY_DIR."
