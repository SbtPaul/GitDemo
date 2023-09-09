import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="This is a comment"
        #original:        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")

    if browser_name == "chrome":
        service_obj = Service("C:/Users/SudipNobonita/node_modules/chromedriver/lib/chromedriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("C:/Users/SudipNobonita/AppData/Roaming/npm/node_modules/protractor/node_modules/webdriver-manager/selenium/geckodriver-v0.32.2.exe")
        driver = webdriver.Firefox(service=service_obj) # right click webdriver and import selenium webdriver
    elif browser_name == "IE":
        service_obj = Service("C:/Program Files/drivers/edge/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)  # right click webdriver and import selenium webdriver
    driver.implicitly_wait(3)
    driver.maximize_window()
    request.cls.driver = driver #this means, whatever class inherits this class will have a driver that's eq to the driver here
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".jpeg"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

