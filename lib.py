import pandas as pd
import math
import numpy as np

import openpyxl
import sklearn

import matplotlib.pyplot as plt
import seaborn as sns

import os
import configparser
import re
import datetime as date
from datetime import datetime
import random
import warnings

import cx_Oracle
import sqlalchemy
from sqlalchemy import create_engine
import pyodbc
from sqlalchemy.dialects import oracle

from pandas.core.common import SettingWithCopyWarning
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
warnings.simplefilter(action='ignore', category=SettingWithCopyWarning)
warnings.filterwarnings('ignore')
pd.options.display.float_format ='{:,.2f}'.format


from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action='ignore', category=SettingWithCopyWarning)
warnings.filterwarnings('ignore')

config = configparser.ConfigParser()
config.read('../config.ini')

def connected_bd(db):
    if db == 'ORA':
        user = config.get('ORA_DB', 'user')
        pwd = config.get('ORA_DB', 'pwd')
        dsn = cx_Oracle.makedsn(
            'dwh.citadele.lv',
            '1525',
            service_name='dwhd.citadele.lv')
        conn_ora = cx_Oracle.connect(
            user=user,
            password=pwd,
            dsn=dsn)
        return conn_ora
    
    if db == 'sysprod':
        user = config.get('SYBASE_PROD', 'user')
        pwd = config.get('SYBASE_PROD', 'pwd')
        dns = config.get('SYBASE_PROD', 'dns')
        engine = create_engine(f"sybase+pyodbc://{user}:{pwd}@{dns}")
        return engine
    
    if db == 'systest':
        user = config.get('SYBASE_TEST', 'user')
        pwd = config.get('SYBASE_TEST', 'pwd')
        dns = config.get('SYBASE_TEST', 'dns')
        engine = create_engine(f"sybase+pyodbc://{user}:{pwd}@{dns}")
        return engine  
        
        