import pyodbc


def get_db_connection():
    driver = 'ODBC Driver 17 for SQL Server'
    server = "JARVIS"
    database = "ClubHopper"
    conn = pyodbc.connect(
             Driver='{' + driver + '}',
             Server=server,
             Database=database,
             Trusted_Connection='yes')
    return conn
