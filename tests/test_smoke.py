import pytest


def test_login(app, env):
    # Act: log in with configured credentials.
    app.login_page.login(env["LOGIN"], env["PASSWORD"])
    # Assert: verify the dashboard is opened for the user.
    assert app.dashboard_page.header.header_title.is_displayed()
    assert (app.dashboard_page.header.header_title.text ==
            "Welcome to the administration")
    assert app.dashboard_page.header.profile_button.text == "Jane Doe"


@pytest.mark.xfail
def test_logout(logged_app):
    # Act: log out from the application.
    logged_app.dashboard_page.header.logout()
    # Assert: verify the login form is shown again.
    assert logged_app.login_page.username_input.is_displayed()
