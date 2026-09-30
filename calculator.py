def calculate_total(price, quantity):
    return round(price * quantity, 2)


def calculate_discount(total, percentage):
    return total * (percentage / 100)


def calculate_final_price(price, quantity, discount_percentage):
    total = calculate_total(price, quantity)
    discount = calculate_discount(total, discount_percentage)

    return total - discount