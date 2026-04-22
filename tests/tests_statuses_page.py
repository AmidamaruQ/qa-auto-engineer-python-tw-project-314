def test_create_status(logged_app):
    task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        task_status_data["name"],
        task_status_data["slug"])
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.task_statuses_form_page.sidebar.open_task_statuses_page()
    assert logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])


def test_update_status(logged_app):
    task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    updated_slug = "updated_slug"

    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        task_status_data["name"],
        task_status_data["slug"])
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.task_statuses_form_page.sidebar.open_task_statuses_page()
    assert logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])
    logged_app.task_statuses_page.open_task_from_row(task_status_data["name"],
                                                     task_status_data["slug"])
    logged_app.task_statuses_form_page.update_task_status_info(
        task_status_data["name"], updated_slug)
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element updated")
    logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], updated_slug)


def test_delete_task_status(logged_app):
    task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        task_status_data["name"],
        task_status_data["slug"])
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.task_statuses_form_page.sidebar.open_task_statuses_page()
    assert logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])
    logged_app.task_statuses_page.open_task_from_row(task_status_data["name"],
                                                     task_status_data["slug"])

    logged_app.task_statuses_form_page.delete_task_status()
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element deleted")
    assert not logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])


def test_multiple_delete_task_status(logged_app):
    first_task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    second_task_status_data = {
        "name": "name2",
        "slug": "slug2"
    }
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        first_task_status_data["name"],
        first_task_status_data["slug"])
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")

    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        second_task_status_data["name"],
        second_task_status_data["slug"])
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")

    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.choose_task_from_row(
        first_task_status_data["name"], first_task_status_data["slug"])
    logged_app.task_statuses_page.choose_task_from_row(
        second_task_status_data["name"], second_task_status_data["slug"])
    logged_app.task_statuses_page.delete_chosen_task()
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "2 elements deleted")

    assert not logged_app.task_statuses_page.is_task_status_present(
        first_task_status_data["name"], first_task_status_data["slug"])
    assert not logged_app.task_statuses_page.is_task_status_present(
        second_task_status_data["name"], second_task_status_data["slug"])
