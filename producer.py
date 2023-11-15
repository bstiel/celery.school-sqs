import logging
from time import sleep
from worker import app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


while True:
    async_result = app.send_task("do_something")
    logger.info(async_result)
    sleep(2.0)
