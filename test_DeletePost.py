from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_Login import OrangeHRMLogin
from test_Sidebar import SideBar



class DeletePost:
    def __init__(self, driver):
        self.driver = driver
        self.OrangeHRMLogin = OrangeHRMLogin(driver)
        self.OrangeHRMLogin.login("Admin", "admin123")
        self.SideBar = SideBar(driver)
        self.SideBar.SideBarOptions("Buzz")

    def postDel(self):
        for i in range(50):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button'))
            )
            options = self.driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button')
            options.click()
            self.delPost = self.driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/ul/li[1]')
            self.delPost.click()
            self.delete = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
            self.delete.click()
            time.sleep(2)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    delete = DeletePost(driver)

    delete.postDel()

    driver.quit()