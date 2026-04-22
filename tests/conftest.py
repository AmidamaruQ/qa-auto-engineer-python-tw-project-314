import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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
        or "http://server"
    )


@pytest.fixture
def driver(request):
    logger = get_logger("driver")
    options = Options()
    # Chromium runs inside a Linux container in CI, so it needs headless-safe flags.
    options.binary_location = os.getenv("CHROME_BINARY", "/usr/bin/chromium")
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-software-rasterizer")

    logger.info("Starting Chrome browser")
    service = Service(
        executable_path=os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
    )
    browser = webdriver.Chrome(service=service, options=options)
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
