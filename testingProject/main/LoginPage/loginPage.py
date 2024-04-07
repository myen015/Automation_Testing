import time
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
        time.sleep(2)

        username_field = self.driver.find_element(By.NAME,'username')
        username_field.send_keys(username)
        time.sleep(2)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)
        time.sleep(2)

        button = self.driver.find_elements(By.TAG_NAME, 'button')

        for button in button:
            if button.text == "Login":
                button.click()
                break

        time.sleep(5)

