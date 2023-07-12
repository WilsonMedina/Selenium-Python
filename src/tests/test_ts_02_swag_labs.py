import sys
import pytest
import time
sys.path.append("..")

from functions.functions import Functions
from pages.page_login import Page_login
from pages.page_plp import Page_plp
from pages.data import Data

class Test_remove_product:

    
    """
        In the video I don't think I explain the fixture function very well, it's a decorator that returns the function that we wrap to have it 
        available for use
    """

    @pytest.fixture  
    def before_each(self):

       self.driver = Functions.open_browser(self) 
       Functions.get_url(self, Data.url)
       page_title = self.driver.title
       assert page_title == Data.text_swag_labs, Data.msg_incorrect_texts 
       Page_login.login(self, Data.username, Data.password, Data.json_file, Data.username_input, Data.password_input, Data.login_button)
       selector_app_logo = Functions.get_selector_pom(self, Data.json_file, Data.app_logo_text)
       assert selector_app_logo.text == Data.text_swag_labs, Data.msg_incorrect_texts 

    def test_01_remove_all_product(self, before_each):

        num_to_add = 5
        num_to_remove = 5

        chosen_list = Page_plp.add_to_cart(self, Data.json_file, Data.add_and_remove_cart_button, num_to_add)
        selector_icon_scp = Functions.get_selector_pom(self, Data.json_file, Data.icon_shopping_cart)
        assert (str(num_to_add) == selector_icon_scp.text or '' == selector_icon_scp.text), Data.msg_incorrect_nums
        time.sleep(Data.time)
        Page_plp.remove_cart(self, Data.json_file, Data.add_and_remove_cart_button, chosen_list)
        assert (str(num_to_add - num_to_remove) == selector_icon_scp.text or '' == selector_icon_scp.text), Data.msg_incorrect_nums
        time.sleep(Data.time)
        

    def test_02_remove_two_products(self, before_each):

        num_to_add = 4
        num_to_remove = 2

        chosen_list = Page_plp.add_to_cart(self, Data.json_file, Data.add_and_remove_cart_button, num_to_add)
        selector_icon_scp = Functions.get_selector_pom(self, Data.json_file, Data.icon_shopping_cart)
        assert (str(num_to_add) == selector_icon_scp.text or '' == selector_icon_scp.text), Data.msg_incorrect_nums   
        time.sleep(Data.time)
        Page_plp.remove_cart(self, Data.json_file, Data.add_and_remove_cart_button, chosen_list, num_to_remove)
        assert (str(num_to_add - num_to_remove) == selector_icon_scp.text or '' == selector_icon_scp.text), Data.msg_incorrect_nums 
        time.sleep(Data.time)
        
    def test_03_remove_five_products(self, before_each):

        num_to_add = 6
        num_to_remove = 4

        chosen_list = Page_plp.add_to_cart(self, Data.json_file, Data.add_and_remove_cart_button, num_to_add)
        selector_icon_scp = Functions.get_selector_pom(self, Data.json_file, Data.icon_shopping_cart)
        assert (str(num_to_add) == selector_icon_scp.text or '' == selector_icon_scp.text), Data.msg_incorrect_nums   
        time.sleep(Data.time)
        Page_plp.remove_cart(self, Data.json_file, Data.add_and_remove_cart_button, chosen_list, num_to_remove)
        assert (str(num_to_add - num_to_remove) == selector_icon_scp.text or '' == selector_icon_scp.text), Data.msg_incorrect_nums 
        time.sleep(Data.time)
        
    def after_each(self, before_each):

        Functions.close_browser(self)

if __name__ == "__main__":
    
    pytest.main()