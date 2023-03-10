from prometheus_client import CollectorRegistry, Counter

QUESTION = 'Question'
OWNER = 'Owner'
FEDERATION = 'Federation'
ADAPTIVE_HOKKEY = 'AdaptiveHockey'
DONATE = 'Donate'
QUIZ = 'Quiz'
WHO_IS_FYRK = 'WhoIsFyrk'

registry = CollectorRegistry()

"""Общее кол-во посещений."""
counter_start_app = Counter('user_start_bot',
                            'Пользователь нажал "start" и запустил бота',
                            ['group'])
registry.register(counter_start_app.labels(group=OWNER))

"""Задать вопрос."""
counter_viewed_question = Counter('user_viewed_question',
                                  'Просмотр пункта меню: Задать вопрос',
                                  ['group'])
registry.register(counter_viewed_question.labels(group=QUESTION))

counter_push_question = Counter('user_push_question',
                                'Нажатие пункта меню: Получить ответ '
                                '(задают вопрос)',
                                ['group'])
registry.register(counter_push_question.labels(group=QUESTION))

"""Узнать о Федерации."""
counter_viewed_federation = Counter('user_viewed_federation',
                                    'Просмотр пункта меню: Узнать о Федерации',
                                    ['group'])
registry.register(counter_viewed_federation.labels(group=FEDERATION))

counter_viewed_federation_values = Counter('user_viewed_federation_values',
                                           'Просмотр подпункта меню: '
                                           'Ценности федерации',
                                           ['group'])
registry.register(counter_viewed_federation_values.labels(group=FEDERATION))

counter_viewed_federation_activities = Counter(
    'user_viewed_federation_activities',
    'Просмотр подпункта меню: '
    'Направления деятельности',
    ['group'])
registry.register(
    counter_viewed_federation_activities.labels(group=FEDERATION))

"""Адаптивные виды хоккея"""
counter_viewed_adaptive_hockey = Counter('user_viewed_adaptive_hockey',
                                         'Просмотр пункта меню: '
                                         'Адаптивные виды хоккея',
                                         ['group'])
registry.register(
    counter_viewed_adaptive_hockey.labels(group=ADAPTIVE_HOKKEY))

counter_viewed_sledzh_hockey = Counter('user_viewed_sledzh_hockey',
                                       'Просмотр подпункта меню: '
                                       'Следж-хоккей',
                                       ['group'])
registry.register(counter_viewed_sledzh_hockey.labels(group=ADAPTIVE_HOKKEY))

counter_viewed_hockey_for_blind = Counter('user_viewed_hockey_for_blind',
                                          'Просмотр подпункта меню: '
                                          'Хоккей для незрячих',
                                          ['group'])
registry.register(
    counter_viewed_hockey_for_blind.labels(group=ADAPTIVE_HOKKEY))

counter_viewed_special_hockey = Counter('user_viewed_special_hockey',
                                        'Просмотр подпункта меню: '
                                        'Специальный хоккей',
                                        ['group'])
registry.register(
    counter_viewed_special_hockey.labels(group=ADAPTIVE_HOKKEY))

ADAPTIVE_HOKKEY_PROMETHEUS = {
    'sledzh_hockey': counter_viewed_sledzh_hockey,
    'special_hockey': counter_viewed_special_hockey,
    'hockey_for_blind': counter_viewed_hockey_for_blind
}

"""Сделать пожертвования."""
counter_viewed_donate = Counter('user_viewed_donate',
                                'Просмотр пункта меню: '
                                'Сделать пожертвования',
                                ['group'])
registry.register(counter_viewed_donate.labels(group=DONATE))

counter_push_donate = Counter('user_push_donate',
                              'Нажатие пункта меню: Поддержать',
                              ['group'])
registry.register(counter_push_donate.labels(group=DONATE))

"""Квиз."""
counter_viewed_quiz = Counter('user_viewed_quiz',
                              'Просмотр пункта меню: Квиз',
                              ['group'])
registry.register(counter_viewed_quiz.labels(group=QUIZ))

counter_push_quiz_start = Counter('user_push_quiz_start',
                                  'Нажатие пункта меню: Старт',
                                  ['group'])
registry.register(counter_push_quiz_start.labels(group=QUIZ))

counter_viewed_quiz_res = Counter('user_viewed_quiz_result',
                                  'Просмотр результатов квиза',
                                  ['group'])
registry.register(counter_viewed_quiz_res.labels(group=QUIZ))

FUNC = {}
for number in range(1, 11):
    FUNC['quiz_res_' + str(number)] = Counter(
        'user_viewed_quiz_result_' + str(number),
        'Результат игры квиз ' + str(number),
        ['group'])
    registry.register(
        FUNC['quiz_res_' + str(number)].labels(group='test'))

"""Кто такой Фырк."""
counter_viewed_who_is_fyrk = Counter('user_viewed_who_is_fyrk',
                                     'Просмотр пункта меню: Кто такой Фырк',
                                     ['group'])
registry.register(counter_viewed_who_is_fyrk.labels(group=WHO_IS_FYRK))
