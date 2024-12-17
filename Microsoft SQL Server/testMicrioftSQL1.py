from sqlalchemy import create_engine, inspect
 
# Данные для подключения
server = '192.168.1.36'
database = 'user_db_1'
username = 'user_1'
password = '12345'

# Установка соединения с базой данных
engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=no&TrustServerCertificate=yes')
   
print("База данных подключена")

# Получение списка таблиц
with engine.connect() as connection:
    inspector = inspect(connection)
    tables = inspector.get_table_names()
    print("Таблицы в базе данных:", tables)

