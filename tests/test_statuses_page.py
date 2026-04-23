import pytest

from tests.support import (
    POPUP_BULK_DELETED_TEMPLATE,
    POPUP_CREATED,
    POPUP_DELETED,
    POPUP_UPDATED,
    build_status_data,
)
from utils.utils import wait_for


def open_statuses_page(app):
    app.base_page.sidebar.open_task_statuses_page()


def create_status(app, status_data):
    open_statuses_page(app)
    app.task_statuses_page.open_create_status()
    app.task_statuses_form_page.create_task_status(
        status_data["name"],
        status_data["slug"],
    )
    assert app.task_statuses_form_page.popup.wait_popup_with_text(POPUP_CREATED)
    open_statuses_page(app)
    assert app.task_statuses_page.is_task_status_present(
        status_data["name"],
        status_data["slug"],
    )


@pytest.mark.step_5_createStatus
def test_create_status(logged_app):
    status_data = build_status_data()

    create_status(logged_app, status_data)


@pytest.mark.step_5_viewList
def test_view_status_list(logged_app):
    status_data = build_status_data()

    create_status(logged_app, status_data)
    headers = logged_app.task_statuses_page.get_table_headers()

    assert "Name" in headers
    assert "Slug" in headers
    assert logged_app.task_statuses_page.get_statuses_count() > 0
    row_text = logged_app.task_statuses_page.get_status_row_text(
        status_data["name"],
    )
    assert status_data["slug"] in row_text


@pytest.mark.step_5_editStatus
def test_edit_status(logged_app):
    status_data = build_status_data()
    updated_status_data = build_status_data()

    create_status(logged_app, status_data)
    logged_app.task_statuses_page.open_status_from_row(
        status_data["name"],
        status_data["slug"],
    )
    logged_app.task_statuses_form_page.update_task_status_info(
        name=updated_status_data["name"],
        slug=updated_status_data["slug"],
    )

    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        POPUP_UPDATED,
    )
    open_statuses_page(logged_app)
    assert wait_for(
        lambda: logged_app.task_statuses_page.is_task_status_present(
            status_data["name"],
            status_data["slug"],
        ),
        False,
    ) is False
    assert logged_app.task_statuses_page.is_task_status_present(
        updated_status_data["name"],
        updated_status_data["slug"],
    )


@pytest.mark.step_5_deleteOne
def test_delete_status(logged_app):
    status_data = build_status_data()

    create_status(logged_app, status_data)
    logged_app.task_statuses_page.open_status_from_row(
        status_data["name"],
        status_data["slug"],
    )
    logged_app.task_statuses_form_page.delete_task_status()

    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        POPUP_DELETED,
    )
    open_statuses_page(logged_app)
    assert not logged_app.task_statuses_page.is_task_status_present(
        status_data["name"],
        status_data["slug"],
    )


@pytest.mark.step_5_deleteAll
def test_delete_all_statuses(logged_app):
    create_status(logged_app, build_status_data())
    open_statuses_page(logged_app)
    initial_count = logged_app.task_statuses_page.get_statuses_count()

    assert initial_count > 0

    logged_app.task_statuses_page.choose_all_statuses()
    logged_app.task_statuses_page.delete_chosen_statuses()

    assert logged_app.task_statuses_page.popup.wait_popup_with_text(
        POPUP_BULK_DELETED_TEMPLATE.format(count=initial_count)
    )
    assert wait_for(
        lambda: logged_app.task_statuses_page.get_statuses_count(),
        0,
    ) == 0
