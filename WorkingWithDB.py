import pyodbc

server = '192.168.10.158:1433'
database = 'EdFi_Ods_Sandbox_rSxRW5q6MUEg0Qje3Vpvi'
username = r"INNIVEINC\NRadev"
password = '7wVIYCk6ctsHohS'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password +'MultipleActiveResultSets=true;')
cursor = cnxn.cursor()