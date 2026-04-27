.PHONY: install start stop check lint test test-coverage
install:
	uv sync --group dev

start:
	docker run -d --rm \
		--name qa-auto-python-testing-app \
		-p 5173:5173 \
		hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

check:
	$(MAKE) lint
	$(MAKE) test

lint:
	uv run ruff check .

test:
	uv run pytest

test-coverage:
	uv run --with pytest-cov pytest \
		--cov=pages \
		--cov=utils \
		--cov=config \
		--cov=settings \
		--cov-report=xml \
		tests/
