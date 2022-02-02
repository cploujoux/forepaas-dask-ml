#!/bin/bash

### POSTGRES

# Deploy Postgres
kubectl create -f ./postgres_manifests_folder/

# Seed Postgres DB
kubectl exec -n connectors -it $(kubectl get pod -n connectors -l "app=postgres" -o jsonpath='{.items[0].metadata.name}') -- sh -c "psql -f /home/postgres/seed/seed.sql"

# To check that DB is instanciated correctly, run :
# psql -h 127.0.0.1 -U root --password -p {NODE_PORT} {DATABASE_NAME}
# then \d+

### MINIO

# Remove Minio repo if necessary
helm repo remove minio

# Add minio charts
helm repo add minio https://charts.min.io/

# Deploy Minio pods
helm install --set accessKey=my-access-key --set secretKey=my-secret-key stable/minio --generate-name

# Then, follow the instructions given in the CLI, like so :
# 1. export POD_NAME=$(kubectl get pods --namespace default -l "release=<my-release>" -o jsonpath="{.items[0].metadata.name}")
# Create Minio external service to be able to listen on port 9000
# 2. k expose deployment <deployment_name> --type=LoadBalancer --name=<whatever_service_name>

# Copy a file from a Minio bucket to the localhost
./mc cp <alias>/<bucket>/<file> .


### DASK

# Connect Dask 
source connect_dask_no_jupyter.sh  

