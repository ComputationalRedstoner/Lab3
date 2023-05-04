import Lab2.bmi as bmi

def test_bmi_normalweight():
    result = bmi.calculate_bmi(1.73,57)
    assert (result == 0)

def test_bmi_overweight():
    result = bmi.calculate_bmi(1.65,75)
    assert (result == 1)

def test_bmi_underweight():
    result = bmi.calculate_bmi(1.8,45)
    assert (result == -1)
