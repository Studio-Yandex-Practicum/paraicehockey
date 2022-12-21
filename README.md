[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/) [![badge](https://img.shields.io/badge/-Python_telegram_bot-008080)](https://github.com/python-telegram-bot/python-telegram-bot/blob/680cca8262ab3e8dc00916ec523b9e015db5bc22/docs/source/telegram.ext.rst) 

# Project Paraicehockey  

## Содержание
1. [О чём проект?](#about)
2. [Структура проекта](#structure)
3. [Подготовка к запуску](#start)

    3.1. [Клонирование проекта из репозитория](#clone)

    3.2. [Настройка poetry](#poetry)
    
    3.3. [Настройка переменных окружения](#env)

4. [Запуск бота](#run-bot)

# 1. О чём проект? <a id="about"></a>

Телеграм-бот для НКО “Федерация адаптивного хоккея”, который поможет пользователям познакомиться с ее деятельностью, получить информацию о мероприятиях и проектах, которые она организует, задать вопрос сотрудникам.

**“Федерация адаптивного хоккея”** - некоммерческая организация, которая создает условия для развития адаптивных видов хоккея в России, повышает их роль в социальной реабилитации детей с инвалидностью. Например, обучает тренеров, судей, волонтеров-пушеров (помощников на коньках), поддерживает новые и действующие команды, содействует разработке специального спортивного инвентаря, организует мероприятия – турниры, летний инклюзивный лагерь, интенсивы. 

Федерация — единственная в России организация, которая занимается развитием адаптивного хоккея для детей на системном уровне и объединяет детские команды со всех уголков страны.

**Сайт Федерации** - [https://paraicehockey.ru/federatsiya-adaptivnogo-hokkeya/](https://paraicehockey.ru/federatsiya-adaptivnogo-hokkeya/)


**Телеграм - канал** - [https://t.me/paraicehockey](https://t.me/paraicehockey)

# 2. Структура проекта <a id="structure"></a>

Нужно дописать


# 3. Подготовка к запуску <a id="start"></a>

## 3.1. Клонирование проекта из репозитория<a id="clone"></a>

Clone the repository to your computer:

```
git@github.com:Studio-Yandex-Practicum/paraicehockey.git
```

## 3.2. Poetry (инструмент для работы с виртуальным окружением и сборки пакетов)<a id="poetry"></a>:

Poetry - это инструмент для управления зависимостями и виртуальными окружениями, также может использоваться для сборки пакетов.

<details>
 <summary>
 Как скачать и установить?
 </summary>

### Установка:

Установите poetry следуя [инструкции с официального сайта](https://python-poetry.org/docs/#installation).
<details>
 <summary>
 Команды для установки:
 </summary>
Для UNIX-систем и Bash on Windows вводим в консоль следующую команду:

> *curl -sSL https://install.python-poetry.org | python -*
Для WINDOWS PowerShell:

> *(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -*
</details>
<br>
После установки перезапустите оболочку и введите команду
> poetry --version
Если установка прошла успешно, вы получите ответ в формате

> Poetry (version 1.2.0)
Для дальнейшей работы введите команду:

> poetry config virtualenvs.in-project true
Выполнение данной команды необходимо для создания виртуального окружения в
папке проекта.

После предыдущей команды создадим виртуальное окружение нашего проекта с
помощью команды:

> poetry install
Результатом выполнения команды станет создание в корне проекта папки .venv.
Зависимости для создания окружения берутся из файлов poetry.lock (приоритетнее)
и pyproject.toml

Для добавления новой зависимости в окружение необходимо выполнить команду

> poetry add <package_name>
_Пример использования:_

> poetry add requests
Также poetry позволяет разделять зависимости необходимые для разработки, от
основных.
Для добавления зависимости необходимой для разработки и тестирования необходимо
добавить флаг ***--dev***

> poetry add <package_name> --dev
_Пример использования:_

> poetry add flake8 --dev
</details>

<details>
 <summary>
 Порядок работы после настройки
 </summary>

<br>

Чтобы активировать виртуальное окружение, введите команду:

> poetry shell
Существует возможность запуска скриптов и команд с помощью команды без
активации окружения:

> poetry run <script_name>.py
_Примеры:_

> poetry run python <script_name>.py
>
> poetry run pytest
>
> poetry run black
Порядок работы в оболочке не меняется. Пример команды для Win:

> python bin\main.py
Доступен стандартный метод работы с активацией окружения в терминале с помощью команд:

Для WINDOWS:

> source .venv/Scripts/activate
Для UNIX:

> source .venv/bin/activate
</details>


## 3.3. Настройка переменных окружения <a id="env"></a>

Перед запуском проекта необходимо создать копию файла
```.env_example```, назвав его ```.env``` и установить значение токена бота

# 4. Запуск бота <a id="run-bot"></a>

В процессе разработки отладка производится на личном боте, для этого нужно в файле .env в переменной BOT_TOKEN указать токен вашего бота.
Запуск бота командой: 
```python main.py ```
В проект добавлен pre-commit для предварительной проверки flake8 и isort перед commit:
Он должен быть установлен глобально, а не в виртуальном окружении проекта, где вы собираетесь его использовать.
```pip install --user pre-commit```

Теперь включим pre-commit в текущем репозитории.

```pre-commit install```

Проверим, что конфигурационный файл валиден, а заодно и что всё нынешнее содержимое репозитория удовлетворяет описанными правилам:

```pre-commit run --all-files```


###
1. Бот зарегистрирован
2. Имя paraicehockeybot
3. Техническое имя paraicehockeybot

4. Use this token to access the HTTP API: 5822407132:AAHA6ySgbmAIQ9NHh-xIxKw9_iN_kPgsTgw Keep your token secure and store it safely, it can be used by anyone to control your bot.

5. Сделал продакт сервер, запустил бот. ubuntu@130.255.170.24 Pleheranar0116
6. Можно проверить в телеграм @paraicehockeybot (отправьте любое сообщение или /start)


#### Author
-

- [Sukharev Kirill](https://github.com/Soliton80)
- [Kolosova Ekaterina](https://github.com/Ekaterina-Kolosova)
-
-
