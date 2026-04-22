from uuid import uuid4

POPUP_CREATED = "Element created"
POPUP_UPDATED = "Element updated"
POPUP_DELETED = "Element deleted"
POPUP_BULK_DELETED_TEMPLATE = "{count} elements deleted"


def unique_suffix():
    return uuid4().hex[:8]


def build_user_data(suffix=None):
    suffix = suffix or unique_suffix()
    return {
        "email": f"user_{suffix}@mail.com",
        "first_name": f"first_{suffix}",
        "second_name": f"last_{suffix}",
    }


def build_label_name(prefix="label", suffix=None):
    suffix = suffix or unique_suffix()
    return f"{prefix}_{suffix}"


def build_status_data(suffix=None):
    suffix = suffix or unique_suffix()
    return {
        "name": f"status_{suffix}",
        "slug": f"slug-{suffix}",
    }


def build_task_data(suffix=None):
    suffix = suffix or unique_suffix()
    return {
        "assignee": "emily@example.com",
        "title": f"title_{suffix}",
        "content": f"content_{suffix}",
        "status": "Draft",
        "label": "critical",
    }
