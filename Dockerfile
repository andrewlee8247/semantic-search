FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN groupadd -r app && \
    useradd --no-log-init -r -g app app -m

RUN apt-get update && \
    apt-get install -qy python3-pip && \
    ln -sf /usr/bin/pip3 /usr/bin/pip && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=app:app requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app /app /semantic_search/app
COPY --chown=app:app /content /semantic_search/content

USER app
ENV PYTHONPATH="/:${PYTHONPATH}"
WORKDIR /semantic_search

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000"]

EXPOSE 8000
