from tests.support import (
    POPUP_CREATED,
    POPUP_DELETED,
    POPUP_UPDATED,
    build_task_data,
)
from utils.utils import wait_for


def open_tasks_page(app):
    app.base_page.sidebar.open_tasks_page()


def create_task(app, task_data):
    open_tasks_page(app)
    app.tasks_page.open_create_task()
    app.task_form_page.create_task(
        assignee=task_data["assignee"],
        title=task_data["title"],
        content=task_data["content"],
        status=task_data["status"],
        label=task_data["label"],
    )
    assert app.task_form_page.popup.wait_popup_with_text(POPUP_CREATED)
    open_tasks_page(app)


def assert_task_presence(app, task_data, is_present=True):
    assert app.tasks_page.is_task_present(
        task_data["status"],
        task_data["title"],
        task_data["content"],
    ) is is_present


def test_create_task(logged_app):
    task_data = build_task_data()

    create_task(logged_app, task_data)

    assert_task_presence(logged_app, task_data)


def test_task_assignee_filter(logged_app):
    first_task = build_task_data()
    second_task = {
        **build_task_data(),
        "assignee": "john@google.com",
    }

    create_task(logged_app, first_task)
    create_task(logged_app, second_task)

    open_tasks_page(logged_app)
    logged_app.tasks_page.choose_assignee(second_task["assignee"])

    assert wait_for(lambda: logged_app.tasks_page.is_task_present(
        second_task["status"],
        second_task["title"],
        second_task["content"],
    ))
    assert wait_for(
        lambda: not logged_app.tasks_page.is_task_present(
            first_task["status"],
            first_task["title"],
            first_task["content"],
        )
    )


def test_task_status_filter(logged_app):
    first_task = build_task_data()
    second_task = {
        **build_task_data(),
        "status": "To Review",
    }

    create_task(logged_app, first_task)
    create_task(logged_app, second_task)

    open_tasks_page(logged_app)
    logged_app.tasks_page.choose_status(second_task["status"])

    assert wait_for(lambda: logged_app.tasks_page.is_task_present(
        second_task["status"],
        second_task["title"],
        second_task["content"],
    ))
    assert wait_for(
        lambda: not logged_app.tasks_page.is_task_present(
            first_task["status"],
            first_task["title"],
            first_task["content"],
        )
    )


def test_task_label_filter(logged_app):
    first_task = build_task_data()
    second_task = {
        **build_task_data(),
        "label": "bug",
    }

    create_task(logged_app, first_task)
    create_task(logged_app, second_task)

    open_tasks_page(logged_app)
    logged_app.tasks_page.choose_label(second_task["label"])

    assert wait_for(lambda: logged_app.tasks_page.is_task_present(
        second_task["status"],
        second_task["title"],
        second_task["content"],
    ))
    assert wait_for(
        lambda: not logged_app.tasks_page.is_task_present(
            first_task["status"],
            first_task["title"],
            first_task["content"],
        )
    )


def test_update_task(logged_app):
    task_data = build_task_data()
    updated_task_data = {
        **task_data,
        "title": build_task_data()["title"],
    }

    create_task(logged_app, task_data)
    assert_task_presence(logged_app, task_data)

    logged_app.tasks_page.open_edit_task(
        status=task_data["status"],
        title=task_data["title"],
        content=task_data["content"],
    )
    logged_app.task_form_page.update_task(title=updated_task_data["title"])

    assert logged_app.task_form_page.popup.wait_popup_with_text(POPUP_UPDATED)
    open_tasks_page(logged_app)
    assert_task_presence(logged_app, updated_task_data)
    assert_task_presence(logged_app, task_data, is_present=False)


def test_delete_task(logged_app):
    task_data = build_task_data()

    create_task(logged_app, task_data)
    assert_task_presence(logged_app, task_data)

    logged_app.tasks_page.open_edit_task(
        status=task_data["status"],
        title=task_data["title"],
        content=task_data["content"],
    )
    logged_app.task_form_page.delete_task()

    assert logged_app.task_form_page.popup.wait_popup_with_text(POPUP_DELETED)
    open_tasks_page(logged_app)
    assert_task_presence(logged_app, task_data, is_present=False)
