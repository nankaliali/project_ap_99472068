
import json
class CreateAccountCustomer:
    def __init__(self,first_name, last_name,user_name ,  phone_number, email, password, profile_address):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.profile_address = profile_address

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, val):
        import os
        if os.path.exists(f"F:\\project_ap_99472068\\Users_information\\customer\\{val}.json") == True:
            raise Exception("Your username has already been used !")
        self._user_name = val


    @property
    def profile_address(self):
        return self._profile_address

    @profile_address.setter
    def profile_address(self, val):
        if val == '':
            raise Exception("Drag your profile photo")
        else:
            val = val.split('///')
            self._profile_address = val[1]



    def save_information_json_file(self):
        import json
        from PIL import Image

        dict_information = {}
        dict_information["user name"] = self.user_name
        dict_information["first_name"] = self.first_name
        dict_information["last_name"] = self.last_name
        dict_information["phone_number"] = self.phone_number
        dict_information["Email"] = self.email
        dict_information["password"] = self.password
        dict_information["Profile"] = self.profile_address



        a_file = open(f"F:\\project_ap_99472068\\Users_information\\customer\\{self.user_name}.json", "w")
        json.dump(dict_information, a_file)
        a_file.close()


        picture = Image.open(self.profile_address)
        picture = picture.save(f"F:\\project_ap_99472068\\Users_information\\photo\\{self.user_name}.jpg")










