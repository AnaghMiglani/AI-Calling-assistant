FROM n8nio/n8n:latest

USER root

RUN apk add --no-cache python3 py3-pip

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install twilio

ENV PATH="/opt/venv/bin:$PATH"

USER node
