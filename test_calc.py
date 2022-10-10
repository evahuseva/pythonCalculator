from calculator import Calc


def test_successful_calculations():
    test_value = Calc('11+11+11+11+11+11+11+11+11+11+11+11').calculate()
    assert type(test_value) is int
    assert 132 == test_value
    test_value = Calc('1*10-5000000+200').output()
    assert type(test_value) is int
    assert -4999790 == test_value
    test_value = Calc('1*2+3*4-5*6+7*8-9*10+123*456').calculate()
    assert type(test_value) is int
    assert 56038 == test_value
    test_value = Calc('0').calculate()
    assert type(test_value) is int
    assert 0 == test_value
    test_value = Calc('100-10-20-30').calculate()
    assert type(test_value) is int
    assert 40 == test_value


