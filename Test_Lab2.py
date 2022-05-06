import Lab2

print("Test_Lap2")

def test_float_conversion():
    result = []
    input_var = "90, 10, 80"
    test_var = [90.0, 10.0, 80.0]

    result = Lab2.convert_to_float(input_var)

    assert (result == test_var)

def test_average_calculation():
    result = 0
    input_var = [90.0, 10.0, 80.0]
    test_var = 60.0

    result = Lab2.calc_average(input_var)

    assert (result == test_var)