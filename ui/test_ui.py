"""
Модуль с UI-тестами с сайта reqres.in.
"""
import json
import pytest
import requests
from requests import Response
from selenium.webdriver import Chrome
from ui.pages.main_page import MainPage


class TestReqresUI(MainPage):
    """
    Класс с UI-тестами главной страницы reqres.in.
    """

    @pytest.mark.parametrize(
        "delay_in_seconds, url", [(1, '/api/users?page=2')])
    def test_list_users_returns_200(
            self, delay_in_seconds: int,
            create_driver_session: Chrome, url: str) -> None:
        """
        Тест-кейс, проверяющий, что в методе List Users в UI и API
        возвращается статус-код 200, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API через requests
        api: Response = requests.get(
            f"{self.site}{url}", timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API через UI
        self.call_list_users(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url

    @pytest.mark.parametrize(
        "delay_in_seconds, url", [(1, '/api/users/2')])
    def test_single_user_returns_200(
            self, delay_in_seconds: int,
            create_driver_session: Chrome, url: str) -> None:
        """
        Тест-кейс, проверяющий, что в методе Single User в UI и API возвращается статус-код 200,
        совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API через requests
        api: Response = requests.get(
            f"{self.site}{url}", timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API через UI
        self.call_single_user(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url

    @pytest.mark.parametrize(
        "delay_in_seconds, url", [(1, "/api/users/23")])
    def test_single_user_returns_404(
            self, delay_in_seconds: int,
            create_driver_session: Chrome, url: str) -> None:
        """
        Тест-кейс, проверяющий, что в методе List Users в UI и API
        возвращается статус-код 404, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API в requests
        api: Response = requests.get(
            f"{self.site}{url}", timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_single_user_404(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url

    @pytest.mark.parametrize(
        "delay_in_seconds, url", [(1, "/api/unknown")])
    def test_get_resources_list_returns_200(
            self, delay_in_seconds: int,
            create_driver_session: Chrome, url: str) -> None:
        """
        Тест-кейс, проверяющий, что в методе Get Resources в UI и API возвращается статус-код 200,
        совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API через requests
        api: Response = requests.get(
            f"{self.site}{url}", timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_resources_list(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url

    @pytest.mark.parametrize(
        "delay_in_seconds, url", [(1, "/api/unknown/2")])
    def test_get_single_resource_returns_200(
            self, delay_in_seconds: int,
            create_driver_session: Chrome, url: str) -> None:
        """
        Тест-кейс, проверяющий, что в методе Single Resource в UI и API
        возвращается статус-код 200, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API через requests
        api: Response = requests.get(
            f"{self.site}{url}", timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_single_resource(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url

    @pytest.mark.parametrize(
        "delay_in_seconds, url", [(1, "/api/unknown/23")])
    def test_get_single_resource_returns_404(
            self, delay_in_seconds: int,
            create_driver_session: Chrome, url: str) -> None:
        """
        Тест-кейс, проверяющий, что в методе Single Resource в UI и API
        возвращается статус-код 404, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API через requests
        api: Response = requests.get(
            f"{self.site}{url}", timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_single_resource_404(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url

    @pytest.mark.parametrize(
        "delay_in_seconds, url, request_data",
        [(1, "/api/users", {"name": "morpheus", "job": "leader"})])
    def test_create_user_returns_200(
            self, delay_in_seconds: int, create_driver_session: Chrome,
            url: str, request_data: dict) -> None:
        """
        Тест-кейс, проверяющий, что в методе Create в UI и API
        возвращается статус-код 200, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API через requests
        api_request: str = json.dumps(request_data, indent=4)
        api: Response = requests.post(
            f"{self.site}{url}", json=request_data, timeout=10)
        api_response: dict = api.json()
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_create_user(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        request_body: str = self.parse_request_body(create_driver_session)
        ui_response: dict = json.loads(self.parse_response_body(create_driver_session))
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response["name"] == ui_response["name"]
        assert api_response["job"] == ui_response["job"]
        assert api_response["id"] is not None
        assert ui_response["id"] is not None
        assert api_response["createdAt"] is not None
        assert ui_response["createdAt"] is not None
        assert request_url == url
        assert api_request == request_body

    @pytest.mark.parametrize(
        "delay_in_seconds, url, request_data",
        [(1, "/api/users/2", {"name": "morpheus", "job": "zion resident"})])
    def test_update_user_returns_200(
            self, delay_in_seconds: int,
            create_driver_session: Chrome,
            url: str, request_data: dict) -> None:
        """
        Тест-кейс, проверяющий, что в методе Update в UI и API
        возвращается статус-код 200, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :param request_data: dict
        :return: None
        """

        # Вызов API через requests
        api_request: str = json.dumps(request_data, indent=4)
        api: Response = requests.put(
            f"{self.site}{url}", json=request_data, timeout=10)
        api_response: dict = api.json()
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_update_user(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        request_body: str = self.parse_request_body(create_driver_session)
        ui_response: dict = json.loads(self.parse_response_body(create_driver_session))
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response["name"] == ui_response["name"]
        assert api_response["job"] == ui_response["job"]
        assert api_response["updatedAt"] is not None
        assert ui_response["updatedAt"] is not None
        assert request_url == url
        assert api_request == request_body

    @pytest.mark.parametrize(
        "delay_in_seconds, url, request_data",
        [(1, "/api/users/2", {"name": "morpheus", "job": "zion resident"})])
    def test_patch_user_returns_200(
            self, delay_in_seconds: int,
            create_driver_session: Chrome,
            url: str, request_data: dict) -> None:
        """
        Тест-кейс, проверяющий, что в методе Patch в UI и API
        возвращается статус-код 200, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :param request_data: dict
        :return: None
        """

        # Вызов API через requests
        api_request: str = json.dumps(request_data, indent=4)
        api: Response = requests.patch(
            f"{self.site}{url}", json=request_data, timeout=10)
        api_response: dict = api.json()
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_patch_user(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        request_body: str = self.parse_request_body(create_driver_session)
        ui_response: dict = json.loads(self.parse_response_body(create_driver_session))
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response["name"] == ui_response["name"]
        assert api_response["job"] == ui_response["job"]
        assert api_response["updatedAt"] is not None
        assert ui_response["updatedAt"] is not None
        assert request_url == url
        assert api_request == request_body

    @pytest.mark.parametrize(
        "delay_in_seconds, url",
        [(1, "/api/users/2")])
    def test_delete_user_returns_200(
            self, delay_in_seconds: int,
            create_driver_session: Chrome, url: str) -> None:
        """
        Тест-кейс, проверяющий, что в методе Delete в UI и API
        возвращается статус-код 200, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :return: None
        """

        # Вызов API через requests
        api: Response = requests.delete(
            f"{self.site}{url}", timeout=10)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_delete_user(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert request_url == url

    @pytest.mark.parametrize(
        "delay_in_seconds, url, request_data",
        [(1, "/api/register", {"email": "eve.holt@reqres.in", "password": "pistol"})]
    )
    def test_user_register_returns_200(
            self, delay_in_seconds: int, create_driver_session: Chrome,
            url: str, request_data: dict) -> None:
        """
        Тест-кейс, проверяющий, что в методе User register в UI и API
        возвращается статус-код 200, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :param request_data: dict
        :return: None
        """

        # Вызов API через requests
        api_request: str = json.dumps(request_data, indent=4)
        api: Response = requests.post(
            f"{self.site}{url}", json=request_data, timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_successful_user_register(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        request_body: str = self.parse_request_body(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url
        assert api_request == request_body

    @pytest.mark.parametrize(
        "delay_in_seconds, url, request_data",
        [(1, "/api/register", {"email": "sydney@fife"})]
    )
    def test_user_register_returns_400(
            self, delay_in_seconds: int,
            create_driver_session: Chrome,
            url: str, request_data: dict) -> None:
        """
        Тест-кейс, проверяющий, что в методе User register в UI и API
        возвращается статус-код 400, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :param request_data: dict
        :return: None
        """

        # Вызов API через requests
        api_request: str = json.dumps(request_data, indent=4)
        api: Response = requests.post(
            f"{self.site}{url}", json=request_data, timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_unsuccessful_user_register(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        request_body: str = self.parse_request_body(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url
        assert api_request == request_body

    @pytest.mark.parametrize(
        "delay_in_seconds, url, request_data",
        [(1, "/api/login", {"email": "eve.holt@reqres.in", "password": "cityslicka"})]
    )
    def test_user_login_returns_200(
            self, delay_in_seconds: int, create_driver_session: Chrome,
            url: str, request_data: dict) -> None:
        """
        Тест-кейс, проверяющий, что в методе User login в UI и API возвращается статус-код 200,
        совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :param request_data: dict
        :return: None
        """

        # Вызов API через requests
        api_request: str = json.dumps(request_data, indent=4)
        api: Response = requests.post(
            f"{self.site}{url}", json=request_data, timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_successful_user_login(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        request_body: str = self.parse_request_body(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url
        assert api_request == request_body

    @pytest.mark.parametrize(
        "delay_in_seconds, url, request_data",
        [(1, "/api/login", {"email": "peter@klaven"})]
    )
    def test_user_login_returns_400(
            self, delay_in_seconds: int, create_driver_session: Chrome,
            url: str, request_data: dict) -> None:
        """
        Тест-кейс, проверяющий, что в методе User login в UI и API
        возвращается статус-код 400, совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url: str
        :param request_data: dict
        :return: None
        """

        # Вызов API через requests
        api_request: str = json.dumps(request_data, indent=4)
        api: Response = requests.post(
            f"{self.site}{url}", json=request_data, timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_unsuccessful_user_login(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        request_body: str = self.parse_request_body(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url
        assert api_request == request_body

    @pytest.mark.parametrize(
        "url_delay, delay_in_seconds, url",
        [(3, 4, f"/api/users?delay=")]
    )
    def test_user_list_returns_200_with_delay(
            self,
            create_driver_session: Chrome,
            url_delay: int,
            delay_in_seconds: int,
            url: str
    ) -> None:
        """
        Тест-кейс, проверяющий, что в методе List Users в UI и API возвращается статус-код 200,
        совпадают тела ответа с UI и API.
        :param delay_in_seconds: int
        :param create_driver_session: Chrome
        :param url_delay: int
        :param url: str
        :return: None
        """

        # Вызов API через requests
        url = f"{url}{url_delay}"
        api: Response = requests.get(
            f"{self.site}{url}", timeout=10)
        api_response: str = json.dumps(api.json(), indent=4)
        api_response_delay: int = int(api.elapsed.total_seconds())
        api_response_status_code: int = api.status_code

        # Вызов API в UI
        self.call_list_users_with_delay(create_driver_session, delay=delay_in_seconds)
        request_url: str = self.parse_request_url(create_driver_session)
        ui_response: str = self.parse_response_body(create_driver_session)
        ui_response_status_code: int = self.parse_response_status_code(create_driver_session)

        assert api_response_status_code == ui_response_status_code
        assert api_response == ui_response
        assert request_url == url
        assert api_response_delay == url_delay
