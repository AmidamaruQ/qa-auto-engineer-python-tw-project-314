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
    implementation = os.getenv("IMPLEMENTATION")
    option_value = request.config.getoption("--base-url")

    if option_value:
        return option_value

    if implementation:
        return f"http://{implementation}.test"

    return os.getenv("APP_BASE_URL", "http://localhost:5173")


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("LOGIN", "admin"),
        "password": os.getenv("PASSWORD", "adminhexlet1122"),
    }


@pytest.fixture(scope="session")
def expected_profile_name():
    return os.getenv("PROFILE_NAME", "Jane Doe")


@pytest.fixture
def driver():
    logger = get_logger("driver")
    options = Options()
    chrome_binary = os.getenv("CHROME_BINARY")

    if chrome_binary:
        options.binary_location = chrome_binary

    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-software-rasterizer")

    logger.info("Starting Chrome browser")
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    service = (
        Service(executable_path=chromedriver_path)
        if chromedriver_path
        else Service()
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
def logged_app(app, credentials):
    logger = get_logger("app")
    logger.info("Authorizing test user")
    app.login_page.login(credentials["username"], credentials["password"])
    return app
