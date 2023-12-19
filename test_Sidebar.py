from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from test_Login import OrangeHRMLogin

class SideBar:
    def __init__(self, driver):
        self.driver = driver


    def SideBarOptions(self, options):
        if(options == "adminside"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
            )
            self.admin = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
            self.admin.click()
            time.sleep(3)
        elif(options == "PIM"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))
            )
            self.PIM = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
            self.PIM.click()
            time.sleep(3)
        elif(options == "Leave"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a'))
            )
            self.Leave = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a')
            self.Leave.click()
            time.sleep(3)
        elif(options == "Time"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a'))
            )
            self.Time = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a')
            self.Time.click()
            time.sleep(3)
        elif(options == "Recruit"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a'))
            )
            self.Recruit = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a')
            self.Recruit.click()
            time.sleep(3)
        elif(options == "MyInfo"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'))
            )
            self.MyInfo = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
            self.MyInfo.click()
            time.sleep(3)
        elif(options == "Perform"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a'))
            )
            self.Perform = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a')
            self.Perform.click()
            time.sleep(3)
        elif(options == "Dashboard"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'))
            )
            self.Dashboard = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a')
            self.Dashboard.click()
            time.sleep(3)
        elif(options == "Directory"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a'))
            )
            self.Directory = self.driver.find_element(By.XPATH,
                                                      '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a')
            self.Directory.click()
            time.sleep(3)
        elif(options == "Maintain"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a'))
            )
            self.Maintain = self.driver.find_element(By.XPATH,
                                                     '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
            self.Maintain.click()
            time.sleep(3)
        elif(options == "Claim"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a'))
            )
            self.Claim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a')
            self.Claim.click()
            time.sleep(3)
        elif(options == "Buzz"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'))
            )
            self.Buzz = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')
            self.Buzz.click()
            time.sleep(3)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()

    nav = SideBar(driver)
    nav.SideBarOptions("adminside")

    driver.quit()