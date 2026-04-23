import logging
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import TestConfig, load_config
from pages.app import Pages
from utils.logging import configure_logging


@pytest.fixture(scope="session")
def test_config() -> TestConfig:
    return load_config()


@pytest.fixture(scope="session")
def test_logger(test_config: TestConfig) -> logging.Logger:
    test_config.log_dir.mkdir(parents=True, exist_ok=True)
    logger = configure_logging(
        test_config.log_level,
        test_config.log_dir,
    )
    logging.captureWarnings(True)
    logger.info(
        "Logging initialised "
        "(implementation=%s, base_url=%s, log_dir=%s)",
        test_config.implementation or "custom",
        test_config.base_url,
        test_config.log_dir,
    )
    return logger


@pytest.fixture(scope="session")
def base_url(test_config: TestConfig) -> str:
    return test_config.base_url


def _configure_options(test_config: TestConfig) -> Options:
    options = Options()
    if test_config.headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument(f"--window-size={test_config.window_size}")
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"],
    )
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    chrome_binary = test_config.chrome_binary
    if chrome_binary and Path(chrome_binary).exists():
        options.binary_location = chrome_binary

    return options


def _prepare_driver(
    driver: webdriver.Chrome,
    base_url: str,
) -> None:
    driver.get(base_url)
    driver.delete_all_cookies()
    driver.execute_script(
        "window.localStorage.clear(); window.sessionStorage.clear();",
    )


def _new_browser(
    base_url: str,
    test_config: TestConfig,
) -> webdriver.Chrome:
    options = _configure_options(test_config)
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(test_config.page_load_timeout)
    driver.implicitly_wait(test_config.implicit_wait)
    _prepare_driver(driver, base_url)
    return driver


@pytest.fixture
def driver(
    base_url: str,
    test_config: TestConfig,
    test_logger: logging.Logger,
):
    test_logger.debug(
        "Creating new browser instance",
    )
    browser = _new_browser(base_url, test_config)
    yield browser
    test_logger.debug(
        "Closing browser instance",
    )
    browser.quit()


@pytest.fixture
def pages(driver, base_url: str):
    return Pages(driver, base_url)


@pytest.fixture
def logged_in_pages(pages):
    from tests.constants import USER

    pages.login.login(USER["login"], USER["password"])
    return pages


@pytest.fixture
def login_page(pages):
    return pages.login


@pytest.fixture
def users_page(logged_in_pages):
    return logged_in_pages.users


@pytest.fixture
def labels_page(logged_in_pages):
    return logged_in_pages.labels


@pytest.fixture
def statuses_page(logged_in_pages):
    return logged_in_pages.statuses


@pytest.fixture
def tasks_page(logged_in_pages):
    return logged_in_pages.tasks
