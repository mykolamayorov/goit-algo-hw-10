import pulp

# Створення проблеми максимізації
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішень: кількість виробленого Лимонаду (x) і Фруктового соку (y)
x = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
y = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Цільова функція: максимізувати загальну кількість продукції
model += x + y, "Total_Production"

# Обмеження по ресурсах:
# Вода: 2x + 1y <= 100
model += 2 * x + 1 * y <= 100, "Water_Constraint"

# Цукор: 1x <= 50
model += 1 * x <= 50, "Sugar_Constraint"

# Лимонний сік: 1x <= 30
model += 1 * x <= 30, "Lemon_Juice_Constraint"

# Фруктове пюре: 2y <= 40
model += 2 * y <= 40, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Статус:", pulp.LpStatus[model.status])
print("Кількість Лимонаду:", int(x.varValue))
print("Кількість Фруктового соку:", int(y.varValue))
print("Загальна кількість продукції:", int(pulp.value(model.objective)))