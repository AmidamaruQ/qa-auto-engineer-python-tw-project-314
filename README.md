### Hexlet tests and linter status:
[![Actions Status](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AmidamaruQ/qa-auto-engineer-python-tw-project-314/actions)

## UI test framework

Stack:
- `pytest`
- `python-dotenv`
- `selenium`

Environment setup:

```bash
cp .env.example .env
```

Available variables:
- `APP_BASE_URL` - base URL for UI tests

Available fixtures:
- `env_config` - loads variables from `.env`
- `base_url` - returns `--base-url`, then `APP_BASE_URL`, then default `http://127.0.0.1:5173`
