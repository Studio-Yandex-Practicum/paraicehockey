import logging

from pydantic import BaseSettings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


class Settings(BaseSettings):
    """Класс с общими настройками бота."""

    bot_token: str
    url_donation: str
    app_title: str = 'Телеграм-бот для НКО “Федерация адаптивного хоккея”'

    class Config:
        """Название файла с переменными окружения в конфиге."""

        env_file = '.env'


settings = Settings()
