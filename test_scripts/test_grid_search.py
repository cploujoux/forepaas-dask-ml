import joblib
import dask.distributed
from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV

c = dask.distributed.Client()

X, y = make_classification(n_samples=10000, n_features=4, random_state=0)
estimator = SVC(gamma='auto', random_state=0, probability=True)

param_grid = {
    'C': [0.001, 0.1, 1.0, 2.5, 5, 10.0],
    'kernel': ['rbf', 'poly', 'linear'],
    'shrinking': [True, False],
}

grid_search = GridSearchCV(estimator, param_grid, verbose=2, cv=5, n_jobs=-1)

with joblib.parallel_backend("dask", scatter=[X, y]):
    grid_search.fit(X, y)

print(grid_search.best_params_, grid_search.best_score_)
