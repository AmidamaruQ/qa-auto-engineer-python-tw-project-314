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


def test_view_users_list(logged_app):
    user_data = build_user_data()

    create_user(logged_app, user_data)

    headers = logged_app.users_page.get_table_headers()

    assert "Email" in headers
    assert "First name" in headers
    assert "Last name" in headers
    assert logged_app.users_page.get_users_count() > 0
    assert_user_presence(logged_app, user_data)


def test_edit_user_form_prefilled(logged_app):
    user_data = build_user_data()

    create_user(logged_app, user_data)
    logged_app.users_page.open_user_from_table(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"],
    )

    assert logged_app.user_form_page.email_value == user_data["email"]
    assert logged_app.user_form_page.first_name_value == user_data["first_name"]
    assert logged_app.user_form_page.last_name_value == user_data["second_name"]

    logged_app.user_form_page.update_user_info(email="invalid-email")
    open_users_page(logged_app)
    assert_user_presence(logged_app, user_data)
    logged_app.users_page.open_user_from_table(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"],
    )

    logged_app.user_form_page.update_user_info(first_name="renamed_user")
    assert logged_app.user_form_page.popup.wait_popup_with_text(POPUP_UPDATED)

    open_users_page(logged_app)
    assert "renamed_user" in logged_app.users_page.get_user_row_text(
        user_data["email"]
    )


def test_delete_user_form(logged_app):
    user_data = build_user_data()

    create_user(logged_app, user_data)
    logged_app.users_page.open_user_from_table(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"],
    )
    logged_app.user_form_page.delete_user()

    assert logged_app.user_form_page.popup.wait_popup_with_text(POPUP_DELETED)
    open_users_page(logged_app)
    assert_user_presence(logged_app, user_data, is_present=False)


def test_delete_all_users(logged_app):
    open_users_page(logged_app)
    initial_count = logged_app.users_page.get_users_count()

    assert initial_count > 0

    logged_app.users_page.choose_all_users()
    logged_app.users_page.delete_chosen_user()
    assert logged_app.users_page.popup.wait_popup_with_text(
        POPUP_BULK_DELETED_TEMPLATE.format(count=initial_count)
    )
    assert logged_app.users_page.get_users_count() == 0
