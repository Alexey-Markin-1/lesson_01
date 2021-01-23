        a = int(input("Введите расстояние пробежки первого дня в км "))
b = int(input("Введите общее желаемое расстояние в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Все получится на %.d день, при условии увеличения нагрузки на 10 процентов ежедневно" % result_days)
