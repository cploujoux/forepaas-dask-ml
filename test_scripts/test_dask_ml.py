#!/usr/bin/env python



from dask.distributed import Client

print('connecting')

client = Client("127.0.0.1:8786")

print("connected")



import dask
from dask.utils import format_bytes

import dask_ml.cluster
import dask_ml.datasets

# import matplotlib.pyplot as plt



X, y = dask_ml.datasets.make_blobs(
    n_samples=100_000,
    n_features=50,
    centers=3,
    chunks=500,
)

format_bytes(X.nbytes)




X = X.persist()




km = dask_ml.cluster.KMeans(n_clusters=2, init_max_iter=2, oversampling_factor=10, random_state=0)

print("km done")

# get_ipython().run_line_magic('time', 'km.fit(X)')



# get_ipython().run_line_magic('matplotlib', 'inline')

# fig, ax = plt.subplots()
# ax.scatter(X[::20, 0], X[::20, 1], marker='.', c=km.labels_[::20],
#            cmap='viridis', alpha=0.25);

