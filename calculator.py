def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total, percentage):
    return total * (percentage / 10)


def calculate_final_price(price, quantity, discount_percentage):
    total = calculate_total(price, quantity)
    discount = calculate_discount(total, discount_percentage)

    return total - discount