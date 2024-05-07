from sqlalchemy import Column, text
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String 
from sqlalchemy import Table
from sqlalchemy import create_engine


engine = create_engine("sqlite:///my_database.db")

metadata_obj = MetaData()
user = Table(
    'user', 
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)



# for table in metadata_obj.sorted_tables:
#     print(table)


metadata_obj.create_all(engine)


metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_info',
     metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

# print(financial_info.primary_key)
# print(financial_info.columns) 
# print(financial_info.constraints)

# for tables in metadata_obj.tables:
#     print(tables)
# print(metadata_obj.tables)

insert_dados = 1,'juliana','email@email','thi'
insert_text = f"insert into user values{insert_dados}"


with engine.connect() as connection:
    sql_insert = text("insert into user values(1,'juliana','email@email','ju')")
    result_insert = connection.execute(sql_insert)
    #print("Número de linhas inseridas:", result_insert.rowcount)
    
    sql = text('select * from user')
    result = connection.execute(sql)

    for row in result:
        print(row)

    #result.close()

