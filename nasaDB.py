#Importing the Mongodb driver for python
from pymongo import MongoClient


class TheClient(object):

    def __init__(self):

        '''connectTimeoutMS  30 s to allow for PaaS warm-up:
        The connection timeout value determines the maximum amount of time the driver will wait for a
        connection to be established with the server. This value is only used when making an initial connection to the
         database, and so selecting the correct setting for this timeout can be a balancing act.

         socketTimeoutMS is set to 5mins:
         The socket timeout option specifies to the driver how long to wait for responses from the server.
         This timeout governs all types of requests (queries, writes, commands, authentication, etc.).
        the driver will never wait more than 5mins
         for the result of a query (although the query will continue to run to completion on the server).


        socketKeepAlive Enabled (True):
         to ensure idle connections are kept alive in the presence of a firewall
         '''

        self.my_client = MongoClient('mongodb://shuayb:shuayb1@ds121373.mlab.com:21373/nasa_db', connectTimeoutMS=30000,
                                socketTimeoutMS=500000, socketKeepAlive=True)
        self.nasa_db = self.my_client.get_default_database()
        self.nasa_coll = self.nasa_db['nasa_collections']
        print(self.nasa_db.collection_names())

        ### Only close the connection when your app is terminating
        self.my_client.close()


