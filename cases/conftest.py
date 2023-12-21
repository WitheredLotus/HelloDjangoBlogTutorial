import jsonpath
import pytest
from pytest_yaml_yoyo.http_session import HttpSession


@pytest.fixture(scope="session", autouse=True)
def login_first(requests_session: HttpSession):

    body = {
        'username': 'test_899',
        'password': '123456'
    }
    res = requests_session.send_request(method='post', url='/api/v1/login', json=body)

    token = jsonpath.jsonpath(res.json(), '$.token')
    print('token: ', token)
    h = {
        'Authorization': f'Token {token[0]}'
    }
    requests_session.headers.update(h)
    yield requests_session