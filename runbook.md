# Runbook

## v0.6 – UC/Selenium kapcsolható driver réteg

**Váltás UC ↔ Selenium:**
- Állítsd a `STEALTH_MODE` ENV-et: `uc` vagy `selenium`, majd indítsd újra a folyamatot.
- Indításkor a logban megjelenik: `driver=uc|selenium`, `headless=...`, és diagnosztikák (`capabilities`, `navigator.webdriver`, UA, UC verzió).

**UC frissítési rutin (Chrome főverzió váltás):**
1) Frissítsd a környezetben a Chrome főverziót.
2) Ha UC nem talál kompatibilis drivert, állítsd a `UC_VERSION_MAIN` ENV-et a főverzióra (pl. `126`); kódmódosítás nem kell.

**Profil és extra kapcsolók:**
- Opcionális perzisztens profil: `CHROME_PROFILE_PATH` (azonos profilt **ne** használd párhuzamosan több folyamatból).
- Extra Chrome flag-ek: `CHROME_ARGS` (szóközzel elválasztva, mindkét módban alkalmazzuk).
- Konténer/CI kompat.: mindkét módban kötelezően használjuk: `--no-sandbox`, `--disable-dev-shm-usage`; headless esetén: `--headless=new`.

**Gyors diagnosztika:**
```bash
python3 bin/run_browser_diag.py
# várható logok: driver=..., diag.capabilities=..., diag.navigator.webdriver=..., diag.ua=..., diag.uc_version=...
```
