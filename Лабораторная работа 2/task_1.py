money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital >= 0:
    if months > 0:
        spend += spend * increase

    budget = money_capital + salary

    if budget < spend:
        break

    money_capital = budget - spend
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)