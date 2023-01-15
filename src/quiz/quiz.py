from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Poll

from src.core.constants import quiz_results, quizzes

from .model import Quiz

quizzes = Quiz.make_quiz(quizzes)


def quiz_menu(update, context):
    """Функция для выдачи кнопки для старта Квиза."""
    chat_id = update.effective_chat.id
    keyboard = [
        [InlineKeyboardButton('Старт', callback_data='quiz_questions')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]
    context.bot_data.clear()
    context.bot.send_message(
        chat_id=chat_id,
        text='А что ты знаешь о хоккее? \
Давай проверим! Для начала нажми "Старт"',
        reply_markup=InlineKeyboardMarkup(keyboard))


def quiz(update=None, context=None, chat_id=None, index=0):
    """Функция для отправки пользователю вопросов и вариантов ответа."""
    question = quizzes[index].question
    answers = quizzes[index].answers
    correct_answer = quizzes[index].correct_answer
    image_path = quizzes[index].image_path
    keyboard = [
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]

    if update:
        chat_id = update.effective_chat.id
    if image_path:
        context.bot.send_photo(
            chat_id,
            open(image_path, 'rb')
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
    if final_points >= 9:
        return quiz_results['9-10'].format(final_points)
    if final_points >= 7 and final_points <= 8:
        return quiz_results['7-8'].format(final_points)
    if final_points >= 5 and final_points <= 6:
        return quiz_results['5-6'].format(final_points)
    return quiz_results['0-4'].format(final_points)


def poll_handler(update, context):
    """
    Функция для выдачи след.
    квиза после выбора ответа пользователя на вопрос.
    """
    chat_id = context.bot_data[update.poll.id]['chat_id']
    index = Quiz.find_index(
        quizzes,
        update.poll.question)
    keyboard = [
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]
    if index <= (len(quizzes) - 1):
        for answer in update.poll.options:
            if answer.voter_count == 1:
                if answer.text == quizzes[index].named_correct_answer:
                    point = 1
                else:
                    point = 0
        context.bot_data.update({
            update.poll.id: point}
        )
    if index < (len(quizzes) - 1):
        quiz(
            context=context,
            chat_id=chat_id,
            index=index + 1)
    if index == (len(quizzes) - 1):
        final_points = 0
        for poll_id in context.bot_data:
            point = context.bot_data[poll_id]
            final_points += point
        context.bot.send_message(
            chat_id=chat_id,
            text=analize_results(final_points),
            reply_markup=InlineKeyboardMarkup(keyboard))
        context.bot_data.clear()
