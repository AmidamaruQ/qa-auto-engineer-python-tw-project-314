import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.pages import Pages
from utils import configure_logging, get_logger


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help="Base URL for UI tests.",
    )


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    configure_logging()

@pytest.fixture(scope="session")
def base_url(request):
    return (
        os.getenv("APP_BASE_URL")
        or "http://127.0.0.1:5173"
    )


@pytest.fixture
def driver(request):
    logger = get_logger("driver")
    options = Options()
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    logger.info("Starting Chrome browser")
    browser = webdriver.Chrome(options=options)
    yield browser
    logger.info("Closing Chrome browser")
    browser.quit()


@pytest.fixture
def app(driver, base_url):
    logger = get_logger("app")
    app = Pages(driver)
    logger.info("Opening base URL: %s", base_url)
    app.base_page.open(base_url)
    return app


@pytest.fixture
def logged_app(app):
    logger = get_logger("app")
    logger.info("Authorizing test user")
    app.login_page.login("admin", "adminhexlet1122")
    return app
