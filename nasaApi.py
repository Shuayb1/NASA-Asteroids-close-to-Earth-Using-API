
from datetime import date, timedelta, datetime
from pyhorizon import Horizon
from nasaDB import TheClient


#To use the method in the inherited class TheClient
class TheAPI(TheClient):

    asteroid = Horizon(key='MnQpBaHXkxFOkbdm0kHQuneUvVXAV59Fwl8h2ILk')

    end_date = date.today()
    start_date = end_date - timedelta(1)
    my_object = {}

    def __init__(self):
        super(TheAPI, self).__init__()
        day_count = (self.end_date - self.start_date).days + 1
        self.v = []
        for single_date in (self.start_date + timedelta(n) for n in range(day_count)):
            self.v.append(single_date.strftime('%Y-%m-%d'))
        # print(len(self.v))
        for i in self.v:
            a = self.asteroid.neo_feed(self.start_date, self.end_date)['near_earth_objects'][i]
            for c in a:
                name = c['name']
                distance = c['close_approach_data'][0]['miss_distance']['kilometers'] + 'km'
                self.my_object[name] = distance
        print(self.my_object)
        self.today_asteroids()
      #  self.nasa_coll.insert(self.my_object)

    def today_asteroids(self):
        # for i in self.v:
        my_object_today = {}
        today = datetime.today().strftime('%Y-%m-%d')

        a = self.asteroid.neo_feed(self.start_date, self.end_date)['near_earth_objects'][today]
        for c in a:
            name = c['name']
            distance = c['close_approach_data'][0]['miss_distance']['kilometers'] + 'km'
            my_object_today[name] = distance
        print(my_object_today)


if __name__ == "__main__":
    TheAPI()




'''
case_list = []
for entry in entries_list:
    case = {'key1': entry[0], 'key2': entry[1], 'key3':entry[2] }
    case_list.append(case)
    
    
slice = dict()
>>> for character in characters:
...     slice.update({character:len(character)})
        slice[character] = len(character)
    
pupils_dictionary = {}


for x in range(3):    
    new_key = raw_input('Enter new key: ')
    new_age = raw_input('Enter new age: ')
    pupils_dictionary[new_key] = new_age
print(pupils_dictionary)    

'''