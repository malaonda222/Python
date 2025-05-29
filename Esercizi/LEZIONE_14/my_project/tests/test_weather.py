from my_project.weather import check_weather
import pytest 

'''
def test_check_weather1():
    assert check_weather(21.00) == 'hot', 'temperatures greater than 20 degrees must be considered as hot'


def test_check_weather2():
    assert check_weather(5.00) == 'average', 'temperatures between 10 and 20 degree must be considered as average temperature'


def test_check_weather3():
    assert check_weather(5.00) == 'cold', 'temperatures lower than 10 degrees must be considered as cold'


def test_check_weather4():
    assert check_weather(13.00) == 'average', 'temperatures between 10 degrees and 20 degrees must be considered as average temperature'

def test_check_weather5():
    assert check_weather(30.00) == 'hot', 'temperatures greater than 20 degrees must be considered as hot temperatures'
    assert check_weather(11.00) == 'cold', 'temperatures lower than 10 degrees must be considered as cold temperatures' 
'''


@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])

def test_check_weather(temperature, expected):
    ae: str = ""
    if temperature > 20:
        ae = 'temperatures greater than 20 degrees must be considered as hot'
    elif 10 < temperature <= 20:
        ae = 'temperatures within 10 and 20 degrees must be considered as average temperature'
    else:
        ae = 'temperatures lower than 10 degrees must be considered as cold'
    assert check_weather(temperature) == expected, ae



    
