def test_create_label(logged_app):
    # Arrange: prepare label data.
    label_name = "label_name"
    # Act: open the label form and create a label.
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(label_name)
    # Assert: verify the creation popup is shown.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created"
    )
    # Assert: verify the created label is present in the table.
    logged_app.label_form_page.sidebar.open_labels_page()
    assert logged_app.labels_page.is_label_present(label_name)


def test_update_label(logged_app):
    # Arrange: prepare source and updated label data.
    label_name = "label_name"
    new_label_name = "new_label_name"
    # Act: create the initial label.
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(label_name)
    # Assert: verify the original label is present before editing.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created"
    )
    logged_app.label_form_page.sidebar.open_labels_page()
    assert logged_app.labels_page.is_label_present(label_name)
    # Act: open the label and update its name.
    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.update_label_info(new_label_name)
    # Assert: verify the updated label is present in the table.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element updated")
    assert logged_app.labels_page.is_label_present(new_label_name)


def test_delete_label(logged_app):
    # Arrange: prepare label data.
    label_name = "label_name"
    # Act: create the label that will be deleted.
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(label_name)
    # Assert: verify the label exists before deletion.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.label_form_page.sidebar.open_labels_page()
    assert logged_app.labels_page.is_label_present(label_name)
    # Act: open the label and delete it.
    logged_app.labels_page.open_label_from_row(label_name)
    logged_app.label_form_page.delete_label()
    # Assert: verify the label is removed from the table.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element deleted")
    assert not logged_app.labels_page.is_label_present(label_name)


def test_multiple_delete_label(logged_app):
    # Arrange: prepare data for two labels.
    first_label_name = "first_label_name"
    second_label_name = "second_label_name"
    # Act: create the first label.
    logged_app.base_page.sidebar.open_labels_page()
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(first_label_name)
    # Assert: verify the first label creation succeeds.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.label_form_page.sidebar.open_labels_page()
    # Act: create the second label.
    logged_app.labels_page.open_create_label()
    logged_app.label_form_page.create_label(second_label_name)
    # Assert: verify the second label creation succeeds.
    assert logged_app.label_form_page.popup.wait_popup_with_text(
        "Element created")
    logged_app.label_form_page.sidebar.open_labels_page()
    # Assert: verify both labels are present before bulk deletion.
    assert logged_app.labels_page.is_label_present(first_label_name)
    assert logged_app.labels_page.is_label_present(second_label_name)
    # Act: select both labels and delete them in bulk.
    logged_app.labels_page.choose_label_from_row(first_label_name)
    logged_app.labels_page.choose_label_from_row(second_label_name)
    logged_app.labels_page.delete_chosen_label()
    # Assert: verify both labels are removed from the table.
    assert logged_app.labels_page.popup.wait_popup_with_text(
        "2 elements deleted")

    assert not logged_app.labels_page.is_label_present(first_label_name)
    assert not logged_app.labels_page.is_label_present(second_label_name)
