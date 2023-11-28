import pytest

array = [1, 2, 3, 4]
@pytest.fixture
def arrs_fixture():
    return array
