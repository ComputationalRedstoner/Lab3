import price_info

def test_fruit_cost():
    input_fruit = 'orange'
    input_quantity = 10
    total_cost = price_info.cost_of_fruits(input_fruit, input_quantity)
    if total_cost == 14:
        return 1
    assert (total_cost == 1)

def test_total_cost():
    price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95, 'pomegranate': 4.95}

    quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1, 'pomegranate': 2}

    total_cost = price_info.total_cost_shopping(price_list, quantity_list)
    if total_cost == 46.75:
        return 1
    assert (total_cost == 1)