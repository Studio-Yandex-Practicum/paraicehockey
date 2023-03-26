import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    value = Column(Integer)

    def __repr__(self):
        return f"Metric(name='{self.name}', value={self.value})"

def create_table():
    """Создаем таблицу, если еще нет."""
    Base.metadata.create_all(engine)

def get_metric_value(name):
    """Получаем актуальное значение метрики."""
    session = Session()
    metric = session.query(Metric).filter_by(name=name).first()
    if metric:
        return metric.value
    else:
        return None

def update_metric_value(name, value):
    """Сохраняем значени одной метрики."""
    session = Session()
    metric = session.query(Metric).filter_by(name=name).first()
    if metric:
        metric.value = value
    else:
        metric = Metric(name=name, value=value)
        session.add(metric)
    session.commit()


def update_metric_query_value(names, values):
    """Сохраняем значение списка метрик."""
    session = Session()
    for name, value in zip(names, values):
        metric = session.query(Metric).filter_by(name=name).first()
        if metric:
            metric.value = value
        else:
            metric = Metric(name=name, value=value)
            session.add(metric)

    session.commit()


def update_metric_quiz_value(metric_dict):
    """Сохраняем результата метрик для квиза."""
    session = Session()
    for name, value in metric_dict.items():
        metric = session.query(Metric).filter_by(name=name).first()
        if metric:
            metric.value = value
        else:
            metric = Metric(name=name, value=value)
            session.add(metric)
    session.commit()