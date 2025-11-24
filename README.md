# 💱 Конвертер валют и температур

**Конвертер валют и температур** — это REST API приложение для конвертации валют и температур. Система использует актуальные курсы валют через ExchangeRate API и выполняет локальную конвертацию температур между различными единицами измерения.

## 🚀 Основные функции

- **💵 Конвертация валют** - Актуальные курсы валют через ExchangeRate API, поддержка всех основных мировых валют, автоматическая конвертация с высокой точностью

- **🌡️ Конвертация температур** - Локальная конвертация без внешних зависимостей, поддержка Цельсия (C), Фаренгейта (F) и Кельвина (K), высокая скорость обработки

- **📋 REST API** - Простые GET endpoints для интеграции, автоматическая валидация данных через Pydantic, детальная обработка ошибок

- **📚 Swagger UI** - Интерактивная документация API, возможность тестирования прямо из браузера, полное описание всех endpoints

## 📦 Установка

### 🔧 Предварительные требования
- **Python 3.11+** и **Poetry**

```bash
# Клонировать репозиторий
git clone https://github.com/avolxn/tp-project.git
cd tp-project

# Настроить окружение
cp example.env .env
```

### 🧩 Отредактируйте `.env` файл

```env
CURRENCY_API_KEY=YOUR_API_KEY
CURRENCY_BASE_URL=https://v6.exchangerate-api.com/v6
```

## 🔑 Получение API ключа

### ExchangeRate API
1. Зарегистрируйтесь на [ExchangeRate-API](https://www.exchangerate-api.com/)
2. Получите бесплатный API ключ в личном кабинете (1500 запросов/месяц)
3. Скопируйте ключ в переменную `CURRENCY_API_KEY` в файле `.env`

## ▶️ Запуск

### 🧪 С Poetry

```bash
# Установка зависимостей
poetry install

# Запуск сервера
poetry run uvicorn tp_project.app:app --reload
```

Сервер запустится на `http://127.0.0.1:8000`

## 💻 Использование API

>🔗 API: `http://localhost:8000`

>📘 Swagger UI: `http://localhost:8000/docs`

### 💵 Конвертация валют

**GET** `/currency/convert`

**Параметры:**
- `amount` (float) - Сумма для конвертации
- `from_currency` (str) - Код валюты из (например, USD)
- `to_currency` (str) - Код валюты в (например, EUR)

**Пример запроса:**
```bash
curl "http://localhost:8000/currency/convert?amount=100&from_currency=USD&to_currency=EUR"
```

**Пример ответа:**
```json
{
  "amount": 100.0,
  "from_currency": "USD",
  "to_currency": "EUR",
  "result": 92.50
}
```

### 🌡️ Конвертация температур

**GET** `/temperature/convert`

**Параметры:**
- `temperature` (float) - Температура для конвертации
- `from_unit` (str) - Единица измерения из (C, F или K)
- `to_unit` (str) - Единица измерения в (C, F или K)

**Пример запроса:**
```bash
curl "http://localhost:8000/temperature/convert?temperature=100&from_unit=C&to_unit=F"
```

**Пример ответа:**
```json
{
  "temperature": 100.0,
  "from_unit": "C",
  "to_unit": "F",
  "result": 212.0
}
```

**Поддерживаемые единицы:**
- `C` - Цельсий (Celsius)
- `F` - Фаренгейт (Fahrenheit)
- `K` - Кельвин (Kelvin)

## 🛠️ Технологический стек

- **FastAPI** - Фреймворк для создания REST API
- **Pydantic** - Валидация данных и настроек
- **Requests** - HTTP клиент для работы с внешними API
- **Poetry** - Управление зависимостями Python
- **ExchangeRate API** - Источник актуальных курсов валют

## 🏗️ Структура проекта

```
tp-project/
├── src/
│   └── tp_project/
│       ├── api/                       # API endpoints
│       │   ├── router.py              # Главный роутер
│       │   ├── currency.py            # Endpoints валют
│       │   └── temperature.py         # Endpoints температур
│       ├── core/                      # Конфигурация
│       │   └── config.py              # Настройки приложения
│       ├── schemas/                   # Pydantic модели
│       │   ├── currency.py            # Схемы валют
│       │   └── temperature.py         # Схемы температур
│       ├── services/                  # Бизнес-логика
│       │   ├── currency.py            # Сервис конвертации валют
│       │   └── temperature.py         # Сервис конвертации температур
│       ├── app.py                     # Приложение FastAPI
│       └── main.py                    # Точка входа приложения
├── tests/                             # Тесты
│   ├── test_currency.py               # Тесты валют
│   ├── test_temperature.py            # Тесты температур
│   └── test_api.py                    # Тесты API
├── example.env                        # Пример файла окружения
├── pyproject.toml                     # Конфигурация Poetry
├── poetry.lock                        # Lock файл зависимостей
├── LICENSE                            # Лицензия MIT
└── README.md                          # Документация
```

## 📄 Лицензия

Этот проект распространяется под лицензией **MIT**. Подробности в файле [LICENSE](LICENSE).