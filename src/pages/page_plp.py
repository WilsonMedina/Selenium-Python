import random
import time

from functions.functions import Functions
from pages.data import Data

class Page_plp:

    def add_to_cart(self, json_file, add_button, num_to_add = None):

        if num_to_add == None:
            num_to_add = 0

        selector_button_add_to_cart = Functions.get_selector_pom(self, json_file, add_button)

        index_list = []
        for index in range(len(selector_button_add_to_cart)):
            index_list.append(index)

        chosen_list = []
        while len(chosen_list) < num_to_add:
            num_random = random.choice(index_list)
            if num_random not in chosen_list:
                chosen_list.append(num_random)
                Functions.get_selector_pom(self, json_file, add_button)[num_random].click()

        return chosen_list

    def remove_cart(self, json_file, remove_button, chosen_list, num_to_remove = None):

        if num_to_remove == None:
            num_to_remove = len(chosen_list)
       
        chosen_remove_list = []
        while len(chosen_remove_list) < num_to_remove:
            num_random = random.choice(chosen_list)
            if num_random not in chosen_remove_list:
                chosen_remove_list.append(num_random)
                Functions.get_selector_pom(self, json_file, remove_button)[num_random].click()
                time.sleep(Data.time - 4)