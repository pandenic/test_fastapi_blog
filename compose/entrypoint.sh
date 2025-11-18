#!/bin/bash
set -o errexit  
set -o pipefail  

case "$CONTAINER_TYPE" in
    api)
        uv run alembic upgrade head;
        uv run uvicorn main:app --host 0.0.0.0 --port 8080 --app-dir /app/src
        ;;
    celery_worker)
        uv run celery -A services.celery.worker.celery_app worker --loglevel=info
        ;;
    flower)
        uv run celery -A services.celery.worker.celery_app flower --url-prefix=flower
        ;;
    *)
        echo "Unsupported CONTAINER_TYPE: $CONTAINER_TYPE" >&2
        exit 1
        ;;
esac