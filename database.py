from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

    ########################################################
    ################### MySQL Defines ######################
    ###################   Testing     ######################
    ########################################################
    
def insert_user(player_name, discord_tag):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            c = conn.cursor()
            c.execute(
                "INSERT INTO 'user_management' ('player_name', 'discord_tag') values((%s, %s);",
                player_name, discord_tag)
            conn.commit()
            c.close()
        except Exception as e:
            return e