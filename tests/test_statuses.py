import uuid

import pytest


@pytest.fixture
def clean_statuses_page(statuses_page):
    assert statuses_page.delete_all_statuses()
    return statuses_page


@pytest.fixture
def seeded_status(clean_statuses_page):
    name = f"Status_{uuid.uuid4().hex[:5]}"
    slug = f"slug-{uuid.uuid4().hex[:5]}"
    assert clean_statuses_page.create_status(name, slug)
    return clean_statuses_page, name, slug


def test_create_status(clean_statuses_page):
    name = f"Backlog_{uuid.uuid4().hex[:5]}"
    slug = f"backlog-{uuid.uuid4().hex[:5]}"
    assert clean_statuses_page.create_status(name, slug)


def test_view_statuses_list(seeded_status):
    statuses_page, name, slug = seeded_status
    statuses_page.open_page()
    statuses_page.wait_for_text("Name")
    statuses_page.wait_for_text("Slug")
    row_values = statuses_page.get_status_row_values(name)
    assert row_values["name"] == name
    assert row_values["slug"] == slug


def test_edit_status(seeded_status):
    statuses_page, name, _slug = seeded_status
    new_name = f"{name}_Updated"
    new_slug = f"updated-{uuid.uuid4().hex[:5]}"
    assert statuses_page.edit_status(name, new_name, new_slug)


def test_delete_status(seeded_status):
    statuses_page, name, _slug = seeded_status
    assert statuses_page.delete_status(name)


def test_delete_all_statuses(seeded_status):
    statuses_page, _name, _slug = seeded_status
    assert statuses_page.delete_all_statuses()
