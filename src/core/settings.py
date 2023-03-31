import logging
import os

from pydantic import BaseSettings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


class Settings(BaseSettings):
    """Класс с общими настройками бота."""

    bot_token: str
    url_donation: str
    app_title: str = 'Телеграм-бот для НКО “Федерация адаптивного хоккея”'
    secret_key: str = os.getenv('SECRET_KEY')
    telegram_admin_ids: str = os.environ.get('TELEGRAM_ADMIN_IDS')
    bot_prometheus: str = os.environ.get('BOT_PROMETHEUS')
    bot_port: str = os.environ.get('BOT_PORT')
    postgres_user: str = os.environ.get('POSTGRES_USER')
    postgres_password: str = os.environ.get('POSTGRES_PASSWORD')
    postgres_db: str = os.environ.get('POSTGRES_DB')
    postgres_host: str = os.environ.get('POSTGRES_HOST')
    postgres_port: str = os.environ.get('POSTGRES_PORT')

    class Config:
        """Название файла с переменными окружения в конфиге."""

        env_file = '.env'


settings = Settings()


class Config:
    """Класс с настройками Flask."""

    SECRET_KEY = settings.secret_key
    PREFERRED_URL_SCHEME = 'https'
