from tests.support import (
    POPUP_BULK_DELETED_TEMPLATE,
    POPUP_CREATED,
    POPUP_DELETED,
    POPUP_UPDATED,
    build_user_data,
)


def open_users_page(app):
    app.base_page.sidebar.open_users_page()


def create_user(app, user_data):
    open_users_page(app)
    app.users_page.open_create_user_form()
    app.user_form_page.create_user(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"],
    )
    assert app.user_form_page.popup.wait_popup_with_text(POPUP_CREATED)
    open_users_page(app)


def assert_user_presence(app, user_data, is_present=True):
    assert app.users_page.is_user_present(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"],
    ) is is_present


def test_create_user(logged_app):
    user_data = build_user_data()

    create_user(logged_app, user_data)

    assert_user_presence(logged_app, user_data)


def test_update_user(logged_app):
    user_data = build_user_data()
    updated_user_data = {
        **user_data,
        "email": build_user_data()["email"],
    }

    create_user(logged_app, user_data)
    assert_user_presence(logged_app, user_data)

    logged_app.users_page.open_user_from_table(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"],
    )
    logged_app.user_form_page.update_user_info(email=updated_user_data["email"])
    assert logged_app.user_form_page.popup.wait_popup_with_text(POPUP_UPDATED)

    open_users_page(logged_app)
    assert_user_presence(logged_app, updated_user_data)
    assert_user_presence(logged_app, user_data, is_present=False)


def test_delete_user(logged_app):
    user_data = build_user_data()

    create_user(logged_app, user_data)
    assert_user_presence(logged_app, user_data)

    logged_app.users_page.open_user_from_table(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"],
    )
    logged_app.user_form_page.delete_user()
    assert logged_app.user_form_page.popup.wait_popup_with_text(POPUP_DELETED)

    open_users_page(logged_app)
    assert_user_presence(logged_app, user_data, is_present=False)


def test_multiple_delete_user(logged_app):
    first_user_data = build_user_data()
    second_user_data = build_user_data()

    create_user(logged_app, first_user_data)
    create_user(logged_app, second_user_data)
    assert_user_presence(logged_app, first_user_data)
    assert_user_presence(logged_app, second_user_data)

    logged_app.users_page.choose_user_in_table(
        first_user_data["email"],
        first_user_data["first_name"],
        first_user_data["second_name"],
    )
    logged_app.users_page.choose_user_in_table(
        second_user_data["email"],
        second_user_data["first_name"],
        second_user_data["second_name"],
    )
    logged_app.users_page.delete_chosen_user()
    assert logged_app.users_page.popup.wait_popup_with_text(
        POPUP_BULK_DELETED_TEMPLATE.format(count=2)
    )

    assert_user_presence(logged_app, first_user_data, is_present=False)
    assert_user_presence(logged_app, second_user_data, is_present=False)
