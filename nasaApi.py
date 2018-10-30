#importing the python wrapper for distance near objects
from pyhorizon import Horizon

#importing date
from datetime import date, timedelta, datetime

#importing the database class
from nasaDB import TheClient

#import utility to parse environment variables, to be used  in deployment
from envparse import env
env.read_envfile()

nasa_api_key = env.str('NASA_API_KEY')


#To use the method in the inherited class TheClient
class TheAPI(TheClient):

    #assigning the object
    asteroid = Horizon(key=nasa_api_key)

    #defining end and start days
    end_date = date.today()
    start_date = end_date - timedelta(6)

    def __init__(self):
        super(TheAPI, self).__init__()
        day_count = (self.end_date - self.start_date).days + 1

        self.date_list = []

        for single_date in (self.start_date + timedelta(n) for n in range(day_count)):
            self.date_list.append(single_date.strftime('%Y-%m-%d'))
        self.parse_all_data()

    def parse_all_data(self):
        db_input = {}

        for day in self.date_list:
            day_link = self.asteroid.neo_feed(self.start_date, self.end_date)['near_earth_objects'][day]
            db_input[day] = {}

            for get in day_link:
                self.name = get['name']
                self.distance = get['close_approach_data'][0]['miss_distance']['kilometers']

                db_input[day].update({self.name: self.distance})

        # self.nasa_coll_all.insert(db_input)

        self.today_asteroids()

    def today_asteroids(self):
        self.today_link = self.request_today_data(self.asteroid)
        self.parse_today_data(self.today_link)

    def request_today_data(self, api):
        self.today = datetime.today().strftime('%Y-%m-%d')
        return api.neo_feed(self.start_date, self.end_date)['near_earth_objects'][self.today]

    def parse_today_data(self, today_link):
        self.db_input_today = {}
        for get in today_link:
            name = get['name']
            distance = get['close_approach_data'][0]['miss_distance']['kilometers']
            self.db_input_today[name] = distance

        # self.nasa_coll_today.insert(db_input_today)


if __name__ == "__main__":
    TheAPI()
