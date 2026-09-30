from user_service import get_user
from calculator import calculate_final_price


def create_order(user_id, price, quantity, discount_percentage):
    user = get_user(user_id)

    if not user:
        return None

    final_price = calculate_final_price(
        price,
        quantity,
        discount_percentage
    )

    return {
        "user_id": user.user_id,
        "user_name": user.name,
        "total": final_price,
    }


def print_order(user_id, price, quantity, discount_percentage):
    order = create_order(
        user_id,
        price,
        quantity,
        discount_percentage
    )

    print(order)