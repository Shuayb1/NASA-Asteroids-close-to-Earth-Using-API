# NASA Asteroids close to Earth Using API
The National Aeronautics and Space Administration (NASA) is an American agency responsible for aeronautics and aerospace research. 

NASA’s API provides data on objects in space. It is an app that displays a list of all Asteroids close to the earth.
The app should list 5 asteroids, and its distance from the earth on a given day. 

The app should have a form where a user can input a date over the last 7days. It should fetch data from NASA and display the asteroids closest the earth, ordered in ascending order of their distance from the earth. It should also cache data fetched from the external API into a local database and render data from its database, if it is not older than 5 mins. If the data is older than 5 mins, it should refetch it from theAPI and update the cache with the new data.

# The projectct is build using

a. Python and Flask Web Framework

b. NASA API/API Python Wrapper

c. MongoDB Database(mLab)

d. HTML and CSS 

e. Travis CI/ Unittesting

f. Virtual Environment and Environment Variables

Trello board for the project - https://trello.com/b/uHy25mRb/nasa-asteroids-close-to-earth-using-api
Wireframe - https://wireframe.cc/pro/edit/194632


# Running the Hello World App
NB: I used variable environment to hide the API Key(NASA_API_KEY) and the Mongodb Server(MONGODB_SERVER), so you should use the variable names as in the parenthesis respectively.

a. Clone the project repo to your computer

b. Using command line, cd into the directory where the project is cloned to

c. In your command line type python hello.py to run the app

d. Open your browser and type the address that is displayed(http://127.0.0.1:5000/)

e. The word "Hello, World!" will be display
