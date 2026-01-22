import logging
from functools import partial

from app.config.config_manager import ConfigManager
from app.constant.task_name import PollingTask
from app.util.http_client import ApHttpClient
from app.util.polling_client import ApPolingService

logger = logging.getLogger(__name__)

class LoaderHealthCheck:
    def __init__(self):
        self.task_name = PollingTask.LOADER_HEALTH_CHECK.name
        self.interval = 60
        self.polling_service = ApPolingService()
        self.apSettings = ConfigManager()

    def start_task(self):
        http_client = ApHttpClient(self.apSettings.LOADER_BASE_URL)

        do_task = partial(http_client.request, "GET", "/health")
        on_result = self.handle_respose

        self.polling_service.start_task(self.task_name, self.interval, do_task, on_result)
        logger.info(f"Loader Health Check Task Started.")

    def stop_task(self):
        self.polling_service.stop_task(task_name=self.task_name)
        logger.info(f"Loader Health Check Task stopped: {self.task_name}")

    def handle_respose(self, response):
        if response and response.status_code == 200:
            data = response.json()
            logger.info(f"result:{data}")
        else:
            logger.error(f"Loader 응답이 올바르지 않습니다. status_code:{response.status_code}")
