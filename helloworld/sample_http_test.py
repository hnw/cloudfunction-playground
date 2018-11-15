from unittest.mock import Mock

import main


def test_print_name():
    name = 'test'
    req = Mock(get_json=Mock(return_value={'name': name}))

    # Call tested function
    assert main.hello_http(req) == 'Hello, {}!'.format(name)


def test_print_hello_world():
    req = Mock(get_json=Mock(return_value={}))

    # Call tested function
    assert main.hello_http(req) == 'Hello, World!'
