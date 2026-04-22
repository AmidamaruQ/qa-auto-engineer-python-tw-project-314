def test_create_user(logged_app):
    test_data = {
        "email": "email@mail.ru",
        "first_name": "first_name",
        "second_name": "second_name",
    }
    logged_app.base_page.sidebar.open_users_page()
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )


def test_update_useer(logged_app):
    user_data = {
        "email": "email@mail.com",
        "first_name": "first_name",
        "second_name": "second_name",
    }
    new_user_email = "new_email@mail.com"
    logged_app.base_page.sidebar.open_users_page()
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"]
    )
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created"
    )
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"]
    )
    logged_app.users_page.open_user_from_table(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"])
    logged_app.user_form_page.update_user_info(new_user_email)

    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        new_user_email,
        user_data["first_name"],
        user_data["second_name"]
    )


def test_delete_user(logged_app):
    test_data = {
        "email": "email@mail.ru",
        "first_name": "first_name",
        "second_name": "second_name",
    }
    logged_app.base_page.sidebar.open_users_page()
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    logged_app.users_page.open_user_from_table(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    logged_app.user_form_page.delete_user()
    logged_app.user_form_page.sidebar.open_users_page()
    assert not logged_app.users_page.is_user_present(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )


def test_multiple_delete_user(logged_app):
    first_user_data = {
        "email": "email1@mail.com",
        "first_name": "first_name1",
        "second_name": "second_name1"
    }
    second_user_data = {
        "email": "email2@mail.com",
        "first_name": "first_name2",
        "second_name": "second_name2"
    }
    logged_app.base_page.sidebar.open_users_page()
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        first_user_data["email"],
        first_user_data["first_name"],
        first_user_data["second_name"]
    )
    assert logged_app.users_page.popup.wait_popup_with_text("Element created")
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        first_user_data["email"],
        first_user_data["first_name"],
        first_user_data["second_name"]
    )
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        second_user_data["email"],
        second_user_data["first_name"],
        second_user_data["second_name"]
    )
    assert logged_app.users_page.popup.wait_popup_with_text("Element created")
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        second_user_data["email"],
        second_user_data["first_name"],
        second_user_data["second_name"]
    )
    logged_app.users_page.choose_user_in_table(
        first_user_data["email"],
        first_user_data["first_name"],
        first_user_data["second_name"]
    )
    logged_app.users_page.choose_user_in_table(
        second_user_data["email"],
        second_user_data["first_name"],
        second_user_data["second_name"]
    )
    logged_app.users_page.delete_chosen_user()
    assert logged_app.users_page.popup.wait_popup_with_text(
        "2 elements deleted"
    )
    assert not logged_app.users_page.is_user_present(
        first_user_data["email"],
        first_user_data["first_name"],
        first_user_data["second_name"]
    )
    assert not logged_app.users_page.is_user_present(
        second_user_data["email"],
        second_user_data["first_name"],
        second_user_data["second_name"]
    )
