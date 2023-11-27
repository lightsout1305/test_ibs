"""
Модуль с фикстурами для API-тестов.
"""
import os
import pytest


@pytest.fixture(scope='session', autouse=True)
def create_test_emails() -> None:
    """
    Фикстура для создания тестового файла с email.
    :return: None
    """
    email_list: list[str] = \
        ["george.bluth@reqres.in\n", "janet.weaver@reqres.in\n", "emma.wong@reqres.in\n",
         "eve.holt@reqres.in\n", "charles.morris@reqres.in\n", "tracey.ramos@reqres.in\n",
         "michael.lawson@reqres.in\n", "lindsay.ferguson@reqres.in\n", "tobias.funke@reqres.in\n",
         "byron.fields@reqres.in\n", "george.edwards@reqres.in\n", "rachel.howell@reqres.in\n"
         ]

    with open('api/test_data/email_list.txt', 'w') as email_file:
        email_file.writelines(email_list)


@pytest.fixture(scope='session', autouse=True)
def create_test_first_names() -> None:
    """
    Фикстура для создания тестового файла с именами.
    :return: None
    """
    first_names_list: list[str] = \
        ["George\n", "Janet\n", "Emma\n", "Eve\n", "Charles\n", "Tracey\n",
         "Michael\n", "Lindsay\n", "Tobias\n", "Byron\n", "George\n", "Rachel\n",
         ]
    with open('api/test_data/first_name_list.txt', 'w') as first_name_file:
        first_name_file.writelines(first_names_list)


@pytest.fixture(scope='session', autouse=True)
def create_test_last_names() -> None:
    """
    Фикстура для создания тестового файла с фамилиями.
    :return: None
    """
    last_names_list: list[str] = \
        ["Bluth\n", "Weaver\n", "Wong\n", "Holt\n", "Morris\n", "Ramos\n",
         "Lawson\n", "Ferguson\n", "Funke\n", "Fields\n", "Edwards\n", "Howell\n",
         ]
    with open('api/test_data/last_name_list.txt', 'w') as last_name_file:
        last_name_file.writelines(last_names_list)


@pytest.fixture(scope='session', autouse=True)
def create_test_avatars() -> None:
    """
    Фикстура для создания тестового файла с URL аватаров.
    :return: None
    """
    avatars_list: list[str] = \
        ["https://reqres.in/img/faces/1-image.jpg\n", "https://reqres.in/img/faces/2-image.jpg\n",
         "https://reqres.in/img/faces/3-image.jpg\n", "https://reqres.in/img/faces/4-image.jpg\n",
         "https://reqres.in/img/faces/5-image.jpg\n", "https://reqres.in/img/faces/6-image.jpg\n",
         "https://reqres.in/img/faces/7-image.jpg\n", "https://reqres.in/img/faces/8-image.jpg\n",
         "https://reqres.in/img/faces/9-image.jpg\n", "https://reqres.in/img/faces/10-image.jpg\n",
         "https://reqres.in/img/faces/11-image.jpg\n", "https://reqres.in/img/faces/12-image.jpg\n",
         ]
    with open("api/test_data/avatars_list.txt", "w") as avatars_file:
        avatars_file.writelines(avatars_list)


@pytest.fixture(scope='session', autouse=True)
def create_test_flower_names() -> None:
    """
    Фикстура для создания тестового файла с названиями цветов.
    :return: None
    """
    flowers_list: list[str] = \
        ["cerulean\n", "fuchsia rose\n", "true red\n", "aqua sky\n", "tigerlily\n", "blue turquoise\n",
         "sand dollar\n", "chili pepper\n", "blue iris\n", "mimosa\n", "turquoise\n", "honeysuckle\n"]
    with open("api/test_data/flowers_list.txt", "w") as flowers_file:
        flowers_file.writelines(flowers_list)


@pytest.fixture(scope='session', autouse=True)
def create_test_colors() -> None:
    """
    Фикстура для создания тестового файла с цветами.
    :return: None
    """
    colors_list: list[str] = \
        ["#98B2D1\n", "#C74375\n", "#BF1932\n", "#7BC4C4\n", "#E2583E\n", "#53B0AE\n",
         "#DECDBE\n", "#9B1B30\n", "#5A5B9F\n", "#F0C05A\n", "#45B5AA\n", "#D94F70\n"]
    with open("api/test_data/colors_list.txt", 'w') as colors_file:
        colors_file.writelines(colors_list)


@pytest.fixture(scope='session', autouse=True)
def create_test_pantone_values() -> None:
    """
    Фикстура для создания тестового файла с пантонами.
    :return: None
    """
    pantone_values_list: list[str] = \
        ["15-4020\n", "17-2031\n", "19-1664\n", "14-4811\n", "17-1456\n", "15-5217\n",
         "13-1106\n", "19-1557\n", "18-3943\n", "14-0848\n", "15-5519\n", "18-2120\n"]
    with open("api/test_data/pantone_values_list.txt", 'w') as pantone_values_file:
        pantone_values_file.writelines(pantone_values_list)


@pytest.fixture(scope='session', autouse=True)
def add_test_directory() -> None:
    """
    Фикстура для создания тестовой директории.
    :return: None
    """
    _ = os.mkdir('api/test_data') if not os.path.exists('api/test_data') else None
