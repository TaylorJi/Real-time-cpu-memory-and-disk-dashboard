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
    # extracting the percent value from the array
    memory_usage = psutil.virtual_memory()[2]

    cpu_interrups = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]

    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]

    print(cpu_usage)
    print(memory_usage)
    print(bytes_sent)
    time.sleep(1)