from prometheus_client import CollectorRegistry, Counter

from src.core.prometheus_constants import (ADAPTIVE_HOKKEY, DONATE, FEDERATION,
                                           METRIC_NAMES, OWNER, QUESTION, QUIZ,
                                           WHO_IS_FYRK)

registry = CollectorRegistry()

"""Общее кол-во посещений."""
counter_start_app = Counter('user_start_bot',
                            METRIC_NAMES['user_start_bot_total'],
                            ['group'])
registry.register(counter_start_app.labels(group=OWNER))

"""Задать вопрос."""
counter_viewed_question = Counter('user_viewed_question',
                                  METRIC_NAMES['user_viewed_question_total'],
                                  ['group'])
registry.register(counter_viewed_question.labels(group=QUESTION))

counter_push_question = Counter('user_push_question',
                                METRIC_NAMES['user_push_question_total'],
                                ['group'])
registry.register(counter_push_question.labels(group=QUESTION))

"""Узнать о Федерации."""
counter_viewed_federation = Counter(
    'user_viewed_federation',
    METRIC_NAMES['user_viewed_federation_total'],
    ['group'])
registry.register(counter_viewed_federation.labels(group=FEDERATION))

counter_viewed_federation_values = Counter(
    'user_viewed_federation_values',
    METRIC_NAMES['user_viewed_federation_values_total'],
    ['group'])
registry.register(counter_viewed_federation_values.labels(group=FEDERATION))

counter_viewed_federation_activities = Counter(
    'user_viewed_federation_activities',
    METRIC_NAMES['user_viewed_federation_activities_total'],
    ['group'])
registry.register(
    counter_viewed_federation_activities.labels(group=FEDERATION))

"""Адаптивные виды хоккея"""
counter_viewed_adaptive_hockey = Counter(
    'user_viewed_adaptive_hockey',
    METRIC_NAMES['user_viewed_adaptive_hockey_total'],
    ['group'])
registry.register(
    counter_viewed_adaptive_hockey.labels(group=ADAPTIVE_HOKKEY))

counter_viewed_sledzh_hockey = Counter(
    'user_viewed_sledzh_hockey',
    METRIC_NAMES['user_viewed_sledzh_hockey_total'],
    ['group'])
registry.register(counter_viewed_sledzh_hockey.labels(group=ADAPTIVE_HOKKEY))

counter_viewed_hockey_for_blind = Counter(
    'user_viewed_hockey_for_blind',
    METRIC_NAMES['user_viewed_hockey_for_blind_total'],
    ['group'])
registry.register(
    counter_viewed_hockey_for_blind.labels(group=ADAPTIVE_HOKKEY))

counter_viewed_special_hockey = Counter(
    'user_viewed_special_hockey',
    METRIC_NAMES['user_viewed_special_hockey_total'],
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
                                METRIC_NAMES['user_viewed_donate_total'],
                                ['group'])
registry.register(counter_viewed_donate.labels(group=DONATE))

counter_push_donate = Counter('user_push_donate',
                              METRIC_NAMES['user_push_donate_total'],
                              ['group'])
registry.register(counter_push_donate.labels(group=DONATE))

"""Квиз."""
counter_viewed_quiz = Counter('user_viewed_quiz',
                              METRIC_NAMES['user_viewed_quiz_total'],
                              ['group'])
registry.register(counter_viewed_quiz.labels(group=QUIZ))

counter_push_quiz_start = Counter('user_push_quiz_start',
                                  METRIC_NAMES['user_push_quiz_start_total'],
                                  ['group'])
registry.register(counter_push_quiz_start.labels(group=QUIZ))

counter_viewed_quiz_res = Counter(
    'user_viewed_quiz_result',
    METRIC_NAMES['user_viewed_quiz_result_total'],
    ['group'])
registry.register(counter_viewed_quiz_res.labels(group=QUIZ))

FUNC = {}
for number in range(11):
    FUNC['quiz_res_' + str(number)] = Counter(
        'user_viewed_quiz_result_' + str(number),
        'Результат игры квиз ' + str(number),
        ['group'])
    registry.register(
        FUNC['quiz_res_' + str(number)].labels(group=QUIZ))

"""Кто такой Фырк."""
counter_viewed_who_is_fyrk = Counter(
    'user_viewed_who_is_fyrk',
    METRIC_NAMES['user_viewed_who_is_fyrk_total'],
    ['group'])
registry.register(counter_viewed_who_is_fyrk.labels(group=WHO_IS_FYRK))
