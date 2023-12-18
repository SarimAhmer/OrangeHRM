import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from test_Login import OrangeHRMLogin


class DeleteUser:
    def __init__(self,driver):
        self.driver = driver
        self.orangeHRM = OrangeHRMLogin(driver)
        self.orangeHRM.login("Admin", "admin123")


    def GoToAdminPage(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
        )
        admin = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        admin.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[1]'))
        )

    def delete_user(self):
        for i in range(50):
            # Wait to find Delete Button
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[1]'))
            )

            userDelete = self.driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[1]')
            ActionChains(self.driver).move_to_element(userDelete).click(userDelete).perform()

            # Wait for Dialog Box
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'))
            )

            deleteBtn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
            ActionChains(self.driver).move_to_element(deleteBtn).click(deleteBtn).perform()



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    userDelete = DeleteUser(driver)

    userDelete.GoToAdminPage()
    userDelete.delete_user()

    driver.close()