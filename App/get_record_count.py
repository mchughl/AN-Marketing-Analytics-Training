from bitestdb_connection import *

schema = 'PhetsavongR'
table = 'test_a'
sql_statement = '''select * from {}.{}.{}'''.format(db,schema,table)
#sql_statement = '''select * from {}.{}.{} where Hyperion = 2571'''.format(db,schema,table)

# Get Current Count of records before import
def getCurrentCountFromDB(query, engine):
    current_table_df = pd.read_sql(query, engine)
    db_count = len(current_table_df.index)
    return print('''The process found {} records'''.format(db_count))

def main():
    getCurrentCountFromDB(sql_statement,engine)

if __name__ == '__main__':
    main()
