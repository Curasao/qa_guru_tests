from pprint import pprint
from datetime import time

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    current_time = time(hour=23)
    if 22 <= current_time.hour or current_time.hour < 6:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """

    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    elif 22 <= current_time.hour or current_time.hour < 6:
        is_dark_theme = True
    else:
        is_dark_theme = False



def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    # TODO найдите пользователя с именем "Olga"
    # решение без цикла
    suitable_users = None
    suitable_users = (users[3])
    # решение с циклом
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет

    suitable_users = None
    suitable_users = list(filter(lambda user: user["age"] < 20, users))
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]



def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def readable_name_and_args(func, *args):
    readable_name = func.__name__.replace('_', ' ').title() # Преобразование имени функции: заменяем "_" пробелами и делаем буквы заглавными

    args_list = []  # Объединение переданных аргументов в строку, используя цикл
    for arg in args:
        args_list.append(str(arg))  # Преобразование каждого аргумента в строку
    args_name = ", ".join(args_list)  # Объединение всех аргументов через запятую

    print(f"{readable_name} [{args_name}]")
    return f"{readable_name} [{args_name}]"   # Возвращаем строку вместо print

def open_browser(browser_name):
    actual_result = readable_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = readable_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = readable_name_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"