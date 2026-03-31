users = []

# Регистрация
def register(email, password):
    if email == "" or password == "":
        return "Ошибка: заполните все поля"

    for user in users:
        if user["email"] == email:
            return "Ошибка: пользователь уже существует"

    users.append({"email": email, "password": password})
    return "Регистрация успешна"


# Авторизация
def login(email, password):
    for user in users:
        if user["email"] == email and user["password"] == password:
            return "Вход выполнен"

    return "Ошибка: неверные данные"


# ---------- ТЕСТЫ ----------
def run_tests():
    print("Запуск тестов...\n")

    users.clear()
    result = register("test@mail.com", "1234")
    print("Тест 1 (регистрация):", "OK" if result == "Регистрация успешна" else "FAIL")

    result = register("test@mail.com", "1234")
    print("Тест 2 (дубликат):", "OK" if result == "Ошибка: пользователь уже существует" else "FAIL")

    result = register("", "")
    print("Тест 3 (пустые поля):", "OK" if result == "Ошибка: заполните все поля" else "FAIL")

    users.clear()
    register("user@mail.com", "1234")
    result = login("user@mail.com", "1234")
    print("Тест 4 (вход):", "OK" if result == "Вход выполнен" else "FAIL")

    result = login("wrong@mail.com", "0000")
    print("Тест 5 (неверный вход):", "OK" if result == "Ошибка: неверные данные" else "FAIL")


# запуск тестов
run_tests()