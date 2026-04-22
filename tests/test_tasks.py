from utils.utils import wait_for


def test_create_task(logged_app):
    # Arrange: prepare task data.
    task_data = {
        "assignee": "emily@example.com",
        "title": "title",
        "content": "test_content",
        "status": "Draft",
        "label": "critical"
    }
    # Act: open the task form and create a task.
    logged_app.base_page.sidebar.open_tasks_page()
    logged_app.tasks_page.open_create_task()
    logged_app.task_form_page.create_task(
        assignee=task_data["assignee"],
        title=task_data["title"],
        content=task_data["content"],
        status=task_data["status"],
        label=task_data["label"]
    )
    # Assert: verify the creation popup is shown.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    # Assert: verify the created task is visible in the table.
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 task_data["title"],
                                                 task_data["content"])


def test_task_assignee_filter(logged_app):
    # Arrange: prepare filter parameters.
    title = "Task"
    content = "Description"
    mail = "john@google.com"

    # Act: open the tasks page and capture the baseline count.
    logged_app.base_page.sidebar.open_tasks_page()
    default_count = logged_app.tasks_page.get_tasks_count("", title, content)
    # Act and assert: apply the assignee filter and verify the result count changes.
    logged_app.tasks_page.choose_assignee(mail)
    assert wait_for(lambda: logged_app.tasks_page.get_tasks_count(
        "", title, content) < default_count)


def test_task_status_filter(logged_app):
    # Arrange: prepare filter parameters.
    title = "Task"
    content = "Description"
    status = "Draft"

    # Act: open the tasks page and capture the baseline count.
    logged_app.base_page.sidebar.open_tasks_page()
    default_count = logged_app.tasks_page.get_tasks_count("", title, content)
    # Act and assert: apply the status filter and verify the result count changes.
    logged_app.tasks_page.choose_status(status)
    assert wait_for(lambda: logged_app.tasks_page.get_tasks_count(
        "", title, content) < default_count)


def test_task_label_filter(logged_app):
    # Arrange: prepare filter parameters.
    title = "Task"
    content = "Description"
    label = "critical"

    # Act: open the tasks page and capture the baseline count.
    logged_app.base_page.sidebar.open_tasks_page()
    default_count = logged_app.tasks_page.get_tasks_count("", title, content)
    # Act and assert: apply the label filter and verify the result count changes.
    logged_app.tasks_page.choose_label(label)
    assert wait_for(lambda: logged_app.tasks_page.get_tasks_count(
        "", title, content) < default_count)


def test_update_task(logged_app):
    # Arrange: prepare source and updated task data.
    task_data = {
        "assignee": "emily@example.com",
        "title": "title",
        "content": "test_content",
        "status": "Draft",
        "label": "critical"
    }
    updated_title = "new_title"
    # Act: create the initial task.
    logged_app.base_page.sidebar.open_tasks_page()
    logged_app.tasks_page.open_create_task()
    logged_app.task_form_page.create_task(
        assignee=task_data["assignee"],
        title=task_data["title"],
        content=task_data["content"],
        status=task_data["status"],
        label=task_data["label"]
    )
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    # Assert: verify the original task is present before editing.
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 task_data["title"],
                                                 task_data["content"])
    # Act: open the task and update its title.
    logged_app.tasks_page.open_edit_task(
        status=task_data["status"],
        title=task_data["title"],
        content=task_data["content"],
    )
    logged_app.task_form_page.update_task(
        title=updated_title
    )
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element updated")
    # Assert: verify the updated task is visible in the table.
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 updated_title,
                                                 task_data["content"])


def test_delete_task(logged_app):
    # Arrange: prepare task data.
    task_data = {
        "assignee": "emily@example.com",
        "title": "title",
        "content": "test_content",
        "status": "Draft",
        "label": "critical"
    }
    # Act: create the task that will be deleted.
    logged_app.base_page.sidebar.open_tasks_page()
    logged_app.tasks_page.open_create_task()
    logged_app.task_form_page.create_task(
        assignee=task_data["assignee"],
        title=task_data["title"],
        content=task_data["content"],
        status=task_data["status"],
        label=task_data["label"]
    )
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    # Assert: verify the task exists before deletion.
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 task_data["title"],
                                                 task_data["content"])
    # Act: open the task and delete it.
    logged_app.tasks_page.open_edit_task(
        status=task_data["status"],
        title=task_data["title"],
        content=task_data["content"],
    )
    logged_app.task_form_page.delete_task()
    # Assert: verify the task is removed from the table.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element deleted")
    assert not logged_app.tasks_page.is_task_present(task_data["status"],
                                                     task_data["title"],
                                                     task_data["content"])
