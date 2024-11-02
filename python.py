import random
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')


class Order:

    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.__order_id = order_id
        self.__customer_name = customer_name
        self.__order_date = order_date
        self.__total_amount = total_amount
        self.__tax = 0.0

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, new_order_id):
        self.__order_id = new_order_id

    @property
    def customer_name(self):
        return self.__customer_name
    
    @customer_name.setter
    def customer_name(self, new_customer_name):
        self.__customer_name = new_customer_name

    @property
    def order_date(self):
        return self.__order_date
    
    @order_date.setter
    def order_date(self, new_order_date):
        self.__order_date = new_order_date

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount):
        self.__total_amount = new_total_amount

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, new_tax):
        self.__tax = new_tax

    def calculate_tax(self, tax_rate):
        self.tax = (self.total_amount * tax_rate)/100
        # print("tax          :",locale.currency(self.tax,grouping=True))
    
    def display_order(self):
        print("----------------------------------------")
        print("Order ID     :", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Order Date   :", self.order_date)
        print("Total Amount :", locale.currency(self.total_amount, grouping=True))

class OrderProcessor(Order):

    def __init__(self):
        self.__order_list = [] 
    
    @property
    def order_list(self):
        return self.__order_list

    def add_order(self, Order):
        self.__order_list.append(Order)

    def calculate_total_revenue(self):
        total_revenue = 0
        for Order in self.__order_list:
            total_revenue += Order.total_amount

        print("Total Revenue:", locale.currency((total_revenue), grouping=True))

    def calculate_tax(self):
        total_tax = 0.0
        for Order in self.__order_list:
            total_tax += Order.tax

        print("Total Tax    :", locale.currency((total_tax), grouping=True))

    def display_order(self):
        print("========================================")
        print("             All ORDERS")
        print("========================================")
        
        for Order in self.__order_list:
            Order.display_order()

o1 = Order(1, "John", "12 Februari 2021", 500000)
o1.calculate_tax(random.random())

o2 = Order(2, "Natalie", "24 Maret 2012", 800000)
o2.calculate_tax(random.random())

o3 = Order(3, "Agus", "3 Juli 2017", 200000)
o3.calculate_tax(random.random())

o4 = Order(4, "Putri", "17 Agustus 2001", 900000)
o4.calculate_tax(random.random())

o5 = Order(5, "Bambang", "5 Oktober 2006", 1400000)
o5.calculate_tax(random.random())

op = OrderProcessor()
op.add_order(o1)
op.add_order(o2)
op.add_order(o3)
op.add_order(o4)
op.add_order(o5)

op.calculate_total_revenue()
op.calculate_tax()
op.display_order()

print(o1.customer_name)
print(o1.__customer_name)
