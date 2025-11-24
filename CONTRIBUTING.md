# 🛠️ Руководство по разработке

## 🚀 Начало работы

1. Форкните репозиторий
2. Клонируйте ваш форк:
   ```bash
   git clone https://github.com/ваш-username/tp-project.git
   cd tp-project
   ```
3. Создайте ветку для ваших изменений:
   ```bash
   git checkout -b feature/ваша-фича
   ```

## 🔧 Настройка окружения

1. Установите зависимости:
   ```bash
   poetry install
   ```

2. Настройте pre-commit хуки:
   ```bash
   poetry run pre-commit install
   ```

3. Настройте `.env` файл:
   ```bash
   cp example.env .env
   ```

## 📝 Процесс разработки

1. Внесите изменения в коде

2. Pre-commit хуки автоматически проверят код при коммите:
   - `ruff` - проверка и автоисправление стиля кода
   - `ruff-format` - форматирование кода

3. Если нужно запустить проверки вручную:
   ```bash
   # Проверка стиля кода
   poetry run ruff check .
   
   # Форматирование кода
   poetry run ruff format .
   
   # Запуск всех pre-commit хуков
   poetry run pre-commit run --all-files
   ```

4. Проверьте, что приложение запускается:
   ```bash
   poetry run uvicorn tp_project.main:app --reload
   ```

## 📤 Отправка изменений

1. Закоммитьте изменения:
   ```bash
   git add .
   git commit -m "Описание ваших изменений"
   ```

2. Отправьте изменения в ваш форк:
   ```bash
   git push origin feature/ваша-фича
   ```

3. Создайте Pull Request на GitHub

4. **CI автоматически проверит ваш код** при создании PR:
   - Проверка стиля кода (`ruff check`)
   - Проверка форматирования (`ruff format --check`)
   - Запуск тестов (`pytest`)