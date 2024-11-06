#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.get("http://google.com")
import pytest

'''Почему не добавляется модуль selenium?'''


@pytest.fixture()
def before_after():
    print("Предусловия перед тестом")
    yield
    print("\nУсловия после теста")


def test_demo1():
    assert 1 == 1


def test_demo2(before_after):
    assert 1 == 2

