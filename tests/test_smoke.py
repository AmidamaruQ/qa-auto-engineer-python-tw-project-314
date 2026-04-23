import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_login_page_elements(app):
    assert app.login_page.username_input.is_displayed()
    assert app.login_page.password_input.is_displayed()
    assert app.login_page.submit_button.is_displayed()


@pytest.mark.step_3
def test_login_form_validation(app):
    app.login_page.click_submit()

    assert app.login_page.driver.find_element(
        By.NAME,
        "username",
    ).get_attribute("aria-invalid") == "true"
    assert app.login_page.driver.find_element(
        By.NAME,
        "password",
    ).get_attribute("aria-invalid") == "true"
    assert app.login_page.submit_button.is_displayed()


@pytest.mark.step_3
def test_login(logged_app, expected_profile_name):
    assert logged_app.dashboard_page.header.header_title.is_displayed()
    assert (
        logged_app.dashboard_page.header.header_title.text
        == "Welcome to the administration"
    )
    assert logged_app.dashboard_page.header.profile_button.text == (
        expected_profile_name
    )


@pytest.mark.step_3
def test_logout(logged_app):
    logged_app.dashboard_page.header.logout()

    assert logged_app.login_page.username_input.is_displayed()
    assert logged_app.login_page.password_input.is_displayed()
