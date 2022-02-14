from stringcalc import string_cal

def test_empty_string():
    result= string_cal("")
    assert result=="0"

def test_number_string():
    result= string_cal("1")
    assert result== 1

def test_sum_of_number():
    result= string_cal("1234")
    assert result==10


def test_sum_of_numbers_with_delimiter():
    result= string_cal("1/2\n3;4")
    assert result== 10

def test_negative_number():
    result=string_cal("-2")
    assert result=="negatives not allowed -2"