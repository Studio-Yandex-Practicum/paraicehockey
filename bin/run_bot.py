from src.features.base import show_main_menu
from prometheus_client import start_http_server


if __name__ == '__main__':
    start_http_server(8000)
    show_main_menu()
