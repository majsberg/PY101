money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

# Количество итераций равно количеству месяцев, когда подушка безопасности + ежемесячная зарплата превышают расходы

month = 1
while money_capital > spend:
    if month > 1:
        spend = spend + spend * increase
    money_capital = money_capital + salary - spend
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
