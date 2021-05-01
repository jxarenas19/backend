FROM python:3.7
ARG GITLAB_TOKEN=NgsNuMFZmUgMebSU2jBA
WORKDIR /usr/src/app

ADD . .

RUN pip install setuptools==30.1.0 && pip install --no-cache-dir -r requirements.txt && python setup.py install

RUN mv /usr/src/app/entrypoint.sh /entrypoint.sh && \
    chmod +x /entrypoint.sh && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
