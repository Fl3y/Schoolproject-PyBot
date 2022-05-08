from mysql.connector import MySQLConnection, Error
import mysql.connector
from python_mysql_dbconfig import read_db_config

    ########################################################
    ################### MySQL Defines ######################
    ###################   Testing     ######################
    ########################################################
    
def insert_user(player_name, ctzn_score):
        try:
            db_config = read_db_config()
            conn = mysql.connector.connect(**db_config)
            c = conn.cursor()
            add_User = (
                "INSERT INTO user_data (player_name, ctzn_score) VALUES (%s, %s)"
                )
            c.execute(add_User, player_name, ctzn_score)
            conn.commit()
            c.close()
        except Exception as e:
            return e