''' this file will include a class with instance methods that will repsonsbile for interacting with
website after response '''
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFlitration():
    def __init__(self,driver:WebDriver):
        self.driver=driver
        
    def start_ratings(self,*stars_values):
        time.sleep(3)
        start_filteration_box=self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="class"]')
        self.driver.implicitly_wait(4)
        start_child_ele=start_filteration_box.find_elements(By.CSS_SELECTOR,'*')
        for stars in stars_values:
            if(stars<=5 and stars>=1):
                for element in start_child_ele:
                    if(str(element.get_attribute('innerHTML'))).strip()==(f"{stars} stars"):
                        element.click()
                        self.driver.implicitly_wait(5)
                        time.sleep(2)
            else:
                print("Check Stars Rating Error!")
    
    def sort_price_lowest_first(self):
        self.driver.implicitly_wait(10)
        sort_selector_ele=self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sort_selector_ele.click()
        self.driver.implicitly_wait(3)
        lowest_price_first_button=self.driver.find_element(By.CSS_SELECTOR,'button[aria-label="Price (lowest first)"]')
        lowest_price_first_button.click()