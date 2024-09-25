import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# driver = None


def pytest_addoption(parser):  # declared and initialized a run time variable. expect --browser_name from  cmd terminal
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):   # request is an instance for this method
    # global driver
    browser_name = request.config.getoption("browser_name")   # passing the variable to the method
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()

    # assigning local driver of this fixture to the class driver - this makes driver work on main test
    request.cls.driver = driver
    yield
    driver.close()

# @pytest.mark.hookwrapper
# def pytest_runtest_markereport(item):
#     """
#         Extends the pytest plygin to take and embed screenshot in html report, whenever test fails
#         :param item:
#         """
#
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style ="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)





