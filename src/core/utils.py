from src.core.settings import settings


def check_id(update, context):
    """Проверка, является ли пользователь админом."""
    chat_id = update.message.chat_id
    if str(chat_id) not in settings.telegram_admin_ids:
        context.bot.send_message(
            chat_id=chat_id,
            text='Данная команда доступна только администраторам.'
        )
        return False
    return True


def is_admin(func):
    """Декоратор для проверки, является ли пользователь админом."""
    def wrapped(update, context):
        if not check_id(update, context):
            return None
        return func(update, context)
    return wrapped
