import employee_info

def test_age_range():
    input_low_lim = 30
    input_upp_lim = 35
    test_range_result = [{'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]
    result = employee_info.get_employees_by_age_range(input_low_lim, input_upp_lim)

    assert (result == test_range_result)

def test_avg_salary():
    result = employee_info.calculate_average_salary()

    assert (result == 361000/6)

def test_employee_by_dept():
    test_employees_result = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    result = employee_info.get_employees_by_dept("Sales")

    assert (result == test_employees_result)