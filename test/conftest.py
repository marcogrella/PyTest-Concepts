import pytest

'''
    -> file named as conftest.py turns all fixture available in all test files in that folder
'''


@pytest.fixture()
def setup():
    print("----------->>> I will be executed first. I am available for all test files!")
    yield
    print("---------------->>> Hey, I will be executed last (after test_fixtureDemo method)")


@pytest.fixture(scope="class")
def setup_class_scope():
    print("----------->>> I will be executed first (with scope class) . I am available for all test files!")
    yield
    print("---------------->>> Hey, I will be executed last (after class)")


def test_fixtureDemo(setup):
    print("----------->>> I will execute steps in fixtureDemo method")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Raul", "Grella", "raulgrella@gmail.com"]

@pytest.fixture(params=[
    ("parametro 1", "parametro 1.1", "parametro 1.2"),
    "parametro 2",
    ("parametro 3", "parametro 3.1")
])
def cross_params(request):
    return request.param