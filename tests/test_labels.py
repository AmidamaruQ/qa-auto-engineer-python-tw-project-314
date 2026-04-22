from tests.support import (
    POPUP_CREATED,
    POPUP_DELETED,
    POPUP_UPDATED,
    build_label_name,
)
from utils.utils import wait_for


def open_labels_page(app):
    app.base_page.sidebar.open_labels_page()


def create_label(app, label_name):
    open_labels_page(app)
    app.labels_page.open_create_label()
    app.label_form_page.create_label(label_name)
    assert app.label_form_page.popup.wait_popup_with_text(POPUP_CREATED)
    open_labels_page(app)


def test_create_label(logged_app):
    label_name = build_label_name()

    create_label(logged_app, label_name)

    assert logged_app.labels_page.is_label_present(label_name)


def test_view_label_list(logged_app):
    label_name = build_label_name()

    create_label(logged_app, label_name)

    headers = logged_app.labels_page.get_table_headers()

    assert "Name" in headers
    assert logged_app.labels_page.get_labels_count() > 0
    assert logged_app.labels_page.is_label_present(label_name)


def test_edit_label_form_prefilled(logged_app):
    label_name = build_label_name()
    new_label_name = build_label_name(prefix="updated_label")

    create_label(logged_app, label_name)
    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.update_label_info(new_label_name)

    assert logged_app.label_form_page.popup.wait_popup_with_text(POPUP_UPDATED)
    open_labels_page(logged_app)
    assert wait_for(
        lambda: not logged_app.labels_page.is_label_present(label_name)
    )
    assert wait_for(
        lambda: any(
            new_label_name in row_text
            for row_text in logged_app.labels_page.get_rows_text()
        )
    )


def test_delete_label_form(logged_app):
    label_name = build_label_name()

    create_label(logged_app, label_name)
    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.delete_label()

    assert logged_app.label_form_page.popup.wait_popup_with_text(POPUP_DELETED)
    open_labels_page(logged_app)
    assert not logged_app.labels_page.is_label_present(label_name)
