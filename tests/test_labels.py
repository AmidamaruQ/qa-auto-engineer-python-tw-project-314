def test_create_label(logged_app):
    label_name = "label_name"
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(label_name)
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created"
    )
    logged_app.label_form_page.sidebar.open_labels_page()
    assert logged_app.labels_page.is_label_present(label_name)


def test_update_label(logged_app):
    label_name = "label_name"
    new_label_name = "new_label_name"
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(label_name)
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created"
    )
    logged_app.label_form_page.sidebar.open_labels_page()
    assert logged_app.labels_page.is_label_present(label_name)
    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.update_label_info(new_label_name)
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element updated")
    assert logged_app.labels_page.is_label_present(new_label_name)


def test_delete_label(logged_app):
    label_name = "label_name"
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(label_name)
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.label_form_page.sidebar.open_labels_page()
    assert logged_app.labels_page.is_label_present(label_name)
    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.delete_label()
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element deleted")
    assert not logged_app.labels_page.is_label_present(label_name)


def test_multiple_delete_label(logged_app):
    first_label_name = "first_label_name"
    second_label_name = "second_label_name"
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(first_label_name)
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.label_form_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(second_label_name)
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.label_form_page.sidebar.open_labels_page()
    assert logged_app.labels_page.is_label_present(first_label_name)
    assert logged_app.labels_page.is_label_present(second_label_name)
    logged_app.labels_page.choose_label_from_row(first_label_name)
    logged_app.labels_page.choose_label_from_row(second_label_name)
    logged_app.labels_page.delete_chosen_label()
    assert logged_app.labels_page.popup.wait_popup_with_text(
        "2 elements deleted")

    assert not logged_app.labels_page.is_label_present(first_label_name)
    assert not logged_app.labels_page.is_label_present(second_label_name)
