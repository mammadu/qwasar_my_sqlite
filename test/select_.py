import sys
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing from
test_class.__from__(nba_player_data)

#Testing select_ command
test_class.__select__("year_start")

test_class.__repr__()

# Desired output -> 1 : {name: "Mammadu"}
