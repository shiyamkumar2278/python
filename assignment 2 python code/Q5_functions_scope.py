global_count = 0

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def calculate_bill(items, gst_rate=0.05):
    subtotal = sum(items)
    gst = subtotal * gst_rate
    return subtotal, gst, subtotal + gst

def scope_demo():
    global global_count
    global_count += 1
    message = "outer"
    def inner():
        nonlocal message
        message = "changed by inner"
    inner()
    print("Nonlocal:", message, "| Global:", global_count)

if __name__ == "__main__":
    print("Buggy:", add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Stored default:", add_item_buggy.__defaults__)
    print("Correct:", add_item("Tea"), add_item("Vada"))
    c1 = add_item("Tea", [])
    c2 = add_item("Coffee", [])
    c3 = add_item("Juice", [])
    print("Customer orders:", c1, c2, c3)
    sub, gst, total = calculate_bill([20, 30, 40])
    print(f"Subtotal={sub:.2f}, GST={gst:.2f}, Total={total:.2f}")
    scope_demo()
