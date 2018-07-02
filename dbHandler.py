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

    def fetch_all(self, table, condition="ORDER BY id DESC"):
        """ This is for getting all variables """
        fetchall_query = "SELECT * FROM {} {}".format(table, condition)
        self.cur.execute(fetchall_query)
        total_results = self.cur.fetchall()
        if total_results:
            return total_results
        return None

    def fetch_one(self, table, condition="ORDER BY id DESC"):
        """ This is for fetching one """
        fetchone_query = "SELECT * FROM {} {}".format(table, condition)
        self.cur.execute(fetchone_query)
        total_results = self.cur.fetchone()
        if total_results:
            return total_results
        return None

    def delete_request(self, id):
        self.cur.execute("DELETE FROM RequestTable WHERE id = {} ".format(id))
        return True

    def modify_request(self, id):
        self.cur.execute("UPDATE requests SET RequestTable =%s WHERE id = %s ")
        return True

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
