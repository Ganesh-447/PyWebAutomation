from selenium.webdriver.common.by import By



class DashboardPage():


    def __init__(self,driver):
        self.driver = driver


    username = (By.XPATH,"//span[@data-qa='lufexuloga']")

    def get_username(self):
        return self.driver.find_element(*DashboardPage.username)
