from background_task import background
from logging import getLogger

logger = getLogger(__name__)

@background(schedule=10)
def demo_job():
    print("Task Done")