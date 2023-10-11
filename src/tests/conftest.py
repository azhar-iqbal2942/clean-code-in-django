import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


def pytest_addoption(parser):
    """
    The `pytest_addoption` function adds a command line option `--integration` to pytest, allowing users
    to run integration tests.

    :param parser: The `parser` parameter is an instance of the `ArgumentParser` class from the
    `argparse` module. It is used to define and parse command-line arguments. In this case, it is used
    to define a command-line option `--integration` that can be used to enable integration tests
    """
    parser.addoption("--integration", action="store_true", help="run integration tests")


def pytest_runtest_setup(item):
    """
    The function `pytest_runtest_setup` skips tests with the "integration" keyword if the
    "--integration" option is not provided.

    :param item: The `item` parameter in the `pytest_runtest_setup` function represents the test item
    that is being set up for execution. It contains information about the test, such as its name,
    keywords, and configuration values
    """
    if "integration" in item.keywords and not item.config.getvalue("integration"):
        pytest.skip("need --integration option to run")
