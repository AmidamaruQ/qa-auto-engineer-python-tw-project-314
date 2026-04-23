def build_hash_url(base_url: str, fragment: str) -> str:
    clean_base_url = base_url.rstrip("/")
    clean_fragment = fragment.lstrip("/#")
    return f"{clean_base_url}/#/{clean_fragment}"


def test_login_page_elements(driver, base_url, login_page):
    driver.get(base_url)

    assert login_page.is_username_input_visible()
    assert login_page.is_password_input_visible()
    assert login_page.is_login_button_visible()
    assert not login_page.is_profile_button_visible()


def test_login_form_validation(driver, base_url, login_page):
    driver.get(base_url)

    login_page.click_submit()

    assert login_page.get_input_aria_invalid("username") == "true"
    assert login_page.get_input_aria_invalid("password") == "true"
    assert login_page.is_login_button_visible()


def test_successful_login_and_logout(driver, base_url, logged_in_pages):
    assert logged_in_pages.login.is_logged_in()
    assert (
        driver.current_url.endswith("#/")
        or driver.current_url == base_url
    )

    driver.get(build_hash_url(base_url, "tasks"))

    assert logged_in_pages.tasks.verify_filters_visible()

    logged_in_pages.login.logout()

    assert logged_in_pages.login.is_logged_out()

    for protected_route in ("tasks", "users"):
        driver.get(build_hash_url(base_url, protected_route))
        assert logged_in_pages.login.is_logged_out()
