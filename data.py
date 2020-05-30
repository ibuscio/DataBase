from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
import sqlalchemy as db

auth_plugin = 'mysql_native_password'

Engine = create_engine('sqlite:///fortune500.db')

Session =  sessionmaker(bind = Engine)
Base = declarative_base()