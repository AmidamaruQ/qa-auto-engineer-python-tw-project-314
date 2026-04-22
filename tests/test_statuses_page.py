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


def test_create_status(logged_app):
    status_data = build_status_data()

    create_status(logged_app, status_data)

    assert logged_app.task_statuses_page.is_task_status_present(
        status_data["name"],
        status_data["slug"],
    )


def test_update_status(logged_app):
    status_data = build_status_data()
    updated_status_data = {
        **status_data,
        "slug": build_status_data()["slug"],
    }

    create_status(logged_app, status_data)
    assert logged_app.task_statuses_page.is_task_status_present(
        status_data["name"],
        status_data["slug"],
    )

    logged_app.task_statuses_page.open_status_from_row(
        status_data["name"],
        status_data["slug"],
    )
    logged_app.task_statuses_form_page.update_task_status_info(
        slug=updated_status_data["slug"],
    )

    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        POPUP_UPDATED
    )
    open_statuses_page(logged_app)
    assert wait_for(
        lambda: logged_app.task_statuses_page.is_task_status_present(
            updated_status_data["name"],
            updated_status_data["slug"],
        )
    )
    assert wait_for(
        lambda: not logged_app.task_statuses_page.is_task_status_present(
            status_data["name"],
            status_data["slug"],
        )
    )


def test_delete_task_status(logged_app):
    status_data = build_status_data()

    create_status(logged_app, status_data)
    assert logged_app.task_statuses_page.is_task_status_present(
        status_data["name"],
        status_data["slug"],
    )

    logged_app.task_statuses_page.open_status_from_row(
        status_data["name"],
        status_data["slug"],
    )
    logged_app.task_statuses_form_page.delete_task_status()

    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        POPUP_DELETED
    )
    open_statuses_page(logged_app)
    assert not logged_app.task_statuses_page.is_task_status_present(
        status_data["name"],
        status_data["slug"],
    )


def test_multiple_delete_task_status(logged_app):
    first_status_data = build_status_data()
    second_status_data = build_status_data()

    create_status(logged_app, first_status_data)
    create_status(logged_app, second_status_data)

    logged_app.task_statuses_page.choose_status_from_row(
        first_status_data["name"],
        first_status_data["slug"],
    )
    logged_app.task_statuses_page.choose_status_from_row(
        second_status_data["name"],
        second_status_data["slug"],
    )
    logged_app.task_statuses_page.delete_chosen_statuses()

    assert logged_app.task_statuses_form_page.popup.wait_popup_with_text(
        POPUP_BULK_DELETED_TEMPLATE.format(count=2)
    )
    assert not logged_app.task_statuses_page.is_task_status_present(
        first_status_data["name"],
        first_status_data["slug"],
    )
    assert not logged_app.task_statuses_page.is_task_status_present(
        second_status_data["name"],
        second_status_data["slug"],
    )
