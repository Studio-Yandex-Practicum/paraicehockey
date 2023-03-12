QUESTION = 'Question'
OWNER = 'Owner'
FEDERATION = 'Federation'
ADAPTIVE_HOKKEY = 'AdaptiveHockey'
DONATE = 'Donate'
QUIZ = 'Quiz'
WHO_IS_FYRK = 'WhoIsFyrk'

METRIC_GROUPS = {
    'Question': 'Вопросы',
    'Federation': 'Федерация',
    'AdaptiveHockey': 'Адаптивный хоккей',
    'Owner': 'Запуск Бота',
}

METRIC_NAMES = {
    'user_push_question_total': 'Нажатие пункта меню: Получить ответ',
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
    'user_start_bot_total': 'Пользователь нажал "start" и запустил бота',
}

PROMETHEUS_URL = 'http://prometheus:9090'

