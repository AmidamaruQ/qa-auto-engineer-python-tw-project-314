def test_login_success(app, credentials):
    app.login_page.login(credentials["username"], credentials["password"])

    assert app.dashboard_page.header.header_title.is_displayed()


def test_login_success_header(app, credentials):
    app.login_page.login(credentials["username"], credentials["password"])

    assert (
        app.dashboard_page.header.header_title.text
        == "Welcome to the administration"
    )


def test_login_fail_empty_fields(app):
    app.login_page.login("", "")

    assert app.login_page.username_input.is_displayed()
    assert app.login_page.is_login_page


def test_logout_redirect_to_login(logged_app):
    logged_app.dashboard_page.header.logout()

    assert logged_app.login_page.username_input.is_displayed()
    assert logged_app.login_page.is_login_page
