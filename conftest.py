import pytest
import allure
import time
import subprocess
import os
import signal
from playwright.sync_api import sync_playwright
from utils.reporter import AllureReporter
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="session")
def browser_context(request):
    # Use pytest-playwright's --browser option (returns a list, get first or default to chromium)
    browser_options = request.config.getoption("--browser")
    browser_name = browser_options[0] if browser_options else "chromium"

    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Invalid browser name: {browser_name}")

        context = browser.new_context()
        yield context

        context.close()
        browser.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    page.set_default_timeout(10000)
    yield page
    page.close()

@pytest.fixture
def reporter(page):
    return AllureReporter(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f" Test session ended at {end_time}")

    allure_results_dir = "allure-results"
    allure_report_dir = "allure-report"
    try:
        print(f"\nGenerating Allure report...")
        subprocess.run(f"allure generate {allure_results_dir} -o {allure_report_dir} --clean", shell=True, check=True)

        print(f"Opening Allure report... (Press Ctrl+C to close)")

        allure_process = subprocess.Popen(
            f"allure open {allure_report_dir}",
            shell=True,
            preexec_fn=os.setsid)

        try:
            allure_process.wait()
        except KeyboardInterrupt:
            print(f"\nCtrl+C detected. Closing Allure...")
            os.killpg(os.getpgid(allure_process.pid), signal.SIGTERM)
            print(f"Allure closed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error generating Allure report: {e}")
    except Exception as ex:
        print(f"Unexpected error during Allure report generation: {ex}")
