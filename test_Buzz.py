from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from test_Login import OrangeHRMLogin
from test_Sidebar import SideBar




class BuzzPost:
    def __init__(self,driver):
        self.driver = driver
        self.OrangeHRMLogin = OrangeHRMLogin(driver)
        self.OrangeHRMLogin.login("Admin", "admin123")
        self.SideBar = SideBar(driver)
        self.SideBar.SideBarOptions("Buzz")
    def PostRand(self):
        for i in range(50):
            time.sleep(2)
            self.textBox = self.driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/textarea')
            ActionChains(self.driver).move_to_element(self.textBox).click().perform()
            ActionChains(self.driver).move_to_element(self.textBox).send_keys(
                "Testing").perform()
            self.post = self.driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/div/button')
            ActionChains(self.driver).move_to_element(self.post).click().perform()
            time.sleep(2)

if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.maximize_window()

    spam = BuzzPost(driver)
    spam.PostRand()

    driver.quit()