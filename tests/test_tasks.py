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


# def test_view_task_list(logged_app):
#     task_data = {
#         **build_task_data(),
#         "assignee": "john@google.com",
#         "status": "Draft",
#     }
#
#     create_task(logged_app, task_data)
#     open_tasks_page(logged_app)
#
#     columns = logged_app.tasks_page.get_board_columns()
#     assert len(columns) > 0
#     assert "Draft" in columns
#
#     logged_app.tasks_page.choose_assignee(task_data["assignee"])
#     logged_app.tasks_page.choose_status(task_data["status"])
#
#     assert wait_for(lambda: logged_app.tasks_page.is_task_present(
#         task_data["status"],
#         task_data["title"],
#         task_data["content"],
#     ))
#
#
# def test_edit_task_form_prefilled(logged_app):
#     task_data = build_task_data()
#     updated_task_data = {
#         **task_data,
#         "title": build_task_data()["title"],
#         "status": "To Review",
#     }
#
#     create_task(logged_app, task_data)
#     logged_app.tasks_page.open_edit_task(
#         status=task_data["status"],
#         title=task_data["title"],
#         content=task_data["content"],
#     )
#     logged_app.task_form_page.update_task(
#         title=updated_task_data["title"],
#         status=updated_task_data["status"],
#     )
#
#     assert logged_app.task_form_page.popup.wait_popup_with_text(POPUP_UPDATED)
#     open_tasks_page(logged_app)
#     assert_task_presence(logged_app, task_data, is_present=False)
#     assert wait_for(
#         lambda: updated_task_data["title"] in
#         logged_app.tasks_page.get_task_text(
#             status=updated_task_data["status"],
#             content=updated_task_data["content"],
#         )
#     )
#
#
# def test_delete_task_form(logged_app):
#     task_data = build_task_data()
#
#     create_task(logged_app, task_data)
#     logged_app.tasks_page.open_edit_task(
#         status=task_data["status"],
#         title=task_data["title"],
#         content=task_data["content"],
#     )
#     logged_app.task_form_page.delete_task()
#
#     assert logged_app.task_form_page.popup.wait_popup_with_text(POPUP_DELETED)
#     open_tasks_page(logged_app)
#     assert_task_presence(logged_app, task_data, is_present=False)
