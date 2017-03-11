FROM openalpr/openalpr:latest

# Reset the entrypoint in parent Dockerfile
ENTRYPOINT []

WORKDIR /srv/platonix

RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt && \
    cd /srv/openalpr/src/bindings/python/ && \
    python3 setup.py install

COPY server.py server.py

CMD ["python3", "/srv/platonix/server.py"]
