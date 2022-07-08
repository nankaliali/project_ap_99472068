# signupcustomer.py
from signupadmin import SignUpAdmin

class SignUpCustomer(SignUpAdmin):

    def __init__(self, user_name, password, first_name, last_name, phone_number, profile_name):
        """Initialize SingUp's attribiutes."""
        super().__init__(user_name, password)
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.profile_name = profile_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return  self._phone_number



    @first_name.setter
    def first_name(self, val):
        if  val.isdigit():
            raise ValueError('The first name contains number')   # If name = 'ali2'  --> raise ValueError
        if len(val) == 0:
            raise ValueError('First name must have at least one letter!')   # If name = ''  --> raise ValueError
        self._first_name = val

    @last_name.setter
    def last_name(self, val):
        if val.isdigit():
            raise ValueError('The last name contains number')  # If name = 'ali2'  --> raise ValueError
        if len(val) == 0:
            raise ValueError('Last name must have at least one letter!')  # If name = ''  --> raise ValueError

        self._last_name = val

    @phone_number.setter
    def phone_number(self, val):
        if not val.isdigit():
            raise ValueError('The last phone number contains letter')  # If name = 'ali2'  --> raise ValueError
        if len(val) == 0:
            raise ValueError('Phone number must have at least one letter!')  # If name = ''  --> raise ValueError

        self._phone_number = val



    def save_user_information(self):
        """Save user ingormation in foramt jason"""
        import json
        dictionary = {
            "user name": self.user_name,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "profile_name": self.profile_name
        }
        with open(f"F:\\project_ap_99472068\\Users_information\\customer\\{self.user_name}.json", "w") as outfile:
            json.dump(dictionary, outfile)

    def check_username_doesnt_exist(self):
        """Check that the username is not already registered"""
        import os.path

        file_exists = os.path.exists(f"F:\\project_ap_99472068\\"
                                     f"Users_information\\customer\\{self.user_name}.json")  # You can registere -->  True
        return not (file_exists)


    def __repr__(self):
            """Return string representation for repr()."""
            return (f"SignUpCustomer:\n"
                    f"{'user_name :':16}{self.user_name:<10}\n"
                    f"{'password :':16}{self.password:<10}\n"
                    f"{'first_name :':16}{self.first_name:<10}\n"
                    f"{'last_name :':16}{self.last_name:<10}\n"
                    f"{'phone_number :':16}{self.phone_number:<10}\n"
                    f"{'profile_name :':16}{self.profile_name:<10}")



s1 = SignUpCustomer('salim1', '8525', 'naeem', 'mohses','123456' ,'adafewewf')
print(s1)


