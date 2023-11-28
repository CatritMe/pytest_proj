from utils.dicts import get_val


def test_get_val():
    assert get_val({1:133}, 1) == 133
    assert get_val({1: 133}, 2) == 'git'