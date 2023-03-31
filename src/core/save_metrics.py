from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.core.settings import settings

# engine = create_engine(
#     f'postgresql://{settings.postgres_user}:{settings.postgres_password}@'
#     f'172.17.0.7:{settings.postgres_port}/{settings.postgres_db}'
# )
engine = create_engine(
    f'postgresql://{settings.postgres_user}:{settings.postgres_password}@'
    f'172.17.0.7:5432/{settings.postgres_db}'
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Metric(Base):
    """Создаем таблицу в базе данных."""

    __tablename__ = 'metrics'

    id_ = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    value = Column(Integer)

    def __repr__(self):
        """Возвращаем строковое представление."""
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
