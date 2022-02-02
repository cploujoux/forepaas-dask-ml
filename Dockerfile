FROM python:3.8.12-buster

COPY requirements-ml-minimal.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

# install minio client
RUN \
    curl https://dl.min.io/client/mc/release/linux-amd64/mc > /usr/bin/mc && \
    chmod +x /usr/bin/mc
# RUN ./minio server /data
# RUN mc --help

RUN echo "docker finished"

