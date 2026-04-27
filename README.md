### Hexlet tests and linter status:
[![Actions Status](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions)

[![CI](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions/workflows/build.yml/badge.svg)](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions/workflows/build.yml)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=AmidamaruQ_qa-auto-engineer-python-tw-project-314&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=AmidamaruQ_qa-auto-engineer-python-tw-project-314)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=AmidamaruQ_qa-auto-engineer-python-tw-project-314&metric=coverage)](https://sonarcloud.io/summary/new_code?id=AmidamaruQ_qa-auto-engineer-python-tw-project-314)

## О проекте

UI automation проект на `pytest` и `selenium` для тестирования kanban-приложения.

Текущая структура:

- `pages/` - page object'ы и агрегатор `Pages`
- `tests/` - тесты и pytest fixtures
- `config.py` - runtime-конфиг тестового раннера
- `settings.py` - дефолтные значения таймаутов и браузерных настроек
- `utils/` - служебные функции

## Стек

- `Python`
- `pytest`
- `selenium`
- `uv`
- `docker`

## Быстрый старт

```bash
uv sync --group dev
```

Для локального запуска против контейнера с приложением:

```bash
make start
APP_BASE_URL=http://localhost:5173 uv run pytest
```

По умолчанию используются креды из [tests/constants.py](/Users/amidamaruq/Documents/projects/qa-auto-engineer-python-tw-project-314/tests/constants.py):

- `admin@google.com`
- `admin!admin`

Поддерживаемые переменные окружения:

- `APP_BASE_URL` - адрес приложения, если не используется `IMPLEMENTATION`
- `IMPLEMENTATION` - если задано, base URL строится как `http://<implementation>.test`
- `HEADLESS` - `true/false`, включает headless Chrome
- `CHROME_BIN` - путь к Chrome/Chromium при нестандартной установке
- `TEST_LOG_DIR` - директория для `pytest.log`
- `TEST_LOG_LEVEL` - уровень логирования
- `BROWSER_WINDOW_SIZE` - размер окна, например `1920,1080`
- `PAGE_LOAD_TIMEOUT` - timeout загрузки страницы
- `SELENIUM_IMPLICIT_WAIT` - implicit wait
- `SELENIUM_DEFAULT_TIMEOUT` - timeout для page object ожиданий

## Команды

```bash
make install
make start
make test
make lint
make check
```

`make test` запускает весь suite из `tests/`.
