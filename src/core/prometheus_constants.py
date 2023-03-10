from src.core.prometheus import (counter_viewed_hockey_for_blind,
                                 counter_viewed_sledzh_hockey,
                                 counter_viewed_special_hockey)

ADAPTIVE_HOKKEY_PROMETHEUS = {
    'sledzh_hockey': counter_viewed_sledzh_hockey,
    'special_hockey': counter_viewed_special_hockey,
    'hockey_for_blind': counter_viewed_hockey_for_blind
}
QUESTION = 'Question'
OWNER = 'Owner'
FEDERATION = 'Federation'
ADAPTIVE_HOKKEY = 'AdaptiveHockey'
