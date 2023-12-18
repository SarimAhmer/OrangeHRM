from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrangeHRMLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_field = self.driver.find_element(By.NAME, 'username')
        password_field = self.driver.find_element(By.NAME, 'password')
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        submit_button.click()
        time.sleep(5)

    def navigate_to_about_page(self):
        dropdown = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span')
        dropdown.click()
        time.sleep(2)
        about_link = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[1]/a')
        about_link.click()
        time.sleep(5)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()

    orangehrm_login = OrangeHRMLogin(driver)
    orangehrm_login.login("Admin", "admin123")

    orangehrm_login.navigate_to_about_page()
    driver.quit()
