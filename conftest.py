import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options=Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dir-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver=webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()