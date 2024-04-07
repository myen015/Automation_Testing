import time
from selenium.webdriver.common.by import By


class SearchFunction:
    def __init__(self, driver):
        self.driver = driver

    def search_functionality(self, search_text):
        search_field = self.driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search"]')
        time.sleep(2)
        search_field.click()
        time.sleep(3)

        search_field.send_keys(search_text)
        time.sleep(3)

        search_results = self.driver.find_elements(By.CLASS_NAME, 'oxd-main-menu-item--name')
        found_categories = []
        for result in search_results:
            category_name = result.text
            if search_text in category_name.lower():
                found_categories.append(category_name)
        assert len(found_categories) > 0, f"No categories containing '{search_text}' were found."

        print("Found categories:", found_categories)

