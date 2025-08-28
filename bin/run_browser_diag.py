#!/usr/bin/env python3
import logging, sys
from utils.driver_factory import make_driver

logging.basicConfig(level=logging.INFO, format="%%(asctime)s %%(levelname)s %%(message)s")
log = logging.getLogger(__name__)

def main():
    drv = make_driver()
    try:
        try:
            drv.get("about:blank")
        except Exception as e:
            log.warning("driver.get about:blank failed: %r", e)
        try:
            caps = getattr(drv, "capabilities", {})
            log.info("diag.capabilities=%s", caps)
        except Exception as e:
            log.warning("diag.capabilities: error=%r", e)
        try:
            wd = drv.execute_script("return navigator.webdriver")
            log.info("diag.navigator.webdriver=%s", wd)
        except Exception as e:
            log.warning("diag.navigator.webdriver: error=%r", e)
        try:
            ua = drv.execute_script("return navigator.userAgent")
            log.info("diag.ua=%s headless_ua_flag=%s", ua, ("HeadlessChrome" in (ua or "")))
        except Exception as e:
            log.warning("diag.ua: error=%r", e)
        try:
            import undetected_chromedriver as uc
            log.info("diag.uc_version=%s", getattr(uc, "__version__", "unknown"))
        except Exception:
            pass
    finally:
        try:
            drv.quit()
        except Exception:
            pass
if __name__ == "__main__":
    sys.exit(main())
