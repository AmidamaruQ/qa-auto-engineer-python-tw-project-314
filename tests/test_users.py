import pytest


def test_create_user(logged_app):
    # Arrange: prepare user data.
    test_data = {
        "email": "email@mail.ru",
        "first_name": "first_name",
        "second_name": "second_name",
    }
    # Act: open the users page and create a new user.
    logged_app.base_page.sidebar.open_users_page()
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    # Assert: verify the creation popup is shown.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    # Assert: verify the created user is present in the table.
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )

@pytest.mark.xfail
def test_update_user(logged_app):
    # Arrange: prepare source and updated user data.
    user_data = {
        "email": "email@mail.com",
        "first_name": "first_name",
        "second_name": "second_name",
    }
    new_user_email = "new_email@mail.com"
    # Act: create the initial user.
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
    # Assert: verify the original user is present before editing.
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"]
    )
    # Act: open the user and update its email.
    logged_app.users_page.open_user_from_table(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"])
    logged_app.user_form_page.update_user_info(new_user_email)
    # Assert: verify the updated user is present in the table.
    logged_app.user_form_page.sidebar.open_users_page()
    assert not logged_app.users_page.is_user_present(
        user_data["email"],
        user_data["first_name"],
        user_data["second_name"]
    )
    assert logged_app.users_page.is_user_present(
        new_user_email,
        user_data["first_name"],
        user_data["second_name"]
    )


def test_delete_user(logged_app):
    # Arrange: prepare user data.
    test_data = {
        "email": "email@mail.ru",
        "first_name": "first_name",
        "second_name": "second_name",
    }
    # Act: create a user that will be deleted.
    logged_app.base_page.sidebar.open_users_page()
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    # Assert: verify the user exists before deletion.
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    # Act: open the user and delete it.
    logged_app.users_page.open_user_from_table(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )
    logged_app.user_form_page.delete_user()
    # Assert: verify the user is removed from the table.
    logged_app.user_form_page.sidebar.open_users_page()
    assert not logged_app.users_page.is_user_present(
        test_data["email"],
        test_data["first_name"],
        test_data["second_name"]
    )


def test_multiple_delete_user(logged_app):
    # Arrange: prepare data for two users.
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
    # Act: create the first user.
    logged_app.base_page.sidebar.open_users_page()
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        first_user_data["email"],
        first_user_data["first_name"],
        first_user_data["second_name"]
    )
    assert logged_app.users_page.popup.wait_popup_with_text("Element created")
    # Assert: verify the first user is present.
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        first_user_data["email"],
        first_user_data["first_name"],
        first_user_data["second_name"]
    )
    # Act: create the second user.
    logged_app.users_page.open_create_user_form()
    logged_app.user_form_page.create_user(
        second_user_data["email"],
        second_user_data["first_name"],
        second_user_data["second_name"]
    )
    assert logged_app.users_page.popup.wait_popup_with_text("Element created")
    # Assert: verify the second user is present.
    logged_app.user_form_page.sidebar.open_users_page()
    assert logged_app.users_page.is_user_present(
        second_user_data["email"],
        second_user_data["first_name"],
        second_user_data["second_name"]
    )
    # Act: select both users and delete them in bulk.
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
    # Assert: verify both users are removed from the table.
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
