.PHONY: install start check lint test test-coverage coverage-xml

install:
	uv sync --group dev

start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

check:
	$(MAKE) lint
	$(MAKE) test

lint:
	uv run ruff check .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=tests --cov-report=xml tests/

coverage-xml:
	$(MAKE) test-coverage
