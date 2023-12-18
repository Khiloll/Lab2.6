def main():
    # Ввод данных с клавиатуры
    routes = []
    n = int(input("Введите количество маршрутов: "))
    for _ in range(n):
        route = {}
        route['название начального пункта маршрута'] = input("Введите название начального пункта маршрута: ")
        route['название конечного пункта маршрута'] = input("Введите название конечного пункта маршрута: ")
        route['номер маршрута'] = int(input("Введите номер маршрута: "))
        routes.append(route)

    # Сортировка по номерам маршрутов
    sorted_routes = sorted(routes, key=lambda x: x['номер маршрута'])

    # Вывод на экран информации о маршрутах
    start_end_point = input("Введите название пункта: ")
    found = False
    for route in sorted_routes:
        if route['название начального пункта маршрута'] == start_end_point or route['название конечного пункта маршрута'] == start_end_point:
            print("Маршрут:", route)
            found = True

    if not found:
        print("Нет маршрутов, начинающихся или заканчивающихся в указанном пункте.")


if __name__ == "__main__":
    main()
