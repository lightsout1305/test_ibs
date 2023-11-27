"""
Модуль с API-тестами с сайта reqres.in
"""
import requests
from requests import Response
import pytest


class TestReqresAPI:
    """
    Класс с тестами всех API с главной страницы Reqres.in.
    """
    reqres: str = "https://reqres.in"

    @pytest.mark.parametrize(
        "list_users_url, page, per_page, total, total_pages, "
        "ids, "
        "url, text",
        [("/api/users?page=1", 1, 6, 12, 2,
          [*range(1, 7)],
          "https://reqres.in/#support-heading",
          "To keep ReqRes free, contributions towards server costs are appreciated!"
          )])
    def test_list_users_on_first_page_returns_200(
            self,
            list_users_url: str,
            page: int,
            per_page: int,
            total: int,
            total_pages: int,
            ids: list[int],
            url: str,
            text: str
    ) -> None:
        """
        Тест-кейс, проверяющий, что метод List Users на первой странице
        возвращает 200, все поля и данные.
        :param list_users_url: str
        :param page: int
        :param per_page: int
        :param total: int
        :param total_pages: int
        :param ids: list[int]
        :param url: str
        :param text: str
        :return: None
        """
        emails: list[str] = \
            [email.rstrip() for email in open("api/test_data/email_list.txt")][:6]
        first_names: list[str] = \
            [first_name.rstrip() for first_name in open("api/test_data/first_name_list.txt")][:6]
        last_names: list[str] = \
            [last_name.rstrip() for last_name in open("api/test_data/last_name_list.txt")][:6]
        avatars: list[str] = \
            [avatar.rstrip() for avatar in open('api/test_data/avatars_list.txt')][:6]
        index: int = 0
        request: Response = requests.get(
            self.reqres + list_users_url, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["page"] == page
        assert request_json["per_page"] == per_page
        assert request_json["total"] == total
        assert request_json["total_pages"] == total_pages
        assert len(request_json) == per_page
        assert request_json["support"]["url"] == url
        assert request_json["support"]["text"] == text

        for data in request_json["data"]:
            assert data["id"] == ids[index]
            assert data["email"] == emails[index]
            assert data["first_name"] == first_names[index]
            assert data["last_name"] == last_names[index]
            assert data["avatar"] == avatars[index]
            index += 1

    @pytest.mark.parametrize(
        "list_users_url, page, per_page, total, total_pages, "
        "ids, "
        "url, text",
        [("/api/users?page=2", 2, 6, 12, 2,
          [*range(7, 13)],
          "https://reqres.in/#support-heading",
          "To keep ReqRes free, contributions towards server costs are appreciated!"
          )])
    def test_list_users_on_second_page_returns_200(
            self,
            list_users_url: str,
            page: int,
            per_page: int,
            total: int,
            total_pages: int,
            ids: list[int],
            url: str,
            text: str
    ) -> None:
        """
        Тест-кейс, проверяющий, что метод List Users на второй странице
        возвращает 200, все поля и данные.
        :param list_users_url: str
        :param page: int
        :param per_page: int
        :param total: int
        :param total_pages: int
        :param ids: list[int]
        :param url: str
        :param text: str
        :return: None
        """
        emails: list[str] = \
            [email.rstrip() for email in open("api/test_data/email_list.txt")][6:]
        first_names: list[str] = \
            [first_name.rstrip() for first_name in open("api/test_data/first_name_list.txt")][6:]
        last_names: list[str] = \
            [last_name.rstrip() for last_name in open("api/test_data/last_name_list.txt")][6:]
        avatars: list[str] = \
            [avatar.rstrip() for avatar in open('api/test_data/avatars_list.txt')][6:]
        index: int = 0
        request: Response = requests.get(
            self.reqres + list_users_url, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["page"] == page
        assert request_json["per_page"] == per_page
        assert request_json["total"] == total
        assert request_json["total_pages"] == total_pages
        assert len(request_json) == per_page
        assert request_json["support"]["url"] == url
        assert request_json["support"]["text"] == text

        for data in request_json["data"]:
            assert data["id"] == ids[index]
            assert data["email"] == emails[index]
            assert data["first_name"] == first_names[index]
            assert data["last_name"] == last_names[index]
            assert data["avatar"] == avatars[index]
            index += 1

    @pytest.mark.parametrize(
        "get_user_url, "
        "ids,"
        "url, text",
        [("api/users",
          [*range(1, 13)],
          "https://reqres.in/#support-heading",
          "To keep ReqRes free, contributions towards server costs are appreciated!"
          )])
    def test_single_user_returns_200(
            self,
            get_user_url: str,
            ids: list[int],
            url: str,
            text: str
    ) -> None:
        """
        Тест-кейс, проверяющий, что метод Single User возвращает 200, все поля и данные.
        :param get_user_url: str
        :param ids: list[int]
        :param url: str
        :param text: str
        :return: None
        """
        emails: list[str] = \
            [email.rstrip() for email in open("api/test_data/email_list.txt")]
        first_names: list[str] = \
            [first_name.rstrip() for first_name in open("api/test_data/first_name_list.txt")]
        last_names: list[str] = \
            [last_name.rstrip() for last_name in open("api/test_data/last_name_list.txt")]
        avatars: list[str] = \
            [avatar.rstrip() for avatar in open('api/test_data/avatars_list.txt')]
        index: int = 0
        for user_id in ids:
            request: Response = requests.get(
                f"{self.reqres}/{get_user_url}/{user_id}", timeout=10)
            request_json: dict = request.json()["data"]
            assert request.status_code == 200
            assert request_json["id"] == user_id
            assert request_json["email"] == emails[index]
            assert request_json["first_name"] == first_names[index]
            assert request_json["last_name"] == last_names[index]
            assert request_json["avatar"] == avatars[index]
            assert request.json()["support"]["url"] == url
            assert request.json()["support"]["text"] == text
            index += 1

    @pytest.mark.parametrize("get_user, user_id", [("api/users", 23)])
    def test_single_user_returns_404(self, get_user: str, user_id: int) -> None:
        """
        Тест-кейс, проверяющий, что метод Single User воз
        :param get_user: str
        :param user_id: int
        :return: None
        """
        request: Response = requests.get(
            f"{self.reqres}/{get_user}/{user_id}", timeout=10)
        assert request.status_code == 404

    @pytest.mark.parametrize(
        "get_list_resources, page, per_page, total, total_pages, "
        "ids, years, "
        "url, text", [
            ("api/unknown", 1, 6, 12, 2, [*range(1, 7)],
             [*range(2000, 2006)],
             "https://reqres.in/#support-heading",
             "To keep ReqRes free, contributions towards server costs are appreciated!"
             )])
    def test_resources_list_on_first_page_returns_200(
            self,
            get_list_resources: str,
            page: int,
            per_page: int,
            total: int,
            total_pages: int,
            ids: list[int],
            years: list[int],
            url: str,
            text: str
    ) -> None:
        """
        Тест-кейс, проверяющий, что метод Resources List на первой странице
        возвращает 200, все поля и данные.
        :param get_list_resources: str
        :param page: int
        :param per_page: int
        :param total: int
        :param total_pages: int
        :param ids: list[int]
        :param url: str
        :param text: str
        :return: None
        """
        flower_names: list[str] = \
            [flower.rstrip() for flower in open('api/test_data/flowers_list.txt')][:6]
        colors: list[str] = \
            [color.strip() for color in open('api/test_data/colors_list.txt')][:6]
        pantone_values: list[str] = \
            [pantone.strip() for pantone in open('api/test_data/pantone_values_list.txt')][:6]
        index: int = 0
        request: Response = requests.get(
            f"{self.reqres}/{get_list_resources}", timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["page"] == page
        assert request_json["per_page"] == per_page
        assert request_json["total"] == total
        assert request_json["total_pages"] == total_pages
        assert len(request_json["data"]) == per_page
        assert request_json["support"]["url"] == url
        assert request_json["support"]["text"] == text

        for data in request_json["data"]:
            assert data["id"] == ids[index]
            assert data["name"] == flower_names[index]
            assert data["year"] == years[index]
            assert data["color"] == colors[index]
            assert data["pantone_value"] == pantone_values[index]
            index += 1

    @pytest.mark.parametrize(
        "get_list_resources, page, per_page, total, total_pages, "
        "ids, years, "
        "url, text", [
            ("api/unknown?page=2", 2, 6, 12, 2, [*range(7, 13)],
             [*range(2006, 2012)],
             "https://reqres.in/#support-heading",
             "To keep ReqRes free, contributions towards server costs are appreciated!"
             )])
    def test_resources_list_on_second_page_returns_200(
            self,
            get_list_resources: str,
            page: int,
            per_page: int,
            total: int,
            total_pages: int,
            ids: list[int],
            years: list[int],
            url: str,
            text: str
    ) -> None:
        """
        Тест-кейс, проверяющий, что метод Resources List на второй странице
        возвращает 200, все поля и данные.
        :param get_list_resources: str
        :param page: int
        :param per_page: int
        :param total: int
        :param total_pages: int
        :param ids: list[int]
        :param url: str
        :param text: str
        :return: None
        """
        flower_names: list[str] = \
            [flower.rstrip() for flower in open('api/test_data/flowers_list.txt')][6:]
        colors: list[str] = \
            [color.strip() for color in open('api/test_data/colors_list.txt')][6:]
        pantone_values: list[str] = \
            [pantone.strip() for pantone in open('api/test_data/pantone_values_list.txt')][6:]
        index: int = 0
        request: Response = requests.get(
            f"{self.reqres}/{get_list_resources}", timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["page"] == page
        assert request_json["per_page"] == per_page
        assert request_json["total"] == total
        assert request_json["total_pages"] == total_pages
        assert len(request_json["data"]) == per_page
        assert request_json["support"]["url"] == url
        assert request_json["support"]["text"] == text

        for data in request_json["data"]:
            assert data["id"] == ids[index]
            assert data["name"] == flower_names[index]
            assert data["year"] == years[index]
            assert data["color"] == colors[index]
            assert data["pantone_value"] == pantone_values[index]
            index += 1

    @pytest.mark.parametrize(
        "get_resource, "
        "ids, years,"
        "url, text", [
            ("api/unknown", [*range(1, 13)],
             [*range(2000, 2012)],
             "https://reqres.in/#support-heading",
             "To keep ReqRes free, contributions towards server costs are appreciated!"
             )])
    def test_single_resource_returns_200(
            self,
            get_resource: str,
            ids: list[int],
            years: list[int],
            url: str,
            text: str
    ) -> None:
        """
        Тест-кейс, проверяющий, что метод Single Resource возвращает 200,
        все поля и данные.
        :param ids: list[int]
        :param url: str
        :param text: str
        :param years: list[int]
        :param get_resource: str
        :return: None
        """
        flower_names: list[str] = \
            [flower.rstrip() for flower in open('api/test_data/flowers_list.txt')]
        colors: list[str] = \
            [color.strip() for color in open('api/test_data/colors_list.txt')]
        pantone_values: list[str] = \
            [pantone.strip() for pantone in open('api/test_data/pantone_values_list.txt')]
        index: int = 0
        for resource_id in ids:
            request: Response = requests.get(
                f"{self.reqres}/{get_resource}/{resource_id}", timeout=10)
            request_json: dict = request.json()["data"]
            assert request.status_code == 200
            assert request_json["id"] == resource_id
            assert request_json["name"] == flower_names[index]
            assert request_json["color"] == colors[index]
            assert request_json["year"] == years[index]
            assert request_json["pantone_value"] == pantone_values[index]
            assert request.json()["support"]["url"] == url
            assert request.json()["support"]["text"] == text
            index += 1

    @pytest.mark.parametrize(
        "get_resource, resource_id", [("api/unknown", 23)])
    def test_single_resource_returns_404(
            self, get_resource: str, resource_id: int) -> None:
        """
        Тест-кейс, что метод Single Resource возвращает 404.
        :param get_resource: str
        :param resource_id: int
        :return: None
        """
        request: Response = requests.get(
            f"{self.reqres}/{get_resource}/{resource_id}", timeout=10)
        assert request.status_code == 404

    @pytest.mark.parametrize(
        "create_user, name, job", [("api/users", "Morphius", "Leader")])
    def test_create_user_returns_201(
            self, create_user: str, name: str, job: str) -> None:
        """
        Тест-кейс, проверяющий, что метод Create возвращает 201.
        :param create_user: str
        :param name: str
        :param job: str
        :return: None
        """
        data: dict = {
            "name": name,
            "job": job
        }
        request: Response = requests.post(
            f"{self.reqres}/{create_user}", json=data, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 201
        assert request_json["name"] == name
        assert request_json["job"] == job
        assert request_json["id"] is not None
        assert request_json["createdAt"] is not None
        assert isinstance(request_json["createdAt"], str)
        assert isinstance(request_json["id"], str)

    @pytest.mark.parametrize(
        "update_user, name, job, user_id",
        [("api/users", "Morphius", "Zion resident", 2)])
    def test_update_user_returns_200(
            self, update_user: str, name: str, job: str, user_id: int) -> None:
        """
        Тест-кейс, проверяющий, что метод Update возвращает 200.
        :param update_user: str
        :param name: str
        :param job: str
        :param user_id: int
        :return: None
        """
        data: dict = {
            "name": name,
            "job": job
        }
        request: Response = requests.put(
            f"{self.reqres}/{update_user}/{user_id}", json=data, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["name"] == name
        assert request_json["job"] == job
        assert request_json["updatedAt"] is not None
        assert isinstance(request_json["updatedAt"], str)

    @pytest.mark.parametrize("patch_user, name, user_id", [("api/users", "Penguin", 2)])
    def test_patch_user_returns_200(
            self, patch_user: str, name: str, user_id: int) -> None:
        """
        Тест-кейс, проверяющий, что метод Patch возвращает 200.
        :param patch_user: str
        :param name: str
        :param user_id: int
        :return: None
        """
        data: dict = {
            "name": name
        }
        request: Response = requests.patch(
            f"{self.reqres}/{patch_user}/{user_id}", json=data, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["name"] == name
        assert request_json["updatedAt"] is not None
        assert isinstance(request_json["updatedAt"], str)

    @pytest.mark.parametrize("delete_user, user_id", [("api/users", 2)])
    def test_delete_user_returns_204(self, delete_user: str, user_id: int) -> None:
        """
        Тест-кейс, проверяющий, что метод Delete возвращает 204.
        :param delete_user: str
        :param user_id: int
        :return: None
        """
        request: Response = requests.delete(
            f"{self.reqres}/{delete_user}/{user_id}", timeout=10)
        assert request.status_code == 204

    @pytest.mark.parametrize(
        "register_user, email, password",
        [("api/register", "eve.holt@reqres.in", "pistol")])
    def test_user_register_returns_200(
            self, register_user: str, email: str, password: str) -> None:
        """
        Тест-кейс, проверяющий, что метод User Register возвращает 200.
        :param register_user: str
        :param email: str
        :param password: str
        :return: None
        """
        data: dict = {
            "email": email,
            "password": password
        }
        request: Response = requests.post(
            f"{self.reqres}/{register_user}", json=data, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["id"] is not None
        assert isinstance(request_json["id"], int)
        assert request_json["token"] is not None
        assert isinstance(request_json["token"], str)

    @pytest.mark.parametrize(
        "register_user, email, error",
        [("api/register", "sydney@fife", "Missing password")])
    def test_user_register_returns_400(
            self, register_user: str, email: str, error: str) -> None:
        """
        Тест-кейс, проверяющий, что метод User Register возвращает 400.
        :param register_user: str
        :param email: str
        :param error: str
        :return: None
        """
        data: dict = {
            "email": email
        }
        request: Response = requests.post(
            f"{self.reqres}/{register_user}", json=data, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 400
        assert request_json["error"] == error

    @pytest.mark.parametrize(
        "login_user, email, password",
        [("api/login", "eve.holt@reqres.in", "cityslicka")])
    def test_user_login_returns_200(
            self, login_user: str, email: str, password: str) -> None:
        """
        Тест-кейс, проверяющий, что метод User Login возвращает 200.
        :param login_user: str
        :param email: str
        :param password: str
        :return: None
        """
        data: dict = {
            "email": email,
            "password": password
        }
        request: Response = requests.post(
            f"{self.reqres}/{login_user}", json=data, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 200
        assert request_json["token"] is not None
        assert isinstance(request_json["token"], str)

    @pytest.mark.parametrize(
        "login_user, email, error",
        [("api/login", "eve.holt@reqres.in", "Missing password")])
    def test_user_login_returns_400(
            self, login_user: str, email: str, error: str) -> None:
        """
        Тест-кейс, проверяющий, что метод User Login возвращает 400.
        :param login_user: str
        :param email: str
        :param error: str
        :return: None
        """
        data: dict = {
            "email": email
        }
        request: Response = requests.post(
            f"{self.reqres}/{login_user}", json=data, timeout=10)
        request_json: dict = request.json()
        assert request.status_code == 400
        assert request_json["error"] == error

    @pytest.mark.parametrize("get_users, delay", [("api/users?delay", 3)])
    def test_list_users_returns_200_in_3_seconds(
            self,
            get_users: str,
            delay: int
    ) -> None:
        """
        Тест-кейс, проверяющий, что метод List Users возвращает 200 с задержкой.
        :param get_users: str
        :param delay: int
        :return: None
        """
        request: Response = requests.get(
            f"{self.reqres}/{get_users}={delay}", timeout=10)
        assert int(request.elapsed.total_seconds()) == 3
        assert request.status_code == 200
