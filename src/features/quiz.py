from telegram import Poll, InlineKeyboardButton, InlineKeyboardMarkup

from src.core.constants import (
    QUESTIONS, RIGHT_ANSWERS,
    ANSWER_VARIANTS, NAMED_RIGHT_ANSWERS)


def start_quiz(update, context):
    """Функция для выдачи кнопки для старта Квиза."""
    chat_id = update.effective_chat.id
    keyboard = [
        [InlineKeyboardButton('Старт', callback_data='quiz_questions')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]

    context.bot.send_message(
        chat_id=chat_id,
        text='А что ты знаешь о хоккее? \
Давай проверим! Для начала нажми "Старт"',
        reply_markup=InlineKeyboardMarkup(keyboard))


def quiz(update=None, context=None, chat_id=None, index=None):
    """Функция для отправки пользователю вопросов и вариантов ответа."""
    keyboard = [
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]
    if update:
        chat_id = update.effective_chat.id
    if index is None:
        question = QUESTIONS[0]
        answers = ANSWER_VARIANTS[0]
        correct_answer = RIGHT_ANSWERS[0]
    else:
        question = QUESTIONS[index]
        answers = ANSWER_VARIANTS[index]
        correct_answer = RIGHT_ANSWERS[index]
    if question == 'Кто изображен на фото?':
        context.bot.send_photo(
            chat_id,
            open('src/static/images/Портрет квиз.jpg', 'rb')
        )
    if question == 'Это клюшка для...':
        context.bot.send_photo(
            chat_id,
            open('src/static/images/Клюшка.jpg', 'rb')
        )
    message = context.bot.send_poll(
        chat_id=chat_id,
        question=question,
        options=answers,
        type=Poll.QUIZ,
        correct_option_id=correct_answer,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    payload = {
        message.poll.id: {
            'question': question,
            'message_id': message.message_id,
            'chat_id': chat_id
        }
    }
    context.bot_data.update(payload)


def analize_results(final_points):
    """Функция для анализа результата ответов пользователя на вопросы."""
    if final_points > 9:
        return f'Количество правильных ответов: {final_points}, \
твой статус "Хоккейный гуру"'
    if final_points <= 8 and final_points >= 7:
        return f'Количество правильных ответов: {final_points}, \
твой статус "Знаток хоккея"'
    if final_points <= 6 and final_points > 5:
        return f'Количество правильных ответов: {final_points}, \
твой статус "Хоккейный профи"'
    if final_points < 5:
        return f'Количество правильных ответов: {final_points}, \
ты молодец, но еще нужно подтянуть знания!'


def poll_handler(update, context):
    """
    Функция для выдачи след.
    квиза после выбора ответа пользователя на вопрос.
    """
    chat_id = context.bot_data[update.poll.id]['chat_id']
    index = QUESTIONS.index(update.poll.question)
    keyboard = [
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]
    if index <= 9:
        for answer in update.poll.options:
            if answer.voter_count == 1:
                if answer.text == NAMED_RIGHT_ANSWERS[index]:
                    point = 1
                else:
                    point = 0
        context.bot_data.update({
            update.poll.id: point}
        )
    if index < 9:
        quiz(
            context=context,
            chat_id=chat_id,
            index=index + 1)
    if index == 9:
        final_points = 0
        for poll_id in context.bot_data:
            point = context.bot_data[poll_id]
            final_points += point
        context.bot.send_message(
            chat_id=chat_id,
            text=analize_results(final_points),
            reply_markup=InlineKeyboardMarkup(keyboard))
        context.bot_data.clear()
