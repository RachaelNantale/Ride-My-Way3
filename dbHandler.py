import psycopg2
import os


class MyDatabase():
    dbname = 'ride'
    conn = psycopg2.connect(
                dbname=dbname, user='postgres', host='localhost', password='oscarkirex', port='5432')

    def __init__(self):
        dbname = ""
        if os.getenv("APP_SETTING") == "'testing'":
            dbname = "ridetest_db"
        else:
            dbname = 'ride'

        try:
            self.conn = psycopg2.connect(
                dbname=dbname, user='postgres', host='localhost', password='oscarkirex', port='5432')

            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            self.create_tables()
        except psycopg2.Error as error:
            print(error)

    def create_tables(self):
        users_table = """CREATE TABLE IF NOT EXISTS UserTable (id TEXT PRIMARY KEY NOT NULL,
         username varchar(50) NOT NULL UNIQUE, email varchar(50) NOT NULL UNIQUE,
          password varchar(50) NOT NULL, phone varchar(10) NOT NULL UNIQUE)"""

        rides_table = """CREATE TABLE IF NOT EXISTS RideTable 
        (id TEXT PRIMARY KEY NOT NULL,
        driver TEXT NOT NULL,
        FOREIGN KEY (driver) REFERENCES UserTable(id) ON DELETE CASCADE ON UPDATE CASCADE ,
         pickup_point varchar(50) NOT NULL, destination varchar(50) NOT NULL, 
         time varchar(50) NOT NULL, done bool)"""

        request_table = """CREATE TABLE IF NOT EXISTS RequestTable 
        (request_id TEXT PRIMARY KEY NOT NULL, 
        ride_id TEXT NOT NULL,
        FOREIGN KEY (ride_id) REFERENCES RideTable (id) ON DELETE CASCADE ON UPDATE CASCADE,  
        passenger TEXT NOT NULL, 
        FOREIGN KEY (passenger) REFERENCES UserTable(id) ON DELETE CASCADE ON UPDATE CASCADE ,
        pickup_point varchar(50) NOT NULL, 
        destination varchar(50) NOT NULL, time varchar(50) NOT NULL, status bool)"""

        self.cur.execute(users_table)
        self.cur.execute(rides_table)
        self.cur.execute(request_table)

    def drop_tables(self):
        drop_request_table = """DROP TABLE IF EXISTS RequestTable CASCADE"""

        drop_rides_table = """DROP TABLE IF EXISTS RideTable CASCADE"""
        drop_user_table = """DROP TABLE IF EXISTS UserTable CASCADE"""

        self.cur.execute(drop_request_table)
        self.cur.execute(drop_user_table)
        self.cur.execute(drop_rides_table)

    def create_record(self, sql):
        if self.cur.execute(sql) is None:
            return True
        return False

    def create_login(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def user_login(self, sql):
        """
        User login
        """
        self.cur.execute(sql)
        return self.cur.fetchone()

    def fetch_all_rides(self, id):
        """
        Fetch all rides
        """
        self.cur.execute(
            "SELECT * FROM RideTable;")
        rides = self.cur.fetchall()
        my_rides = []
        for ride in rides:
            my_dict = ({'id': ride[0], 'driver': ride[1],
                        'pickup_point': ride[2], 'destination': [
                3], 'time': [4], 'done': [5]})
            my_rides.append(my_dict)
        return rides

    def fetch_all_requests(self, request_id):
        """
        Fetch all requests
        """
        self.cur.execute(
            "SELECT * FROM RequestTable;")
        requests = self.cur.fetchall()
        my_requests = []
        for request in requests:
            my_dict = {}
            my_dict['ride_id'] = request[0]
            my_dict['request_id'] = request[1]
            my_dict['passenger'] = request[2]
            my_dict['pickup_point'] = request[3]
            my_dict['destination'] = request[4]
            my_dict['time'] = request[5]
            my_dict['status'] = request[6]
            my_requests.append(my_dict)
        return my_requests

    def fetch_one_ride(self, id):

        self.cur.execute(
            "SELECT * FROM RideTable WHERE id = '{}' ".format(id))
        ride = self.cur.fetchone()
        my_dict = {}
        if ride:
            my_dict['id'] = ride[0]
            my_dict['driver'] = ride[1]
            my_dict['pickup_point'] = ride[2]
            my_dict['destination'] = ride[3]
            my_dict['time'] = ride[4]
            my_dict['status'] = ride[5]
            print(my_dict)
            return my_dict
        return None

    def fetch_one_request_by_rideid(self, ride_id):
        self.cur.execute(
            "SELECT * FROM RequestTable WHERE ride_id = '{}' ".format(ride_id))
        requests = self.cur.fetchall()
        my_requests = []
        for request in requests:
            my_dict = {}
            my_dict['ride_id'] = request[0]
            my_dict['request_id'] = request[1]
            my_dict['passenger'] = request[2]
            my_dict['pickup_point'] = request[3]
            my_dict['destination'] = request[4]
            my_dict['time'] = request[5]
            my_dict['status'] = request[6]
            my_requests.append(my_dict)
        return my_requests

    def fetch_one_request(self, request_id):
        self.cur.execute(
            "SELECT * FROM RequestTable WHERE request_id = '{}' ".format(request_id))
        request = self.cur.fetchone()
        if request:
            my_dict = {}
            my_dict['ride_id'] = request[0]
            my_dict['request_id'] = request[1]
            my_dict['passenger'] = request[2]
            my_dict['pickup_point'] = request[3]
            my_dict['destination'] = request[4]
            my_dict['time'] = request[5]
            my_dict['status'] = request[6]
            return my_dict
        return None

    def fetch_user(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def delete_record(self, id):
        delete_cmd = "DELETE FROM RideTable WHERE id='{}'".format(id)
        self.cur.execute(delete_cmd)

    def modify_record(self, sql):
        """
        Modify a record
        """
        if self.cur.execute(sql) is None:
            return True
        return False

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    ride = MyDatabase()
    ride.create_tables()
    