from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import names
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_Login import OrangeHRMLogin
from selenium.webdriver.common.action_chains import ActionChains
from test_Sidebar import SideBar


class UserClaim:
    def __init__(self, driver):
        self.driver = driver
        self.OrangeHRMLogin = OrangeHRMLogin(driver)
        self.OrangeHRMLogin.login("Admin", "admin123")
        self.sidebar = SideBar(driver)
        self.sidebar.SideBarOptions("Claim")
    def submitClaim(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input'))
        )
        name = self.driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input')
        name.send_keys(random.choice(string.ascii_letters))
        time.sleep(2)
        name.send_keys(Keys.ARROW_DOWN)
        name.send_keys(Keys.RETURN)

        # Event_type = ['a', 'm', 't']
        # event = self.driver.find_element(By.XPATH,
        #                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]')
        # event.click()
        # event.send_keys(random.choice(Event_type))
        # event.send_keys(Keys.ARROW_DOWN)
        # event.send_keys(Keys.RETURN)

        # currency = self.driver.find_element(By.XPATH,
        #                                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]')
        # currency.send_keys(random.choice(string.ascii_letters))
        # currency.send_keys(Keys.RETURN)

        Submit = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div[2]/form/div[3]/button[2]')
        Submit.click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    claims = UserClaim(driver)

    claims.submitClaim()

    driver.close()