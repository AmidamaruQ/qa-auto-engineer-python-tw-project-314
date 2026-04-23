import pytest
from selenium.webdriver.common.by import By

from tests.support import (
    POPUP_CREATED,
    POPUP_DELETED,
    POPUP_UPDATED,
    build_label_name,
    build_status_data,
    build_task_data,
    build_user_data,
)
from tests.test_labels import create_label
from tests.test_statuses_page import create_status
from tests.test_users import create_user
from utils import xpath_literal
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
    assert app.tasks_page.is_task_present_by_title(task_data["title"])


def create_task_dependencies(app):
    user_data = build_user_data()
    primary_status = build_status_data()
    secondary_status = build_status_data()
    label_name = build_label_name()

    create_user(app, user_data)
    create_status(app, primary_status)
    create_status(app, secondary_status)
    create_label(app, label_name)

    return {
        "assignee": user_data["email"],
        "status": primary_status["name"],
        "alt_status": secondary_status["name"],
        "label": label_name,
    }


def build_task_with_dependencies(app):
    dependencies = create_task_dependencies(app)
    return {
        **build_task_data(),
        "assignee": dependencies["assignee"],
        "status": dependencies["status"],
        "alt_status": dependencies["alt_status"],
        "label": dependencies["label"],
    }


def assert_page_has_text(app, text):
    locator = (By.XPATH, f"//*[normalize-space()={xpath_literal(text)}]")
    assert app.tasks_page.label(locator).is_displayed()


@pytest.mark.step_7_createTasks
def test_create_task(logged_app):
    task_data = build_task_with_dependencies(logged_app)

    create_task(logged_app, task_data)


@pytest.mark.step_7_viewBoard
def test_view_task_details(logged_app):
    task_data = build_task_with_dependencies(logged_app)

    create_task(logged_app, task_data)
    logged_app.tasks_page.open_task_details(task_data["title"])

    assert_page_has_text(logged_app, task_data["title"])
    assert_page_has_text(logged_app, task_data["content"])
    assert_page_has_text(logged_app, task_data["assignee"])


@pytest.mark.step_7_editTasks
def test_edit_task(logged_app):
    task_data = build_task_with_dependencies(logged_app)
    updated_title = f"updated_{task_data['title']}"

    create_task(logged_app, task_data)
    logged_app.tasks_page.open_edit_task_by_title(task_data["title"])
    logged_app.task_form_page.update_task(title=updated_title)

    assert logged_app.task_form_page.popup.wait_popup_with_text(POPUP_UPDATED)
    open_tasks_page(logged_app)
    assert wait_for(
        lambda: logged_app.tasks_page.is_task_present_by_title(
            task_data["title"],
        ),
        False,
    ) is False
    assert logged_app.tasks_page.is_task_present_by_title(updated_title)


@pytest.mark.step_7_dragAndDropTasks
def test_change_task_status(logged_app):
    task_data = build_task_with_dependencies(logged_app)

    create_task(logged_app, task_data)
    logged_app.tasks_page.open_edit_task_by_title(task_data["title"])
    logged_app.task_form_page.update_task(status=task_data["alt_status"])

    assert logged_app.task_form_page.popup.wait_popup_with_text(POPUP_UPDATED)
    open_tasks_page(logged_app)
    assert logged_app.tasks_page.is_task_in_status(
        task_data["title"],
        task_data["alt_status"],
    )


@pytest.mark.step_7_deleteTasks
def test_delete_task(logged_app):
    task_data = build_task_with_dependencies(logged_app)

    create_task(logged_app, task_data)
    logged_app.tasks_page.open_edit_task_by_title(task_data["title"])
    logged_app.task_form_page.delete_task()

    assert logged_app.task_form_page.popup.wait_popup_with_text(POPUP_DELETED)
    open_tasks_page(logged_app)
    assert wait_for(
        lambda: logged_app.tasks_page.is_task_present_by_title(
            task_data["title"],
        ),
        False,
    ) is False
