import sys
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_players.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing from
#test_class.from_(nba_player_data)

print(test_class.from_(nba_player))

