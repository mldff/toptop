import pytest
from selenium import webdriver
from datetime import datetime
import logging


def pytest_configure(config):
    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
    log_file = f"E:\\auto\\jira\\logs\\log_{timestamp}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info("Pytest configured and logging started")


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
