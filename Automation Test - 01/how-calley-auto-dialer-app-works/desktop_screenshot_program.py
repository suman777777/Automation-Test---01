# https://www.getcalley.com/how-calley-auto-dialer-app-works/
## automation Test 1 -- UI testing
## Code for desktop--chrome browser
## URL -- https://www.getcalley.com/how-calley-auto-dialer-app-works/


import time
from selenium import webdriver
resolutions = [{"width": 1920, "height": 1080},
               {"width": 1366, "height": 768},
               {"width": 1536, "height": 864}]
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
def take_screenshot_with_resolution(resolution):
    opts.add_argument(f"--window-size={resolution['width']}, {resolution['height']}")
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    try:
        driver.get("https://www.getcalley.com/how-calley-auto-dialer-app-works/")
        screenshot_name = resolution["width"] ,  resolution["height"]
        driver.save_screenshot(str(screenshot_name) + ".png")
        print(f'screenshot taken with resolution {resolution['width']}*{resolution['height']}')
    finally:
        driver.quit()
for resolution in resolutions:
    take_screenshot_with_resolution(resolution)
