# CHANGELOG

## v0.6
- Switchable driver layer: **undetected-chromedriver** (`STEALTH_MODE=uc`) vagy baseline Selenium (`STEALTH_MODE=selenium`).
- Új modul: `utils/driver_factory.py` (`make_driver()`), közös konténer/CI flag-ek: `--no-sandbox`, `--disable-dev-shm-usage`, headless esetén `--headless=new`.
- Diagnosztika: `bin/run_browser_diag.py` (capabilities, navigator.webdriver, User-Agent, UC verzió).
- `.env.example` és `runbook.md` frissítve (`UC_VERSION_MAIN`, `CHROME_ARGS`, `CHROME_PROFILE_PATH`). 
- `requirements.txt`: pinned `undetected-chromedriver==3.5.5`, ensured `selenium>=4.9`.
