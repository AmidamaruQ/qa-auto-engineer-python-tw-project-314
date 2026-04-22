start:
	docker run --rm -d -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check