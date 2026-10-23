product_name = "манго"
price_per_kg = "187"
weight = "43"
user_money = "8041"
cost = int(price_per_kg) * int(weight)
change = int(user_money) - int(cost)
print(f"================Чек================")
print(f"Товар: {product_name:>28}")
print(f"Цена: {f'{weight}кг * {price_per_kg}руб/кг':>29}")
print(f"Итого: {cost:>25}руб")
print(f"Внесено: {user_money:>23}руб")
print(f"Сдача: {change:>25}руб")
print("===================================")