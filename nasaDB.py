#Importing the Mongodb driver for python
from pymongo import MongoClient

#importing utility to parse environment variables, to be used  in deployment and getting the key
from envparse import env

env.read_envfile()
mongodb_server = env.str('MONGODB_SERVER')


class TheClient(object):

    def __init__(self):

        '''connectTimeoutMS  30 s to allow for PaaS warm-up:
        The connection timeout value determines the maximum amount of time the driver will wait for a
        connection to be established with the server. This value is only used when making an initial connection to the
         database, considering poor network coverage,
          so selecting the correct setting for this timeout can be a balancing act.

         socketTimeoutMS is set to 5mins:
         The socket timeout option specifies to the driver how long to wait for responses from the server.
         This timeout governs all types of requests (queries, writes, commands, authentication, etc.).
        the driver will never wait more than 5mins for the result of a query
         (although the query will continue to run to completion on the server).


        socketKeepAlive Enabled (True):
         to ensure idle connections are kept alive in the presence of a firewall
         '''

        self.my_client = MongoClient(mongodb_server, connectTimeoutMS=30000,
                                     socketTimeoutMS=500000, socketKeepAlive=True)
        self.nasa_db = self.my_client.get_default_database()
        self.nasa_coll_all = self.nasa_db['nasa_collections']
        self.nasa_coll_today = self.nasa_db['nasa_collections_today']

        #Only close the connection when the app is terminating
        self.my_client.close()
