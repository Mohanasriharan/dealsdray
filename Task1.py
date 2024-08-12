import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


devices = {
    "Desktop": [
        {"name": "1920x1080", "width": 1920, "height": 1080},
        {"name": "1366x768", "width": 1366, "height": 768},
        {"name": "1536x864", "width": 1536, "height": 864}
    ],
    "Mobile": [
        {"name": "360x640", "width": 360, "height": 640},
        {"name": "414x896", "width": 414, "height": 896},
        {"name": "375x667", "width": 375, "height": 667}
    ]
}


browsers = ['chrome', 'firefox']


sitemap_url = 'https://www.getcalley.com/page-sitemap.xml'



def get_driver(browser):
    if browser == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    return driver


def capture_screenshot(driver, device_name, resolution_name, browser_name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    directory = f"Screenshots/{device_name}/{resolution_name}/{browser_name}"
    os.makedirs(directory, exist_ok=True)
    screenshot_path = f"{directory}/screenshot-{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot: {screenshot_path}")



def run_tests():
    for browser in browsers:
        driver = get_driver(browser)
        for device_name, resolutions in devices.items():
            for res in resolutions:
                driver.set_window_size(res['width'], res['height'])
                driver.get(sitemap_url)
                time.sleep(2)  # Wait for page to load
                capture_screenshot(driver, device_name, res['name'], browser)
        driver.quit()


if __name__ == "__main__":
    run_tests()
