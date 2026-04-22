import pytest


def test_login(app, env):
    app.login_page.login(env["LOGIN"], env["PASSWORD"])
    assert app.dashboard_page.header.header_title.is_displayed()
    assert (app.dashboard_page.header.header_title.text ==
            "Welcome to the administration")
    assert app.dashboard_page.header.profile_button.text == "Jane Doe"


@pytest.mark.xfail
def test_logout(logged_app):
    logged_app.dashboard_page.header.logout()
    assert logged_app.login_page.username_input.is_displayed()
