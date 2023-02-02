CHAMPION_WAY_URL = 'https://paraicehockey.ru/mobilnoe-prilozhenie/'

ADAPTIVE_HOKKEY_MAIN_TEXT = """В командах Федерации тренируются более 900 ребят
 в 31 регионе России. Мы развиваем три направления адаптивного хоккея:
1. Следж-хоккей (48 команд)
2. Хоккей для незрячих (10 команд)
3. Специальный хоккей для детей с интеллектуальными особенностями
 (13 команд)."""

SLEDZH_TEAMS_URL = 'https://paraicehockey.ru/teams-type/komandy-sledzh-hokkey/'

SPECIAL_TEAMS_URL = 'https://paraicehockey.ru/teams-type/spetsialnyy-hokkey/'

BLIND_TEAMS_URL = 'https://paraicehockey.ru/teams-type/hokkey-dlya-nezryachih/'

SLEDZH_PHOTO1 = 'src/static/images/sledj_1.png'
SLEDZH_PHOTO2 = 'src/static/images/sledj_2.png'
SPECIAL_HOCK1 = 'src/static/images/special_hockey_1.png'
SPECIAL_HOCK2 = 'src/static/images/special_hockey_2.png'
BLIND_PHOTO1 = 'src/static/images/blind_hockey_1.png'
BLIND_PHOTO2 = 'src/static/images/blind_hockey_2.png'

ADAPTIVE_HOKKEY_PAGES_TEXT_URLS = {
    'sledzh_hockey': [SLEDZH_TEAMS_URL, SLEDZH_PHOTO1, SLEDZH_PHOTO2],
    'special_hockey': [SPECIAL_TEAMS_URL, SPECIAL_HOCK1, SPECIAL_HOCK2],
    'hockey_for_blind': [BLIND_TEAMS_URL, BLIND_PHOTO1, BLIND_PHOTO2]
}

ALL_FOR_HOKKEY_MAIN_TEXT = """Привет, друг!
Здесь ты можешь приобрести экипировку и инвентарь для игры!"""

HOCKEY_EQUIPMENT_URL = 'https://hockey-family.com/equipment/'

ATTRIBUTES_SHOP_URL = 'https://kolosova411.pythonanywhere.com/'

STICKERS_URL = 'https://t.me/addstickers/the_world_of_hockey'

quizzes = [
    [
        'Кто изображен на фото?',
        [
            'Всеволод Бобров',
            'Игорь Ларионов',
            'Валерий Харламов'
        ],
        '0',
        'Всеволод Бобров',
        'src/static/images/portrait.jpg',
    ],
    [
        'Какая страна считается родоначальником хоккея с шайбой?',
        ['Канада', 'США', 'СССР'],
        '0',
        'Канада'
    ],
    [
        'Выберете по возрастанию игроков которые играли давно,недавно,сейчас',
        [
            'Горди Хоу, Харламов, Мозякин, Панарин',
            'Мозякин, Панарин, Мозякин, Харламов',
            'Мозякин, Мозякин, Харламов, Панарин'
        ],
        '0',
        'Горди Хоу, Харламов, Мозякин, Панарин'
    ],
    [
        'Первый российский вратарь получивший приз "Везина трофи"',
        [
            'Илья Брызгалов',
            'Евгений Набоков',
            'Владислав Третьяк',
            'Сергей Бобровский'
        ],
        '3',
        'Сергей Бобровский'
    ],
    [
        'Какая страна завоевала больше всех золотых медалей чемпионата мира?',
        [
            'Канада',
            'США',
            'СССР/Россия',
            'Финляндия'
        ],
        '2',
        'СССР/Россия'
    ],
    [
        'Где хоккейную шайбу хранят перед игрой?',
        [
            'На льду',
            'В морозильной камере',
            'В судейской',
            'В раздевалке'
        ],
        '1',
        'В морозильной камере'
    ],
    [
        'Какая из этих стран выигрывала Чемпионат мира по хоккею?',
        [
            'Венгрия',
            'Великобритания',
            'Словения',
            'Франция'
        ],
        '1',
        'Великобритания'
    ],
    [
        'Самый титулованный хоккейный клуб в новейшей истории России',
        [
            'Динамо (Москва)',
            'Ак Барс (Казань)',
            'Металлург (Магнитогорск)',
            'Локомотив (Ярославль)'
        ],
        '1',
        'Ак Барс (Казань)'
    ],
    [
        'Это клюшка для...',
        [
            'Хоккея с шайбой',
            'Следж-хоккея',
            'Хоккея с мячом',
            'Гольфа'
        ],
        '2',
        'Хоккея с мячом',
        'src/static/images/stick.jpg',
    ],
    [
        'Сколько клюшек у следж-хоккейного вратаря?',
        [
            'Ни одной',
            'Одна',
            'Две',
            'У всех по-разному'
        ],
        '1',
        'Одна'
    ]
]

quiz_results = {
    0: 'src/static/images/quiz/0.png',
    1: 'src/static/images/quiz/1.png',
    2: 'src/static/images/quiz/2.png',
    3: 'src/static/images/quiz/3.png',
    4: 'src/static/images/quiz/4.png',
    5: 'src/static/images/quiz/5.png',
    6: 'src/static/images/quiz/6.png',
    7: 'src/static/images/quiz/7.png',
    8: 'src/static/images/quiz/8.png',
    9: 'src/static/images/quiz/9.png',
    10: 'src/static/images/quiz/10.png',
}

QUESTION_TEXT = """На связи Фырк. Я енот, но это не мешает мне соединить тебя
с сотрудниками Федерации. Просто перейди в чат с сотрудником и тебе ответят."""
