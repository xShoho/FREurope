import requests

from datetime import datetime
from zoneinfo import ZoneInfo
from bs4 import BeautifulSoup

from core import browser, logger


driver = browser.init_driver()
browser_logger = logger.init_logger("browser")


def parse_utc(dt: datetime, from_tz: str = "Europe/Warsaw") -> datetime:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo= ZoneInfo(from_tz))
    else:
        dt = dt.astimezone(ZoneInfo(from_tz))
        
    return dt.astimezone(ZoneInfo("UTC"))


def parse_HTML(URL: str):
    headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246" }
    response = requests.get(url= URL, headers= headers)
    
    if response.status_code == 200:
        driver.get(URL)
        browser_logger.info(f"Succesfully connected to: { URL }")
        return BeautifulSoup(driver.page_source, 'lxml')
    else:
        browser_logger.error(f"Connection to: { URL } failed with HTTP response code: { response.status_code }")