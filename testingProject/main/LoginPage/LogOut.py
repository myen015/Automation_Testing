import time
from selenium.webdriver.common.by import By


class LogOut:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        logout = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span')
        logout.click()
        time.sleep(4)

        logout_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')
        logout_button.click()
        time.sleep(5)
