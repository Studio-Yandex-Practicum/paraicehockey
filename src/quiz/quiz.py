from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Poll

from src.core.constants import quiz_results, quizzes
from src.core.prometheus import (FUNC, QUIZ, counter_push_quiz_start,
                                 counter_viewed_quiz, counter_viewed_quiz_res)

from .model import Quiz

quizzes = Quiz.make_quiz(quizzes)


def quiz_menu(update, context):
    """Функция для выдачи кнопки для старта Квиза."""
    counter_viewed_quiz.labels(group=QUIZ).inc()
    chat_id = update.effective_chat.id
    keyboard = [
        [InlineKeyboardButton('Старт', callback_data='quiz_questions')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')]]
    context.bot_data.clear()
    context.bot.send_message(
        chat_id=chat_id,
        text='А что ты знаешь о хоккее? \
Давай проверим! Для начала нажми "Старт"',
        reply_markup=InlineKeyboardMarkup(keyboard))


def quiz(update=None, context=None, chat_id=None, index=0):
    """Функция для отправки пользователю вопросов и вариантов ответа."""
    if index == 0:
        counter_push_quiz_start.labels(group=QUIZ).inc()
    question = quizzes[index].question
    answers = quizzes[index].answers
    correct_answer = quizzes[index].correct_answer
    image_path = quizzes[index].image_path
    keyboard = [
        [InlineKeyboardButton('Меню', callback_data='main_menu')]]
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
    if final_points in quiz_results:
        return quiz_results[final_points]


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
        [InlineKeyboardButton('Меню', callback_data='main_menu')]]
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
        counter_viewed_quiz_res.labels(group=QUIZ).inc()
        final_points = 0
        for poll_id in context.bot_data:
            point = context.bot_data[poll_id]
            final_points += point
        FUNC['quiz_res_' + str(final_points)].labels(group=QUIZ).inc()
        context.bot.send_photo(
            chat_id=chat_id,
            photo=open(analize_results(final_points), 'rb'),
            reply_markup=InlineKeyboardMarkup(keyboard))
        context.bot_data.clear()
