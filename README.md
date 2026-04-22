### Hexlet tests and linter status:
[![Actions Status](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions)

[![CI](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions/workflows/build.yml/badge.svg)](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions/workflows/build.yml)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=AmidamaruQ_qa-auto-engineer-python-tw-project-314&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=AmidamaruQ_qa-auto-engineer-python-tw-project-314)

## О проекте

UI automation проект на `pytest` и `selenium` для тестирования kanban-приложения.

## Стек

- `Python`
- `pytest`
- `selenium`
- `uv`
- `docker`

## Быстрый старт

```bash
cp .env.example .env
uv sync
```

В `.env` должны быть заданы:
- `APP_BASE_URL`
- `LOGIN`
- `PASSWORD`

## Команды

```bash
make install
make start
make test
make lint
make build
```

`make build` поднимает контейнер приложения, дожидается его готовности и запускает тесты.
