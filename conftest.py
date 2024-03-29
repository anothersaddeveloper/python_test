# content of conftest.py
import pytest


def pytest_addoption(parser):
    print("Running tests")
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    print("Running tests")
    return request.config.getoption("--cmdopt")
