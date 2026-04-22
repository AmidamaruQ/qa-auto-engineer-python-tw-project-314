from tests.support import (
    POPUP_BULK_DELETED_TEMPLATE,
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


def test_update_label(logged_app):
    label_name = build_label_name()
    new_label_name = build_label_name(prefix="updated_label")

    create_label(logged_app, label_name)
    assert logged_app.labels_page.is_label_present(label_name)

    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.update_label_info(new_label_name)

    assert logged_app.label_form_page.popup.wait_popup_with_text(POPUP_UPDATED)
    open_labels_page(logged_app)
    assert wait_for(
        lambda: logged_app.labels_page.is_label_present(new_label_name)
    )
    assert wait_for(
        lambda: not logged_app.labels_page.is_label_present(label_name)
    )


def test_delete_label(logged_app):
    label_name = build_label_name()

    create_label(logged_app, label_name)
    assert logged_app.labels_page.is_label_present(label_name)

    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.delete_label()

    assert logged_app.label_form_page.popup.wait_popup_with_text(POPUP_DELETED)
    open_labels_page(logged_app)
    assert not logged_app.labels_page.is_label_present(label_name)


def test_multiple_delete_label(logged_app):
    first_label_name = build_label_name(prefix="first_label")
    second_label_name = build_label_name(prefix="second_label")

    create_label(logged_app, first_label_name)
    create_label(logged_app, second_label_name)

    assert logged_app.labels_page.is_label_present(first_label_name)
    assert logged_app.labels_page.is_label_present(second_label_name)

    logged_app.labels_page.choose_label_from_row(first_label_name)
    logged_app.labels_page.choose_label_from_row(second_label_name)
    logged_app.labels_page.delete_chosen_label()

    assert logged_app.labels_page.popup.wait_popup_with_text(
        POPUP_BULK_DELETED_TEMPLATE.format(count=2)
    )
    assert not logged_app.labels_page.is_label_present(first_label_name)
    assert not logged_app.labels_page.is_label_present(second_label_name)
