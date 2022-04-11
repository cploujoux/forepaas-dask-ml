export DASK_SCHEDULER="127.0.0.1"
export DASK_SCHEDULER_UI_IP="127.0.0.1"
export DASK_SCHEDULER_PORT=8080
export DASK_SCHEDULER_UI_PORT=8081
kubectl port-forward --namespace default svc/daskjob-sample-dask-job-scheduler $DASK_SCHEDULER_PORT:8786 &
kubectl port-forward --namespace default svc/daskjob-sample-dask-job-scheduler $DASK_SCHEDULER_UI_PORT:80 &

echo tcp://$DASK_SCHEDULER:$DASK_SCHEDULER_PORT               -- Dask Client connection
echo http://$DASK_SCHEDULER_UI_IP:$DASK_SCHEDULER_UI_PORT     -- Dask dashboard