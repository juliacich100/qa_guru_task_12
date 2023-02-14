import pytest


def test_passed():
    pass


def test_failed_one():
    assert 1 == 2


def test_skipped():
    pytest.skip(reason='as example of a skipped test')