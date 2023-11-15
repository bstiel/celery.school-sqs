from celery import Celery

sqs_queue = ""
sqs_queue_url = ""
aws_access_key = ""
aws_secret_key = ""

# sqs
app = Celery(
    "app",
    broker_url=f"sqs://{aws_access_key}:{aws_secret_key}@",
    broker_connection_retry_on_startup=True,
    broker_connection_retry=True,
    broker_transport_options={
        "region": "us-east-1",
        "predefined_queues": {
            "celery": {
                "url": sqs_queue_url,
                "access_key_id": aws_access_key,
                "secret_access_key": aws_secret_key,
            }
        },
    },
    task_create_missing_queues=False,
)


@app.task(name="do_something", bind=True)
def do_something(self):
    print("Message received")
