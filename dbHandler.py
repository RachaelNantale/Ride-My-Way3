import psycopg2


class MyDatabase():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                "dbname='ride' user='postgres' host='localhost' password='oscarkirex' port='5432'")

            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            self.create_tables()
        except psycopg2.Error as error:
            print(error)

    def create_tables(self):
        users_table = "CREATE TABLE IF NOT EXISTS UserTable (id TEXT PRIMARY KEY NOT NULL, username varchar(50) NOT NULL, email varchar(50) NOT NULL, password varchar(50) NOT NULL, phone varchar(10) NOT NULL)"
        rides_table = "CREATE TABLE IF NOT EXISTS RideTable (id TEXT PRIMARY KEY NOT NULL,  driver varchar(25) NOT NULL UNIQUE, pickup_point varchar(50) NOT NULL, destination varchar(50) NOT NULL, time varchar(50) NOT NULL, done bool)"
        request_table = "CREATE TABLE IF NOT EXISTS RequestTable (id TEXT PRIMARY KEY NOT NULL,  passenger varchar(25) NOT NULL, pickup_point varchar(50) NOT NULL, destination varchar(50) NOT NULL, time varchar(50) NOT NULL)"
        self.cur.execute(users_table)
        self.cur.execute(rides_table)
        self.cur.execute(request_table)

    def create_record(self, sql):
        if self.cur.execute(sql) is None:
            return True
        return False

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

    def fetch_one_ride(self, id):

        self.cur.execute(
            "SELECT * FROM RideTable WHERE id = '{}' ".format(id))
        ride = self.cur.fetchone()
        my_dict = {}
        my_dict['id'] = ride[0]
        my_dict['driver'] = ride[1]
        my_dict['pickup_point'] = ride[2]
        my_dict['destination'] = ride[3]
        my_dict['time'] = ride[4]
        my_dict['done'] = ride[5]
        print(my_dict)
        return my_dict

    def delete_record(self, id):
        delete_cmd = "DELETE FROM RideTable WHERE id='{}'".format(id)
        self.cur.execute(delete_cmd)

    def modify_ride(self, sql):
        """
        Modify a request
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
    # ride.fetch_all('RequestTable')
    # ride.fetch_one('RideTable')

    # ride.create_record("UserTable", "(id, username,email,password, phone)",
    #                    ('1yyqqqy', 'rachael', 'rachaelexample.com', '', '1111111111'))
    # ride.create_record("RideTable", "(id, driver,pickup_point,destination, time, done)",
    #                    ('1yeq', 'rachael', 'Kamwokya', 'busia', '7pm', False))
