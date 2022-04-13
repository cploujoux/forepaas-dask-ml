# forepaas-dask-ml

## Getting started

First, go to the repository root and build the Docker images locally :

```
docker build . -t dask-pod.0.0.3
```

```
docker build -t dask-nomnio.0.0.1 -f Dockerfile.nominio .
```

Then, create a local Minio server and copy the Python test file inside a bucket : 
You can also you any other minio server that you have at disposition

```
mc alias set my-storage http://localhost:9000 user password
mc mb my-test-storage/my-minio-bucket
mc cp ./test_scripts/test.py my-test-storage/my-minio-bucket/test.py
```

Adpat the helm chart values to correspond to your paths and urls 

In a terminal, execute the following command to run the job using helm :

```
helm install my-dask ./dask_job_chart
```

After running your jobs you can run

```
helm delete my-dask 
```

## Operator

```
cd dask-operator
```

To setup the operator

```
make docker-build docker-push
```

NB: if you are running locally on minikube you will need to load the created docker image with 

```
minikube image load my.domain/dask-operator:0.0.1
```


To deploy the operator

```
make deploy
```



Deploy sample CR

```
kubeclt apply -f ./config/samples/charts_v1alpha1_daskjob.yaml
```

Add the end of the job you should then delete the CR
```
kubeclt delete -f ./config/samples/charts_v1alpha1_daskjob.yaml
```

To destroy the operator use 
```
make undeploy
```


## Test scripts

You can copy test.py into your minio server to test this operator

To use test2.py you can first setup the postgres database by running 

```
kubectl create -f ./postgres_manifests/
```

```
kubectl exec -n connectors -it $(kubectl get pod -n connectors -l "app=postgres" -o jsonpath='{.items[0].metadata.name}') -- sh -c "psql -f /home/postgres/seed/seed.sql"
```

You should then update the script to use the correct IP address for the postgres server.

If you are using minikube you should also run 
```
minikube tunnel
```
