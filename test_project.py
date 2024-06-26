from project import *


def test_take_coin():
    assert take_coin(3) == 3
    assert take_coin(2) == 2
    assert take_coin(1) == 1

    try:
        take_coin(0)
        assert False
    except ValueError:
        assert True

    try:
        take_coin(4)
        assert False
    except ValueError:
        assert True

    try:
        take_coin(-1)
        assert False
    except ValueError:
        assert True


def test_computer_takes_coins():
    assert computer_takes_coins(6) == 1
    assert computer_takes_coins(7) == 2
    assert computer_takes_coins(8) == 3
    assert computer_takes_coins(15) == 2


def test_wining_situation():
    assert wining_situation(
        2) == f'\n{RED}YOU LOSE! You took the last coin.{RESET}\n'
    assert wining_situation(
        1) == f'\n{GREEN}YOU WIN! The machine took the last coin.{RESET}\n'
