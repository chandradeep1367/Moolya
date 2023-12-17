import pytest


##### if we are not define scope it will like test setup and test teardowm
@pytest.fixture(scope="class")
def setup():
    print("this will run first")
    yield
    print("this will run in last")

@pytest.fixture(scope="class")
def name():
    return ["sunil", "anil", "chandradeep"]

@pytest.fixture(params=['Chrome','Firefox'])
def data(request):
    return request.param
