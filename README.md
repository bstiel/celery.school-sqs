# Celery with SQS as a Message Broker

This projects contains the source code examples accompanying my blog post:

https://celery.school/posts/amazon-sqs-celery-broker/

## Setup

1. Create a virtual environment and install the dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

2. Create the SQS queue in the AWS Management Console

3. Set your AWS credentials, SQS queue name and Url in `worker.py`

4. Start `producer.py` and the Celery worker via Honcho:

```bash
$ honcho start
```
