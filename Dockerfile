FROM python:3.10.0-slim

ENV PYTHONUNBUFFERED=1

RUN groupadd -r app && \
    useradd --no-log-init -r -g app app -m

RUN apt-get update && \
	apt-get install -qy python3-pip && \
	ln -sf /usr/bin/pip3 /usr/bin/pip && \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*

ADD --chown=app:app requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD --chown=app:app . /

USER app
WORKDIR /

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000"]

EXPOSE 8000