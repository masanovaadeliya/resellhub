from main import register, login, users 
def test_register_success():
    users.clear()
    result = register("test@mail.com", "1234")
    assert result == "Регистрация успешна"


def test_register_duplicate():
    users.clear()
    register("test@mail.com", "1234")
    result = register("test@mail.com", "1234")
    assert result == "Ошибка: пользователь уже существует"


def test_register_empty():
    result = register("", "")
    assert result == "Ошибка: заполните все поля"


def test_login_success():
    users.clear()
    register("user@mail.com", "1234")
    result = login("user@mail.com", "1234")
    assert result == "Вход выполнен"


def test_login_fail():
    result = login("wrong@mail.com", "0000")
    assert result == "Ошибка: неверные данные"