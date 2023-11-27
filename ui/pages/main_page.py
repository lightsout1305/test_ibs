"""
Модуль с объектом главной страницы reqres.in.
"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
    """
    Класс объекта главной страницы reqres.in.
    """
    site: str = "https://reqres.in"
    __list_users: str = "//li[@data-id='users']"
    __single_user: str = "//li[@data-id='users-single']"
    __user_not_found: str = "//li[@data-id='users-single-not-found']"
    __list_resources: str = "//li[@data-id='unknown']"
    __get_resource: str = "//li[@data-id='unknown-single']"
    __resource_not_found: str = "//li[@data-id='unknown-single-not-found']"
    __create_user: str = "//li[@data-id='post']"
    __update_user: str = "//li[@data-id='put']"
    __patch_user: str = "//li[@data-id='patch']"
    __delete_user: str = "//li[@data-id='delete']"
    __register_successful: str = "//li[@data-id='register-successful']"
    __register_unsuccessful: str = "//li[@data-id='register-unsuccessful']"
    __login_successful: str = "//li[@data-id='login-successful']"
    __login_unsuccessful: str = "//li[@data-id='login-unsuccessful']"
    __delay: str = "//li[@data-id='delay']"
    __request_body: str = "//pre[@data-key='output-request']"
    __request_url: str = "//span[@data-key='url']"
    __response_body: str = "//pre[@data-key='output-response']"
    __status_code: str = "//span[@data-key='response-code']"
    __spinner: str = "//div[@class='cube1']"

    def call_list_users(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода List Users.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        list_users_button: WebElement = driver.find_element(
            By.XPATH, self.__list_users
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(list_users_button).perform()
        list_users_button.click()
        if delay is not None:
            time.sleep(delay)

    def call_single_user(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Single User.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        single_user_button: WebElement = driver.find_element(
            By.XPATH, self.__single_user
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(single_user_button).perform()
        single_user_button.click()
        if delay is not None:
            time.sleep(delay)

    def call_single_user_404(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Single User 404.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        single_user_404_button: WebElement = driver.find_element(
            By.XPATH, self.__user_not_found
        )
        single_user_404_button.click()
        if delay is not None:
            time.sleep(delay)

    def call_resources_list(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Resources List.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        resources_list_button: WebElement = driver.find_element(
            By.XPATH, self.__list_resources
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(resources_list_button).perform()
        resources_list_button.click()
        if delay is not None:
            time.sleep(delay)

    def call_single_resource(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Single Resource.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        single_resource_button: WebElement = driver.find_element(
            By.XPATH, self.__get_resource
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(single_resource_button).perform()
        single_resource_button.click()
        if delay is not None:
            time.sleep(delay)

    def call_single_resource_404(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Single Resource 404.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        single_resource_404_button: WebElement = driver.find_element(
            By.XPATH, self.__resource_not_found
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(single_resource_404_button).perform()
        single_resource_404_button.click()
        if delay is not None:
            time.sleep(delay)

    def call_create_user(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Create.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        create_user: WebElement = driver.find_element(
            By.XPATH, self.__create_user
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(create_user).perform()
        create_user.click()
        if delay is not None:
            time.sleep(delay)

    def call_update_user(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Update.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        update_user: WebElement = driver.find_element(
            By.XPATH, self.__update_user
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(update_user).perform()
        update_user.click()
        if delay is not None:
            time.sleep(delay)

    def call_patch_user(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Patch.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        patch_user: WebElement = driver.find_element(
            By.XPATH, self.__patch_user
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(patch_user).perform()
        patch_user.click()
        if delay is not None:
            time.sleep(delay)

    def call_delete_user(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода Delete.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        delete_user: WebElement = driver.find_element(
            By.XPATH, self.__delete_user
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(delete_user).perform()
        delete_user.click()
        if delay is not None:
            time.sleep(delay)

    def call_successful_user_register(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода User Register.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        user_register: WebElement = driver.find_element(
            By.XPATH, self.__register_successful
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(user_register).perform()
        user_register.click()
        if delay is not None:
            time.sleep(delay)

    def call_unsuccessful_user_register(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода User Register 400.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        user_register: WebElement = driver.find_element(
            By.XPATH, self.__register_unsuccessful
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(user_register).perform()
        user_register.click()
        if delay is not None:
            time.sleep(delay)

    def call_successful_user_login(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода User Login.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        user_login: WebElement = driver.find_element(
            By.XPATH, self.__login_successful
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(user_login).perform()
        user_login.click()
        if delay is not None:
            time.sleep(delay)

    def call_unsuccessful_user_login(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода User Login 400.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        user_login: WebElement = driver.find_element(
            By.XPATH, self.__login_unsuccessful
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(user_login).perform()
        user_login.click()
        if delay is not None:
            time.sleep(delay)

    def call_list_users_with_delay(self, driver: Chrome, delay: int = None) -> None:
        """
        Вызов метода List Users с задержкой.
        :param driver: Chrome
        :param delay: int | None
        :return: None
        """
        list_users: WebElement = driver.find_element(
            By.XPATH, self.__delay
        )
        actions: ActionChains = ActionChains(driver)
        actions.move_to_element(list_users).perform()
        list_users.click()
        if delay is not None:
            time.sleep(delay)

    def parse_request_url(self, driver: Chrome) -> str:
        """
        Парсинг URL запроса метода с UI.
        :param driver: Chrome
        :return: str
        """
        url: WebElement = driver.find_element(
            By.XPATH, self.__request_url
        )
        return url.text

    def parse_request_body(self, driver: Chrome) -> str:
        """
        Парсинг тела запроса метода с UI.
        :param driver: Chrome
        :return: str
        """
        request_body: WebElement = driver.find_element(
            By.XPATH, self.__request_body
        )
        return request_body.text

    def parse_response_body(self, driver: Chrome) -> str:
        """
        Парсинг тела ответа метода с UI.
        :param driver: Chrome
        :return: str
        """
        response: WebElement = driver.find_element(
            By.XPATH, self.__response_body
        )
        return response.text

    def parse_response_status_code(self, driver: Chrome) -> int:
        """
        Парсинг статус-кода метода с UI.
        :param driver: Chrome
        :return: int
        """
        response_status_code: WebElement = driver.find_element(
            By.XPATH, self.__status_code
        )
        return int(response_status_code.text)
