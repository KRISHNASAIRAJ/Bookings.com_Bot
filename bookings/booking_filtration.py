''' this file will include a class with instance methods that will repsonsbile for interacting with
website after response '''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFlitration():
    def __init__(self,driver:WebDriver):
        self.driver=driver
        
    def start_ratings(self,*stars):
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(10)
        start_filteration_box=self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="class"]')
        start_child_ele=start_filteration_box.find_elements(By.CSS_SELECTOR,'*')
        
        for star_value in stars:
            for star_childs in start_child_ele:
                if str(star_childs.get_attribute('innerHTML')).strip()==f"{star_value} star":
                    star_childs.click()