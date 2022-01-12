#!/bin/sh
# echo "Launching cluster ..."
# helm repo add dask https://helm.dask.org/
# helm repo update
# helm install my-dask dask/dask
# helm upgrade my-dask dask/dask -f dask_config.yaml
# echo "Cluster launched"

echo "Exporting variables..."
export DASK_SCHEDULER="127.0.0.1"
export DASK_SCHEDULER_UI_IP="127.0.0.1"
export DASK_SCHEDULER_PORT=8080
export DASK_SCHEDULER_UI_PORT=8081
echo  "Post forwarding..."
kubectl port-forward --namespace default svc/my-dask-scheduler $DASK_SCHEDULER_PORT:8786 &
kubectl port-forward --namespace default svc/my-dask-scheduler $DASK_SCHEDULER_UI_PORT:80 &

echo tcp://$DASK_SCHEDULER:$DASK_SCHEDULER_PORT               -- Dask Client connection
echo http://$DASK_SCHEDULER_UI_IP:$DASK_SCHEDULER_UI_PORT     -- Dask dashboard