# choosefood.py
from datetime import date
import json
class ChooseFood:
    day_today= int(date.today().strftime("%d"))
    month_today = int(date.today().strftime("%m"))
    year_today = int(date.today().strftime("%Y"))

    def __init__(self,day, month, year,user_name):
        self.year = year
        self.month = month
        self.day = day
        self.date = f"{(self.year)}/{self.month:02d}/{self.day:02d}"
        self.username = user_name

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, val):
        self._year = val

    @month.setter
    def month(self, val):
        if val > 12 or val < 1:
            raise ValueError("We only have 12 months a year.")
        self._month = val

    @day.setter
    def day(self, val):
        if 0 < self.month < 7:
            if val>31 or val < 1:
                raise ValueError('The first 6 months of the year have 31 days')

        if 6 < self.month < 13:
            if val>30 or val < 1:
                raise ValueError('The first 6 months of the year have 30 days')

        self._day = val

    def display_food(self):
        name_file = self.date.replace('/','.')
        with open(f"F:\\project_ap_99472068\\Food_information\\{name_file}.json", 'r') as accounts:
            food_data = json.dumps(json.load(accounts), indent=4)
        return food_data



    @staticmethod
    def tabdil_miladi_be_shamsi(day, month, year):

        return f"{year:02d}/{month:02d}/{day:02d}"





    def check_the_expiratio_date(self):
        day_today = int(date.today().strftime("%d"))
        month_today = int(date.today().strftime("%m"))
        year_today = int(date.today().strftime("%Y"))

        today_time = str(ChooseFood.tabdil_miladi_be_shamsi(day_today, month_today, year_today))  # date_time_today_shamsi convert to a integer
        today_time = today_time.split('/')                                                        # 1401-04-01 --> 14010401
        today_time = int(''.join(today_time))

        user_selected_date = int(self.date.replace('/',''))

        if user_selected_date >= today_time:
            return True   # The date is valid
        return False

    def save_orders(self ,name_food, numbers_of_orders,cost_each_food):
        """Sace orders in json file.
           dictionary_orders = {"name_food": {cost_each_food:---, number_of_foods:---, Total payment:---}
        """
        import os.path

        self.newpath = f'F:\\project_ap_99472068\\orders\\{self.username}'
        if  os.path.exists(self.newpath) == False:
            os.makedirs(self.newpath)

        name_file = self.date.replace('/', '.')
        dictionary_orders = {name_food: {"numbers of orders": numbers_of_orders, "cost each food": cost_each_food, "payment": cost_each_food*numbers_of_orders}}

        file_exists = os.path.exists(f"{self.newpath}\\{name_file}.json")

        if file_exists:
            a_file = open(f"{self.newpath}\\{name_file}.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            try:
                json_object[name_food]["numbers of orders"] += numbers_of_orders
                json_object[name_food]["payment"] += numbers_of_orders * cost_each_food

            except:
                json_object[name_food] = {"numbers of orders": numbers_of_orders, "cost each food": cost_each_food, "payment": 2000*numbers_of_orders}

            a_file = open(f"{self.newpath}\\{name_file}.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

        else:
            with open(f"{self.newpath}\\{name_file}.json", "w") as outfile:
                json.dump(dictionary_orders, outfile)

    def select_food(self, name_food, number_of_orders):
        name_file = self.date.replace('/', '.')

        a_file = open(f"F:\\project_ap_99472068\\Food_information\\{name_file}.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        if json_object[name_food]['number_of_foods_available'] - number_of_orders >= 0:
            json_object[name_food]['number_of_foods_available'] -= number_of_orders
        else:
            raise Exception(f"We only have {json_object[name_food]['number_of_foods_available']} {name_food}"
                            f", but you have ordered up to {number_of_orders} {name_food}!")
        self.cost_each_food = json_object[name_food]["cost_food"]

        a_file = open(f"F:\\project_ap_99472068\\Food_information\\{name_file}.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
        self.save_orders(name_food, number_of_orders, self.cost_each_food)


    def __repr__(self):
        return f"ChoosFood( '{self.date}' )"
'''


c1 = ChooseFood(14,4,1401,'salim6')
c1.select_food('makaroni', 10)
'''