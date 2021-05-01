FROM python:3.7
ARG GITLAB_TOKEN=NgsNuMFZmUgMebSU2jBA
WORKDIR /usr/src/app

ADD . .

RUN pip install setuptools==30.1.0 && git clone https://gitlab-ci-token:${GITLAB_TOKEN}@gitlab.com/kiero-developers/backend-kiero/kmodels.git && \
    cd kmodels && git checkout develop && pip install --no-cache-dir -r requirements.txt && python setup.py install

RUN mv /usr/src/app/entrypoint.sh /entrypoint.sh && \
    chmod +x /entrypoint.sh && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
