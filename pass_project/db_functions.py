from pickle import TRUE
import sqlite3
import pandas as pd

def get_conx():
    conx = sqlite3.connect("database.db")
    return conx
    
#test func to show conn to db works
def get_user_data():
    con = get_conx()
    user_data = pd.read_sql_query("SELECT * FROM stoke_users;", con)
    user_data_df = pd.DataFrame(user_data)
    con.close()
    return(user_data_df)

# def get_all():
#     con = get_conx()
#     user_data = pd.read_sql_query("SELECT * FROM stoke_users;", con)
#     user_data_df = pd.DataFrame(user_data)
#     con.close()
#     print(user_data_df)

# get_all() 