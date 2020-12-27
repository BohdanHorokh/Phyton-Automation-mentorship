import logging.config

import allure
import pytest
from allure import attachment_type

from utils.driver_init import chrome_driver_init

from os import path
logging.conf = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

logging.config.fileConfig(logging.conf)
logger = logging.getLogger('root')


@pytest.fixture(scope='session')
def get_driver():
    driver = chrome_driver_init()
    logger.info('Initiating chrome driver')
    yield driver
    logger.info('Closing chrome driver')
    driver.quit()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    report = (yield).get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "report_" + report.when, report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    driver = request.node.funcargs['get_driver']
    # attach = driver.get_screenshot_as_png()
    if request.node.report_setup.failed or request.node.report_call.failed:
        allure.attach(driver.get_screenshot_as_png(), 'screenshot', attachment_type=attachment_type.PNG)
