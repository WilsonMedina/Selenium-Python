from functions.functions import Functions

class Page_login():

    def login(self, username, password, json_file, username_input, password_input, login_button):

        selector_username = Functions.get_selector_pom(self, json_file, username_input)
        selector_password = Functions.get_selector_pom(self, json_file, password_input)
        selector_button = Functions.get_selector_pom(self, json_file, login_button)
        Functions.write_data(self, selector_username, username)
        Functions.write_data(self, selector_password, password)
        Functions.click(self, selector_button)