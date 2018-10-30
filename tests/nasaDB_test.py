import unittest
import requests

from envparse import env
from nasaApi import TheAPI

env.read_envfile()

nasa_api_key = env.str('NASA_API_KEY')


def get_api():
    response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?' + 'start_date=' + str(TheAPI.start_date) + '&' +
                            'end_date=' + str(TheAPI.end_date) + '&detailed=false&api_key=' + nasa_api_key)

    return response.json()


def parsed_data():
    api_class = TheAPI()
    check_asteroid_distance = api_class.distance
    return check_asteroid_distance


def today_asteroid_link():
    api_class = TheAPI()
    link_variable = api_class.today_link[0]
    return list(link_variable.keys())[4]


class TestNasaDB(unittest.TestCase):
    def test_api(self):
        '''If the API call is ok, this object link should be a string'''
        assert type(get_api()['near_earth_objects'][str(TheAPI.start_date)][0]['links']['self']) == str

    def test_parsed_data(self):
        ''' The asteroid name and asteroid distance with their specific dates are string '''
        assert type(parsed_data()) == str

    def test_today_asteroid_link(self):
        '''nasa_jpl_url is the fourth key in the data set link, which is a list of objects '''
        assert today_asteroid_link() == 'nasa_jpl_url'


if __name__ == '__main__':
    unittest.main()
