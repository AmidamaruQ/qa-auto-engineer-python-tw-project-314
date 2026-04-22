def test_create_status(logged_app):
    # Arrange: prepare task status data.
    task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    # Act: open the status form and create a task status.
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        task_status_data["name"],
        task_status_data["slug"])
    # Assert: verify the creation popup is shown.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")
    # Assert: verify the created task status is present in the table.
    logged_app.task_statuses_form_page.sidebar.open_task_statuses_page()
    assert logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])


def test_update_status(logged_app):
    # Arrange: prepare source and updated task status data.
    task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    updated_slug = "updated_slug"

    # Act: create the initial task status.
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        task_status_data["name"],
        task_status_data["slug"])
    # Assert: verify the original task status is present before editing.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.task_statuses_form_page.sidebar.open_task_statuses_page()
    assert logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])
    # Act: open the task status and update its slug.
    logged_app.task_statuses_page.open_task_from_row(task_status_data["name"],
                                                     task_status_data["slug"])
    logged_app.task_statuses_form_page.update_task_status_info(
        task_status_data["name"], updated_slug)
    # Assert: verify the updated task status is present in the table.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element updated")
    logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], updated_slug)


def test_delete_task_status(logged_app):
    # Arrange: prepare task status data.
    task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    # Act: create the task status that will be deleted.
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        task_status_data["name"],
        task_status_data["slug"])
    # Assert: verify the task status exists before deletion.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.task_statuses_form_page.sidebar.open_task_statuses_page()
    assert logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])
    # Act: open the task status and delete it.
    logged_app.task_statuses_page.open_task_from_row(task_status_data["name"],
                                                     task_status_data["slug"])

    logged_app.task_statuses_form_page.delete_task_status()
    # Assert: verify the task status is removed from the table.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element deleted")
    assert not logged_app.task_statuses_page.is_task_status_present(
        task_status_data["name"], task_status_data["slug"])


def test_multiple_delete_task_status(logged_app):
    # Arrange: prepare data for two task statuses.
    first_task_status_data = {
        "name": "name",
        "slug": "slug"
    }
    second_task_status_data = {
        "name": "name2",
        "slug": "slug2"
    }
    # Act: create the first task status.
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        first_task_status_data["name"],
        first_task_status_data["slug"])
    # Assert: verify the first task status creation succeeds.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")

    # Act: create the second task status.
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.open_create_task()
    logged_app.task_statuses_form_page.create_task_status(
        second_task_status_data["name"],
        second_task_status_data["slug"])
    # Assert: verify the second task status creation succeeds.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "Element created")

    # Act: select both task statuses and delete them in bulk.
    logged_app.base_page.sidebar.open_task_statuses_page()
    logged_app.task_statuses_page.choose_task_from_row(
        first_task_status_data["name"], first_task_status_data["slug"])
    logged_app.task_statuses_page.choose_task_from_row(
        second_task_status_data["name"], second_task_status_data["slug"])
    logged_app.task_statuses_page.delete_chosen_task()
    # Assert: verify both task statuses are removed from the table.
    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        "2 elements deleted")

    assert not logged_app.task_statuses_page.is_task_status_present(
        first_task_status_data["name"], first_task_status_data["slug"])
    assert not logged_app.task_statuses_page.is_task_status_present(
        second_task_status_data["name"], second_task_status_data["slug"])
