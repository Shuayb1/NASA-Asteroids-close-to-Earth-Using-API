import unittest
import requests

from envparse import env
from nasaApi import TheAPI
import app

env.read_envfile()

nasa_api_key = env.str('NASA_API_KEY')


def get_api():
    response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?' + 'start_date=' + str(TheAPI.start_date) + '&' +
                            'end_date=' + str(TheAPI.end_date) + '&detailed=false&api_key=' + nasa_api_key)

    return response.json()


def db_input():
    api_class = TheAPI()
    check_db_input = api_class.distance
    return check_db_input

#
# def db_output():
#     s = app.app.test_client()
#     return s


class TestNasa(unittest.TestCase):
    def test_api(self):
        '''If the API call is ok, this object link should be a string'''
        assert type(get_api()['near_earth_objects'][str(TheAPI.start_date)][0]['links']['self']) == str

    def test_db_input(self):
        ''' The asteroid name and asteroid distance with their specific dates are object i.e dict '''
        assert type(db_input()) == str

    # def test_db_output(self):
    #     '''This is what goes out to the html, after all the required field is gotten'''
    #     assert type(db_output()) == dict


if __name__ == '__main__':
    unittest.main()
