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

        v = []
        my_object = {}

        for single_date in (self.start_date + timedelta(n) for n in range(day_count)):
            v.append(single_date.strftime('%Y-%m-%d'))

        for i in v:
            a = self.asteroid.neo_feed(self.start_date, self.end_date)['near_earth_objects'][i]

            for c in a:
                name = c['name']
                distance = c['close_approach_data'][0]['miss_distance']['kilometers'] + 'km'
                my_object[name] = distance

        print(my_object)
        # self.nasa_coll_all.insert(my_object)
        self.today_asteroids()

    def today_asteroids(self):

        my_object_today = {}
        today = datetime.today().strftime('%Y-%m-%d')

        a = self.asteroid.neo_feed(self.start_date, self.end_date)['near_earth_objects'][today]

        for c in a:
            name = c['name']
            distance = c['close_approach_data'][0]['miss_distance']['kilometers'] + 'km'
            my_object_today[name] = distance

        print(my_object_today)
        # self.nasa_coll_today.insert(my_object_today)


if __name__ == "__main__":
    TheAPI()
