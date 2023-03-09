from prometheus_client import Counter

"""Общее кол-во посещений."""
counter_start_app = Counter('user_start_bot',
                            'Пользователь нажал "start" и запустил бота')

"""Задать вопрос."""
counter_viewed_question = Counter('user_viewed_question',
                                  'Просмотр пункта меню: Задать вопрос')
counter_push_question = Counter('user_push_question',
                                'Нажатие пункта меню: Получить ответ '
                                '(задают вопрос)')

"""Узнать о Федерации."""
counter_viewed_federation = Counter('user_viewed_federation',
                                    'Просмотр пункта меню: Узнать о Федерации')
counter_viewed_federation_values = Counter('user_viewed_federation_values',
                                           'Просмотр подпункта меню: '
                                           'Ценности федерации')
counter_viewed_federation_activities = Counter(
    'user_viewed_federation_activities',
    'Просмотр подпункта меню: '
    'Направления деятельности')

"""Адаптивные виды хоккея"""
counter_viewed_adaptive_hockey = Counter('user_viewed_adaptive_hockey',
                                         'Просмотр пункта меню: '
                                         'Адаптивные виды хоккея')
counter_viewed_sledzh_hockey = Counter('user_viewed_sledzh_hockey',
                                       'Просмотр подпункта меню: '
                                       'Следж-хоккей')
counter_viewed_hockey_for_blind = Counter('user_viewed_hockey_for_blind',
                                          'Просмотр подпункта меню: '
                                          'Хоккей для незрячих')
counter_viewed_special_hockey = Counter('user_viewed_special_hockey',
                                        'Просмотр подпункта меню: '
                                        'Специальный хоккей')
ADAPTIVE_HOKKEY_PROMETHEUS = {
    'sledzh_hockey': counter_viewed_sledzh_hockey,
    'special_hockey': counter_viewed_special_hockey,
    'hockey_for_blind': counter_viewed_hockey_for_blind
}
