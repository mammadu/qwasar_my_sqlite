import pandas as pd
from os.path import exists
import random
from pandas.core.base import SelectionMixin


class MySqliteRequest:
    def __init__(self):
        self.columns = []
        self.columns_extracted = []
        self.run_dictionary = {}
        self.query_dictionary = {}
        # self.join_dictionary = {}
        self.data_location = '../data/'
        self.from_usage = False
        self.from_message = "Please use from_ method before any other command"
        self.path_message = "File path does not exist, introduce correct path"

    def __repr__(self):
        print(f"current state of query is {self.run_dictionary}")
        return

    def __from__(self, table_name):
        """
        from_ implements the sql FROM command, each request must have one.
        from_ will take a string(table_name) this is the name of the csv file to query.
        """
        csv_path = self.data_location + table_name  #create path
        if (exists(csv_path)):  #check file existence
            df = pd.read_csv(csv_path, sep=',')
            df = df.fillna("null")
            df = df.astype(str)
            tuples = [tuple(x) for x in df.values]
            self.columns = list(df.columns)

            for idx, val in enumerate(tuples):
                self.query_dictionary[idx] = {}
                for jdx, value in enumerate(val):
                    self.query_dictionary[idx][self.columns[jdx]] = value

            self.from_usage = True
            return self.query_dictionary
        else:
            print(self.path_message)

    def __select__(self, string_s):
        """
        The select_ method implements the sql SELECT command. 
        It takes as the parameter a string OR an array of strings.
        It will continue to build the request. During the run()
        """
        if self.from_usage:

            if not isinstance(string_s, list):  #convert string to list
                s = string_s
                string_s = list()
                string_s.append(s)

            column_bool = True
            for column in string_s:
                if column not in self.columns:
                    column_bool = False
            if self.from_usage == True and column_bool:
                for idx in self.query_dictionary:
                    self.run_dictionary[idx] = {}
                    for column in string_s:
                        self.run_dictionary[idx][
                            column] = self.query_dictionary[idx][column]
        else:
            print(self.from_message)

    def __where__(self, column_name, criteria):
        """
        The where_ method takes two arguments. column_name targets the column and
        criteria the condition to actuate by filtering the entries within run_dictionary.
        """
        if self.from_usage == True and column_name in self.columns:
            for entry in self.run_dictionary:
                if self.run_dictionary[
                        entry] and criteria != self.run_dictionary[entry][
                            column_name]:
                    self.run_dictionary[entry] = None
        else:
            print(self.from_message)

    def __join__(self, other, column_on_db_a, filename_db_b, column_on_db_b):
        """
        The join_ method loads another filename_db
        and will join both database on an on column.
        """
        db_B = MySqliteRequest()
        db_B.fr0m(filename_db_b)
        s_db_A = set(self.column_list_extractor(column_on_db_a))
        s_db_B = set(db_B.column_list_extractor(column_on_db_b))
        print(s_db_B)
        """
        if (s_db_A and s_db_B):
            print("Join Possible")
        else:
            return "Join no possible"
        """
        #...do we need to establish primary keys/foreign keys
        #load both tables
        # self.table
        # other.__from__(table)
        #do select on tables to have specific columns listed
        #   table A [column a, b c]
        #   table B [column d e]
        #   table C[column a, b, e]

    def __order__(self, order, column_name):
        """
        Order Implement an order method which will received two parameters, 
        order (:asc or :desc) and column_name. 
        It will sort depending on the order base on the column_name.
        """
        temp_d = {}
        tup = []
        oP = ["asc", "desc"]
        if self.from_usage and column_name in self.columns and order in oP:

            for key, val in self.query_dictionary.items():
                tup.append((key, val[column_name]))

            if order in "asc":
                temp = sorted(tup, reverse=False, key=lambda x: x[1])
            else:
                temp = sorted(tup, reverse=True, key=lambda x: x[1])

            for idx, val in enumerate(temp):
                temp_d[idx] = self.run_dictionary[val[0]]

            self.run_dictionary = temp_d
        else:
            print(self.from_message)

    def __insert__(self, table_name):
        """
        Insert Implement a method to insert which will receive a table name (filename).
        It will continue to build the request.
        """

    def __values__(self, data):
        """
        Values Implement a method to values which will receive data.
        (a hash of data on format (key => value)).
        It will continue to build the request. During the run() you do the insert.
        """

    def __update__(self, table_name):
        """
        Update Implement a method to update which will receive a table name (filename).
        It will continue to build the request.
        An update request might be associated with a where request
        """

    def __set__(self, data):
        """
        Set Implement a method to update which will receive data
        (a hash of data on format (key => value)). 
        It will perform the update of attributes on all matching row.
        An update request might be associated with a where request.
        """

    def __delete__(self):
        """
        Delete Implement a delete method. 
        It set the request to delete on all matching row. 
        It will continue to build the request. 
        An delete request might be associated with a where request.
        """

    def __run__(self):

        for idx in self.run_dictionary:
            row = ""
            if self.run_dictionary[idx]:
                for column_value in self.run_dictionary[idx]:
                    row += self.run_dictionary[idx][column_value] + " "
                print(row)

    #Helper Functions
    def column_extractor(self):

        choice = random.choice(list(self.run_dictionary.values()))
        li = []
        for key in choice:
            li.append(key)
        return li

    def column_list_extractor(self, column_on_db):
        li = []
        for idx, val in enumerate(self.query_dictionary):
            li.append(self.query_dictionary[idx][column_on_db])
        return li

    #End Helper Function

    def run(self):
        return self.__run__()

    def fr0m(self, table_name):
        return self.__from__(table_name)

    def order(self, order, column_name):
        return self.__order__(order, column_name)

    def join(self, other, column_on_db_a, filename_db_b, column_on_db_b):
        return self.__join__(other, column_on_db_a, filename_db_b,
                             column_on_db_b)
