# cart.py
import os
import json
import pandas as pd

class Cart:

    def __init__(self, user_name):
        self.user_name = user_name


    def finalize_orders(self):
        factor = []
        file_address= f"F:\\project_ap_99472068\\orders\\{self.user_name}"
        file_exists = os.path.exists(file_address)

        if file_exists:
            for filename in os.listdir(file_address):
                with open(os.path.join(file_address, filename), 'r') as f:
                    json_object = json.load(f)
                    date_order = filename.removesuffix('.json')

                    for key in json_object:
                        factor.append(key)
                        for val in json_object[key].values():
                            factor.append(val)
                        factor.append(date_order)

                    print(factor)
            self.list_factor = []
            for index in range(0,len(factor),5):
                self.list_factor.append(factor[index:index+5])

            self.total_payment = 0
            for cost in self.list_factor:
                self.total_payment += cost[3]

            print(self.list_factor)

            factor_proper_display = pd.DataFrame(self.list_factor, columns = ['  Name Food', '   Number Food', 'Food Costs', 'PaYment', '  Date   '])

            print(factor_proper_display)
            print('-----------------------------------------------------------------------')
            print('                                             ',self.total_payment)

    @staticmethod
    def finalize_purchase():
        pass

    def payment(self):
        pass



c1 = Cart('salim20')
c1.finalize_orders()


