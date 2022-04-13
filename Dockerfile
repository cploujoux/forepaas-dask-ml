FROM daskdev/dask:2022.1.1-py3.8

ENV PYTHONUNBUFFERED=1

COPY requirements-ml-minimal.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

RUN apt-get update
RUN apt-get install -y curl
# install minio client
RUN \
    curl https://dl.min.io/client/mc/release/linux-amd64/mc > /usr/bin/mc && \
    chmod +x /usr/bin/mc
