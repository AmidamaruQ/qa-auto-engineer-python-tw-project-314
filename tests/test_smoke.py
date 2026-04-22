def test_login(app, credentials, expected_profile_name):
    app.login_page.login(credentials["username"], credentials["password"])

    assert app.dashboard_page.header.header_title.is_displayed()
    assert (
        app.dashboard_page.header.header_title.text
        == "Welcome to the administration"
    )
    assert (
        app.dashboard_page.header.profile_button.text
        == expected_profile_name
    )


def test_logout(logged_app):
    logged_app.dashboard_page.header.logout()

    assert logged_app.login_page.username_input.is_displayed()
    assert logged_app.login_page.is_login_page


def test_login_empty_credentials(app):
    app.login_page.login("", "")

    assert app.login_page.username_input.is_displayed()
    assert app.login_page.is_login_page
