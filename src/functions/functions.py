import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Functions:

    browser = 'Chrome'

    def open_browser(self, browser = browser):

        if browser.lower() == 'chrome':

            options_browser = webdriver.ChromeOptions()
            options_browser.add_argument('start-maximized')
            options_browser.add_argument('incognito')
            options_browser.add_experimental_option('detach', True)
            driver = webdriver.Chrome(options=options_browser)

        if browser.lower() == 'firefox':
            
            driver = webdriver.Firefox()
            driver.maximize_window()

        return driver
    
    def get_url(self, url):

        self.driver.get(url)

    def close_browser(self):

        self.driver.quit()

    def get_selector_pom(self, json_file, key):

        json_path = ("C:\\Users\\wilso\\Desktop\\Python\\selenium\\selenium_test\\" + json_file + ".json")
        
        try:

            with open(json_path, "r") as json_pom:

                json_dict = json.loads(json_pom.read())
                select_by = json_dict[key]["select_by"]
                its_value = json_dict[key]["its_value"]
                multiple_select = json_dict[key]["multiple_select"]

                """
                    In the video I don't explain the WebDriverWait functionality because I had not done it but basically it's waiting for the
                    driver 5 seconds until with EC.presence_of_element_located or EC.presence_of_all_elements_located the selector or selectors
                    are available to be called
                """

                if select_by.lower() == "id" and multiple_select.lower() == "false":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, its_value))) 
                elif select_by.lower() == "name" and multiple_select.lower() == "false":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, its_value)))
                elif select_by.lower() == "name" and multiple_select.lower() == "true":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.NAME, its_value)))
                elif select_by.lower() == "xpath" and multiple_select.lower() == "false":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, its_value)))
                elif select_by.lower() == "xpath" and multiple_select.lower() == "true":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, its_value)))
                elif select_by.lower() == "css" and multiple_select.lower() == "false":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, its_value)))
                elif select_by.lower() == "css" and multiple_select.lower() == "true":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, its_value)))
                elif select_by.lower() == "class" and multiple_select.lower() == "false":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, its_value)))
                elif select_by.lower() == "class" and multiple_select.lower() == "true":
                    selector = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, its_value)))
    
                return selector
            
        except FileNotFoundError:
            print(f'Json file "{json_file}.json" no found')
            Functions.close_browser(self)
        
        except KeyError:
            print(f'Key "{key}" no found')
            Functions.close_browser(self)

        except NoSuchElementException:
            print(f'Selector "{its_value}" no found')
            Functions.close_browser(self)

        except TimeoutException:
            print(u'Time up')
            Functions.close_browser(self)

    def write_data(self, selector, text):

        selector.send_keys(text)

    def click(self, selector):

        selector.click()

   
           

                
            
            
        

        
    
