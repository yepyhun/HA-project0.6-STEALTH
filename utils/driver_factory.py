# utils/driver_factory.py
import os, logging, pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import undetected_chromedriver as uc

log = logging.getLogger(__name__)

def _apply_common_flags(opts, headless: bool):
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    if headless:
        opts.add_argument("--headless=new")

def make_driver():
    mode = os.getenv("STEALTH_MODE", "selenium").strip().lower()
    headless = os.getenv("HEADLESS", "1") == "1"
    profile_path = os.getenv("CHROME_PROFILE_PATH", "").strip()
    uc_version_main_env = os.getenv("UC_VERSION_MAIN", "").strip()
    extra_args = os.getenv("CHROME_ARGS", "").strip()

    if mode == "uc":
        opts = uc.ChromeOptions()
        _apply_common_flags(opts, headless)
        if profile_path:
            pathlib.Path(profile_path).mkdir(parents=True, exist_ok=True)
            opts.add_argument(f"--user-data-dir={profile_path}")
            log.warning("UC profile in use at %s; avoid parallel runs on the same profile.", profile_path)
        for arg in (extra_args.split() if extra_args else []):
            opts.add_argument(arg)
        kwargs = {}
        if uc_version_main_env.isdigit():
            kwargs["version_main"] = int(uc_version_main_env)
        drv = uc.Chrome(options=opts, **kwargs)
        log.info("driver=uc headless=%s uc_version_main=%s", headless, uc_version_main_env or "auto")
        return drv

    # baseline: Selenium
    opts = ChromeOptions()
    _apply_common_flags(opts, headless)
    opts.add_argument("--disable-blink-features=AutomationControlled")
    for arg in (extra_args.split() if extra_args else []):
        opts.add_argument(arg)
    drv = webdriver.Chrome(options=opts)
    log.info("driver=selenium headless=%s", headless)
    return drv
