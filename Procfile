producer: python producer.py
worker: celery --app=worker.app worker --pool=solo --concurrency=1 --loglevel=INFO --queues=celery