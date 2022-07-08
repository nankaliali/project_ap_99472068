# signupcustomer.py

class SignUpAdmin:

    def __init__(self, user_name, password):
        """Initialize SingUp's attribiutes."""
        self.user_name = user_name
        self.password = password


    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @user_name.setter
    def user_name(self, val):
        """Set username or raise ValueError if invalid"""
        if len(val) == 0:
            raise ValueError("Username must have at least one letter! ")  # username = empty  --> invalid
        self._user_name = val

    @password.setter
    def password(self, val):
        """Set password or raise ValueError if invalid"""
        if len(val) == 0:
            raise ValueError("Password must have at least one letter!")  # password = empty  --> invalid
        if  not (val.isdigit()):   # If password = '1256' --> True
            raise ValueError('Password contains numbers only')         # If password = 'ali25' --> False
        self._password = val

    def save_user_information(self):
        """Save user ingormation in foramt jason"""
        import json
        dictionary = {
            "user name" : self.user_name,
            "password" : self.password,
                      }
        with open(f"F:\\project_ap_99472068\\Users_information\\admin\\{self.user_name}.json", "w") as outfile:
            json.dump(dictionary, outfile)

    def check_username_doesnt_exist(self):
        """Check that the username is not already registered"""
        import os.path

        file_exists = os.path.exists(f"F:\\project_ap_99472068\\"
                                     f"Users_information\\admin\\{self.user_name}.json")   # if username was not already registerd -->  True
        return not(file_exists)                                                               # if username was alreary registerd --> False --> enter another username

    def __repr__(self):
        """Return string representation for repr()."""
        return (f'SignUpAdmin:\n'
                f'user_name : {self.user_name}\n'
                f'password : {self.password}\n')







