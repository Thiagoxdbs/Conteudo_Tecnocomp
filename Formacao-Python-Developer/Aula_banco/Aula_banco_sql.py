#from requests import Session
from sqlalchemy import func, select
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, create_engine, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    #column é para acrescentar uma coluna
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)


    address = relationship(
        #criando relacionamento das tabelas com relationship, back_populates colocando o nome da relação
        # cascade enventos em cascata, colocando interdepencia, tirando os usuarios deletados
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User (id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "Address"
    # autoincrement faz o preenchimento automatico
    id = Column(Integer, primary_key=True)
    # nullable não pode vir nulo
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Address (id={self.id}, email_address={self.email_address})"
    

#print(Address.__table__)
#print(User.__tablename__)


#conexão com o banco de dados
engine = create_engine("sqlite://")


#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


insp = inspect(engine)
#se existe table
#print(insp.has_table("user_account"))
#nomes das tabelas
#print(insp.get_table_names())
#schema do banco de dados
#print(insp.default_schema_name)


with Session(engine) as session:
    juliana = User(
        name= "Juliana",
        fullname= "Juliana Mascarenhas",
        address= [Address(email_address='juliana@email.com.br')]
    )
    thiago = User(
        name= "Thiago",
        fullname= "Thiago Bianchi",
        address= [Address(email_address='thiago@email.com.br'),
                  Address(email_address='thiagobianchi@email.com.br')]
    )
    paty = User(
        name= "Paty",
        fullname= "Paty Bianchi"
    )

    #enviando para o bd
    session.add_all([juliana,thiago,paty])

    session.commit()


# stmt = select(User).where(User.name.in_(['Thiago','Paty']))
# for user in session.scalars(stmt):
#     print(user)

# stmt_address = select(Address).where(Address.user_id.in_([2]))
# for address in session.scalars(stmt_address):
#     print(address)

# ordem = select(User).order_by(User.fullname.desc())
# for ordn in session.scalars(ordem):
#     print(ordn)

# ordem = select(Address).order_by(Address.email_address)
# for ordn in session.scalars(ordem):
#     print(ordn)

#join = select(User.fullname, Address.email_address).join_from(Address, User)
# for join_s in session.scalars(join):
#     print(join_s)

# connection = engine.connect()
# results = connection.execute(join).fetchall()
# for conexao in results:
#     print(conexao)

# result_count = select(func.count('*')).select_from(User)
# for rc in session.scalars(result_count):
#     print(rc)