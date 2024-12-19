# Конвертер JSON в пользовательский конфигурационный язык

## Описание
Этот инструмент преобразует данные из формата JSON в пользовательский формат конфигурационного языка. Он поддерживает обработку массивов, числовых значений и строковых констант, а также выявляет синтаксические ошибки.

## Возможности
- Конвертирует ключи и значения JSON в указанный формат конфигурационного языка.
- Поддерживает вычисление массивов в постфиксной нотации.
- Проверяет синтаксис ключей и значений.
- Сообщает о синтаксических ошибках с подробным описанием.
- Предоставляет интерфейс командной строки для указания входных и выходных файлов.

## Требования
- Python версии 3.7 или выше.

## Установка
1. Клонируйте или загрузите репозиторий.
2. Сохраните основной скрипт Python как `converter.py`.
3. Убедитесь, что Python установлен и добавлен в PATH.

## Использование
### Интерфейс командной строки
Запустите скрипт с помощью следующей команды:

```bash
python converter.py --input <путь_к_входному_json> --output <путь_к_выходному_конфигу>
```

### Пример
#### Входной JSON (`input.json`):
```json
{
    "AA": [1, 2, 3],
    "BB": 10,
    "CC": "CONSTANT",
    "DD": [4, 5],
    "LEN_EXAMPLE": [10, 20],
    "RESULT": [10, 5, 3]
}
```

#### Команда:
```bash
python converter.py --input input.json --output output.txt
```

#### Выходной конфиг (`output.txt`):
```
var AA 6;
var BB 10;
var CC CONSTANT;
var DD 9;
var LEN_EXAMPLE 2;
var RESULT 18;
```

## Основные моменты
### Правила синтаксиса
- **Имена ключей**: Должны соответствовать регулярному выражению `[A-Z_]+`.
- **Типы значений**:
  - Числа (например, `10`)
  - Строки (только заглавные буквы, например, `"CONSTANT"`)
  - Массивы (например, `[1, 2, 3]`, вычисляются как `6`)
- **Формат вывода**: `var <КЛЮЧ> <ЗНАЧЕНИЕ>;`

### Обработка ошибок
- Неверный синтаксис JSON или отсутствие файла.
- Неподдерживаемые форматы ключей или значений.
- Ошибки при вычислении постфиксного выражения.

## Тестирование
- Создавайте JSON-файлы для тестирования всех поддерживаемых функций.
- Запускайте скрипт и проверяйте файл вывода на корректность.

### Примеры тестовых случаев
1. **Корректный ввод**:
   - Числовые константы, массивы и допустимые строки.

2. **Некорректный ввод**:
   - Ключи с недопустимыми символами (например, `"key1"`).
   - Массивы со смешанными типами данных (например, `[1, "строка"]`).

## Устранение неисправностей
- Убедитесь, что JSON-файл корректен и правильно отформатирован.
- Проверьте правильность пути к входному файлу.
- Ознакомьтесь с сообщениями об ошибках для выявления конкретных проблем с синтаксисом.


### Выполнение теста 
![image](https://github.com/user-attachments/assets/782c3029-bc2c-46f5-87ab-2d412d10214d)
