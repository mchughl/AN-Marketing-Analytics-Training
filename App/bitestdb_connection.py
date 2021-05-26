import pandas as pd
import sqlalchemy
import urllib
import glob
import os
import pathlib
import datetime

## Connection 
server = "s1wpvsqlmbi1.us1.autonation.com"
db = 'BITESTDB'
params = urllib.parse.quote_plus(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
connection = engine.connect()

