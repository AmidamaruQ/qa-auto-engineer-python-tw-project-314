from utils.utils import wait_for


def test_create_task(logged_app):
    task_data = {
        "assignee": "emily@example.com",
        "title": "title",
        "content": "test_content",
        "status": "Draft",
        "label": "critical"
    }
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
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 task_data["title"],
                                                 task_data["content"])


def test_task_assignee_filter(logged_app):
    title = "Task"
    content = "Description"
    mail = "john@google.com"

    logged_app.base_page.sidebar.open_tasks_page()
    default_count = logged_app.tasks_page.get_tasks_count("", title, content)
    logged_app.tasks_page.choose_assignee(mail)
    assert wait_for(lambda: logged_app.tasks_page.get_tasks_count(
        "", title, content) < default_count)


def test_task_status_filter(logged_app):
    title = "Task"
    content = "Description"
    status = "Draft"

    logged_app.base_page.sidebar.open_tasks_page()
    default_count = logged_app.tasks_page.get_tasks_count("", title, content)
    logged_app.tasks_page.choose_status(status)
    assert wait_for(lambda: logged_app.tasks_page.get_tasks_count(
        "", title, content) < default_count)


def test_task_label_filter(logged_app):
    title = "Task"
    content = "Description"
    label = "critical"

    logged_app.base_page.sidebar.open_tasks_page()
    default_count = logged_app.tasks_page.get_tasks_count("", title, content)
    logged_app.tasks_page.choose_label(label)
    assert wait_for(lambda: logged_app.tasks_page.get_tasks_count(
        "", title, content) < default_count)


def test_update_task(logged_app):
    task_data = {
        "assignee": "emily@example.com",
        "title": "title",
        "content": "test_content",
        "status": "Draft",
        "label": "critical"
    }
    updated_title = "new_title"
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
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 task_data["title"],
                                                 task_data["content"])
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
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 updated_title,
                                                 task_data["content"])


def test_delete_task(logged_app):
    task_data = {
        "assignee": "emily@example.com",
        "title": "title",
        "content": "test_content",
        "status": "Draft",
        "label": "critical"
    }
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
    logged_app.task_form_page.sidebar.open_tasks_page()
    assert logged_app.tasks_page.is_task_present(task_data["status"],
                                                 task_data["title"],
                                                 task_data["content"])
    logged_app.tasks_page.open_edit_task(
        status=task_data["status"],
        title=task_data["title"],
        content=task_data["content"],
    )
    logged_app.task_form_page.delete_task()
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element deleted")
    assert not logged_app.tasks_page.is_task_present(task_data["status"],
                                                     task_data["title"],
                                                     task_data["content"])
