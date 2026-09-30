def calculate_total(price, quantity, tax_percentage):
    tax_percent = price * quantity * (tax_percentage / 100)
    return (price * quantity) + tax_percent


def calculate_discount(total, percentage):
    return total * (percentage / 1000)


def calculate_final_price(price, quantity, discount_percentage):
    total = calculate_total(price, quantity)
    discount = calculate_discount(total, discount_percentage)

    return (total - discount)