from tests.conftest import arrs_fixture
from utils import arrs

def test_get(arrs_fixture):
    assert arrs.get(arrs_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(arrs_fixture):
    assert arrs.my_slice(arrs_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(arrs_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(arrs_fixture, None, 2) == [1, 2]
    assert arrs.my_slice([], 1) == []
