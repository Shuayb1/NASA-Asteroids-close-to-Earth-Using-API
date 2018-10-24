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

        date_list = []
        db_input = {}

        for single_date in (self.start_date + timedelta(n) for n in range(day_count)):
            date_list.append(single_date.strftime('%Y-%m-%d'))

        for day in date_list:
            day_link = self.asteroid.neo_feed(self.start_date, self.end_date)['near_earth_objects'][day]
            db_input[day] = {}

            for get in day_link:
                self.name = get['name']
                self.distance = get['close_approach_data'][0]['miss_distance']['kilometers']
                db_input[day].update({self.name: self.distance})


        # self.nasa_coll_all.insert(db_input)
        # print(self.db_input[self.end_date])

        # self.today_asteroids()

    def today_asteroids(self):

        db_input_today = {}
        today = datetime.today().strftime('%Y-%m-%d')

        today_link = self.asteroid.neo_feed(self.start_date, self.end_date)['near_earth_objects'][today]

        for get in today_link:
            name = get['name']
            distance = get['close_approach_data'][0]['miss_distance']['kilometers']
            db_input_today[name] = distance

        # print(db_input_today)
        # self.nasa_coll_today.insert(db_input_today)


if __name__ == "__main__":
    TheAPI()
