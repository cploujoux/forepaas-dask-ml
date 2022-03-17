# forepaas-dask-ml

## Getting started

First, go to the repository root and build the Docker image locally :

```
docker build . -t dask-pod.0.0.2
```

Then, create a local Minio server and copy the Python test file inside a bucket : 

```
mc alias set my-storage http://localhost:9000 user password
mc mb my-test-storage/my-minio-bucket
mc cp ./test_scripts/test_dask_ml.py my-test-storage/my-minio-bucket/test_dask_ml.py
```

Adpat values to correspond to your paths and urls

In a terminal, execute the following command :

```
helm install my-dask-1 ./dask_helm_chart_1
```

