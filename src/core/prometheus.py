from prometheus_client import CollectorRegistry, Counter

registry = CollectorRegistry()

"""Общее кол-во посещений."""
counter_start_app = Counter('user_start_bot',
                            'Пользователь нажал "start" и запустил бота',
                            ['group'])
registry.register(counter_start_app.labels(group='Owner'))


"""Задать вопрос."""
counter_viewed_question = Counter('user_viewed_question',
                                  'Просмотр пункта меню: Задать вопрос',
                                  ['group'])
registry.register(counter_viewed_question.labels(group='Question'))

counter_push_question = Counter('user_push_question',
                                'Нажатие пункта меню: Получить ответ '
                                '(задают вопрос)',
                                ['group'])
registry.register(counter_push_question.labels(group='Question'))


"""Узнать о Федерации."""
counter_viewed_federation = Counter('user_viewed_federation',
                                    'Просмотр пункта меню: Узнать о Федерации',
                                    ['group'])
registry.register(counter_viewed_federation.labels(group='Federation'))

counter_viewed_federation_values = Counter('user_viewed_federation_values',
                                           'Просмотр подпункта меню: '
                                           'Ценности федерации',
                                           ['group'])
registry.register(counter_viewed_federation_values.labels(group='Federation'))

counter_viewed_federation_activities = Counter(
    'user_viewed_federation_activities',
    'Просмотр подпункта меню: '
    'Направления деятельности',
    ['group'])
registry.register(
    counter_viewed_federation_activities.labels(group='Federation'))

"""Адаптивные виды хоккея"""
counter_viewed_adaptive_hockey = Counter('user_viewed_adaptive_hockey',
                                         'Просмотр пункта меню: '
                                         'Адаптивные виды хоккея',
                                         ['group'])
registry.register(
    counter_viewed_adaptive_hockey.labels(group='AdaptiveHockey'))

counter_viewed_sledzh_hockey = Counter('user_viewed_sledzh_hockey',
                                       'Просмотр подпункта меню: '
                                       'Следж-хоккей',
                                       ['group'])
registry.register(counter_viewed_sledzh_hockey.labels(group='AdaptiveHockey'))

counter_viewed_hockey_for_blind = Counter('user_viewed_hockey_for_blind',
                                          'Просмотр подпункта меню: '
                                          'Хоккей для незрячих',
                                          ['group'])
registry.register(
    counter_viewed_hockey_for_blind.labels(group='Adaptive Hockey'))

counter_viewed_special_hockey = Counter('user_viewed_special_hockey',
                                        'Просмотр подпункта меню: '
                                        'Специальный хоккей',
                                        ['group'])
registry.register(
    counter_viewed_special_hockey.labels(group='AdaptiveHockey'))
ADAPTIVE_HOKKEY_PROMETHEUS = {
    'sledzh_hockey': counter_viewed_sledzh_hockey,
    'special_hockey': counter_viewed_special_hockey,
    'hockey_for_blind': counter_viewed_hockey_for_blind
}
