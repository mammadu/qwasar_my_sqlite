import sys
<<<<<<< HEAD
sys.path.insert(0, '../my-sqlite/')
from my_sqlite_request import MySqliteRequest

test_class = MySqliteRequest()
=======
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

#main data srcs
nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#prints generic output of MySqLiteRequest class
>>>>>>> temH
print(test_class)
