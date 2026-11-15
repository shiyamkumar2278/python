"""TASK 5 – Functions, Parameters and Scope
Problem Context: College Canteen Order System
"""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


def add(a, b):
    return a + b


def customer(name, item):
    print(name, item)


def order_item(item, quantity=1):
    print(item, quantity)


def calculate_bill(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst


def customer_counter():
    count = 0

    def add_customer():
        nonlocal count
        count += 1
        return count

    return add_customer


def create_order():
    order = []

    def add_to_order(item):
        order.append(item)
        return order

    return add_to_order


if __name__ == "__main__":
    print("Mutable Default Parameter Bug")
    print(add_item_buggy("Tea"))
    print(add_item_buggy("Vada"))

    print("\\nCorrected Function Using None")
    print(add_item("Tea"))
    print(add_item("Vada"))

    print("\\nComplete Code Comparison")
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print(add_item("Tea"), add_item("Vada"))
    print("Default list:", add_item_buggy.__defaults__)

    print("\\nPositional Parameters")
    print(add(10, 20))

    print("\\nKeyword Parameters")
    customer(item="Tea", name="Arun")

    print("\\nDefault Parameters")
    order_item("Tea")
    order_item("Coffee", 2)

    print("\\nReturning Multiple Values")
    total, gst = calculate_bill(1000)
    print("GST:", gst)
    print("Total:", total)

    print("\\nLocal Variable")
    def calculate():
        amount = 100
        print(amount)
    calculate()

    print("\\nGlobal Variable")
    total_orders = 0

    def show_orders():
        print(total_orders)

    def add_order():
        global total_orders
        total_orders += 1

    show_orders()
    add_order()
    print(total_orders)

    print("\\nNonlocal Variable")
    counter = customer_counter()
    print(counter())
    print(counter())

    print("\\nTesting with Three Customers")
    customer1 = add_item("Tea")
    customer1 = add_item("Vada", customer1)
    customer2 = add_item("Coffee")
    customer3 = add_item("Sandwich")
    print("Customer 1:", customer1)
    print("Customer 2:", customer2)
    print("Customer 3:", customer3)

    print("\\nAlternative – Explicit List")
    customer1 = []
    customer2 = []
    add_item("Tea", customer1)
    add_item("Coffee", customer2)
    print(customer1)
    print(customer2)

    print("\\nAlternative – Closure")
    customer1 = create_order()
    customer2 = create_order()
    print(customer1("Tea"))
    print(customer2("Coffee"))
