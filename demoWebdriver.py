from selenium import webdriver
from locust import task, HttpUser, between
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WebdriverUsage(HttpUser):
    wait_time = between(2, 3)
    driver = None
    host = "https://www.saucedemo.com/"
    url = "https://www.saucedemo.com/"

    def __init__(self, environment):
        super().__init__(environment)
        self.driver = webdriver.Chrome()

    def on_start(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def on_stop(self):
        self.driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()

    @task
    def addToCart(self):
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        self.driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        self.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys('Suman')
        self.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys('Reddy')
        self.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys('560099')
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        Total_cost = self.driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']").text
        act_cost = 'Total: $112.28'
        self.assertEquals(act_cost, Total_cost, "TotalCost MissMatch and Failed")
        print(" TotalCost Fetched Successfully")
