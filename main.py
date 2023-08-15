from selenium import webdriver

def get_driver():
    # Configured options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    # Lines 12 and 13 help Selenium avoid detection from the web browser
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    # Corrected XPath expression to find the h1 element
    element = driver.find_element_by_xpath("//h1[contains(text(), 'Automated Page')]")
    return element.text

print(main())