import uuid

import pytest


@pytest.fixture
def clean_labels_page(labels_page):
    assert labels_page.delete_all_labels()
    assert labels_page.create_label("Label_Name")
    return labels_page


@pytest.fixture
def seeded_label(clean_labels_page):
    name = f"Label_{uuid.uuid4().hex[:5]}"
    assert clean_labels_page.create_label(name)
    return clean_labels_page, name


def test_create_label(clean_labels_page):
    name = f"New_Label_{uuid.uuid4().hex[:5]}"
    assert clean_labels_page.create_label(name)


def test_view_labels_list(clean_labels_page):
    clean_labels_page.open_page()
    clean_labels_page.wait_until_label_present("Label_Name")
    assert clean_labels_page.get_table() is not None


def test_edit_label(seeded_label):
    labels_page, name = seeded_label
    new_name = f"{name}_Updated"
    assert labels_page.edit_label(name, new_name)


def test_delete_label(seeded_label):
    labels_page, name = seeded_label
    assert labels_page.delete_label(name)


def test_delete_all_labels(seeded_label):
    labels_page, _name = seeded_label
    assert labels_page.delete_all_labels()
