import psutil
import time
import pyodbc

con = pyodbc.connect('Driver={SQL Server};'
                     'Server=DESKTOP-E6IT52M\\SQLEXPRESS;'
                     'Database=System_Information;'
                     'Trusted_Connection=yes;')

cursor = con.cursor()

while 1==1:
    cpu_usage = psutil.cpu_percent()
    print(cpu_usage)
    time.sleep(1)