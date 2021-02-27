import pytest

@pytest.fixture()
def my_fixture():
    print("\nfixture SetUp")
    yield
    print("\nfixture TearDown")

def test_first(my_fixture):
    print("test 1")

def test_second(my_fixture):
    print("test 2")