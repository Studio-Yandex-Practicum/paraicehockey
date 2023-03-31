QUESTION = 'Question'
OWNER = 'Owner'
FEDERATION = 'Federation'
ADAPTIVE_HOKKEY = 'AdaptiveHockey'
DONATE = 'Donate'
QUIZ = 'Quiz'
WHO_IS_FYRK = 'WhoIsFyrk'
STICKER = 'Sticker'
ALL_FOR_HOCKEY = 'all for hockey'

METRIC_GROUPS = {
    QUESTION: 'Вопросы',
    FEDERATION: 'Федерация',
    ADAPTIVE_HOKKEY: 'Адаптивный хоккей',
    OWNER: 'Запуск Бота',
    DONATE: 'Сделать пожертвование',
    WHO_IS_FYRK: 'Кто такой Фырк',
    STICKER: 'Стикер пак',
    ALL_FOR_HOCKEY: 'Всё для хоккея',
    QUIZ: 'Квиз',
}

METRIC_NAMES = {
    'user_viewed_question_total': 'Просмотр пункта меню: Задать вопрос',
    'user_viewed_federation_activities_total': (
        'Просмотр подпункта меню: Направления деятельности'),
    'user_viewed_federation_total': 'Просмотр пункта меню: Узнать о Федерации',
    'user_viewed_federation_values_total': (
        'Просмотр подпункта меню: Ценности федерации'),
    'user_viewed_adaptive_hockey_total': (
        'Просмотр пункта меню: Адаптивные виды хоккея'),
    'user_viewed_sledzh_hockey_total': 'Просмотр пункта меню: Следж хоккей',
    'user_viewed_special_hockey_total': (
        'Просмотр пункта меню: Специальный хоккей'),
    'user_viewed_hockey_for_blind_total': (
        'Просмотр пункта меню: Хоккей для незрячих'),
    'user_start_bot_total': 'Пользователь нажал "start" и запустил бота',
    'user_viewed_donate_total': 'Просмотр пункта меню: Сделать пожертвования',
    'user_viewed_who_is_fyrk_total': 'Просмотр пункта меню: Кто такой Фырк',
    'user_viewed_quiz_total': 'Просмотр пункта меню: Квиз',
    'user_push_quiz_start_total': 'Нажатие пункта меню: Старт',
    'user_viewed_quiz_result_total': 'Просмотр результатов квиза',
    'user_viewed_sticker_total': 'Просмотр пункта меню: Получить стикерпак',
    'user_viewed_all_for_hockey_total': 'Просмотр пункта меню: Всё для хоккея',
    'user_viewed_quiz_result_0_total': 'Нет правильных ответов',
    'user_viewed_quiz_result_1_total': 'Один правильный ответ',
    'user_viewed_quiz_result_2_total': 'Два правильных ответа',
    'user_viewed_quiz_result_3_total': 'Три правильных ответа',
    'user_viewed_quiz_result_4_total': 'Четыре правильных ответа',
    'user_viewed_quiz_result_5_total': 'Пять правильных ответов',
    'user_viewed_quiz_result_6_total': 'Шесть правильных ответов',
    'user_viewed_quiz_result_7_total': 'Семь правильных ответов',
    'user_viewed_quiz_result_8_total': 'Восемь правильных ответов',
    'user_viewed_quiz_result_9_total': 'Девять правильных ответов',
    'user_viewed_quiz_result_10_total': 'Ответил правльно на все вопросы',

}

PROMETHEUS_URL = 'http://172.17.0.6:9090'
