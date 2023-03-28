from prometheus_client import start_http_server

from src.core.settings import settings
from src.features.base import show_main_menu

if __name__ == '__main__':
    start_http_server(settings.bot_port)
    show_main_menu()
