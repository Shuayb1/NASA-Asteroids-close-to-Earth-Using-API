# NASA Asteroids close to Earth Using API
The National Aeronautics and Space Administration (NASA) is an American agency
responsible for aeronautics and aerospace research. NASA’s API provides data on
objects in space. It is an app that displays a list of all Asteroids close to the earth.
The app should list 5 asteroids, and its distance from the earth on a given day. The
app should have a form where a user can input a date over the last 30 days. It should
fetch data from NASA and display the asteroids closest the earth, ordered in
ascending order of their distance from the earth.
It should also cache data fetched from the external API into a local
database and render data from its database, if it is not
older than 5 mins. If the data is older than 5 mins, it should refetch it from the
API and update the cache with the new data.

The projectct is build using Python; web framework is flask, and DB is Pymongo(MongoDB for python). 
Trello board for the project - https://trello.com/b/uHy25mRb/nasa-asteroids-close-to-earth-using-api
