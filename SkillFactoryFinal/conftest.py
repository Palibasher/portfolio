import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or edge")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language, en, fr, es, ru etc...")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart configurating for test..")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        language = request.config.getoption("language")
        options.add_experimental_option('prefs', {'intl.accept_languages' : language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument("--headless")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "edge":
        print("\nstart firefox browser for test..")
        browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge")
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()

