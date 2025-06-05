flat_number = int(input("Введіть номер квартири: "))

entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1

print("Під'їзд:", entrance_number)
print("Поверх:", floor_number)