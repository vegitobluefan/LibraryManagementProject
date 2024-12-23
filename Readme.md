# Library Management System

## Описание проекта

Library Management System — это консольное приложение для управления библиотекой. Система позволяет добавлять, удалять и искать книги, обновлять их статусы, а также сохранять и загружать данные из текстового файла.

Проект создан на языке Python, с акцентом на простоту и удобство использования. Он предоставляет базовую функциональность для работы с каталогом библиотеки и хранит данные в формате текста без использования сторонних библиотек.

Также было реализовано тестирование основного функционала приложения при помощи unittest.

---
## Основной функционал
- **Добавление книги**: Укажите название, автора и год издания для добавления новой книги в библиотеку.
- **Удаление книги**: Удаление книги по уникальному идентификатору (ID).
- **Поиск книг**: Возможность поиска по названию, автору или году издания.
- **Отображение всех книг**: Просмотр списка всех книг в библиотеке с деталями.
- **Обновление статуса книги**: Обновите статус книги (например, "в наличии" или "выдана").
- **Сохранение данных**: Сохраняет текущее состояние библиотеки в текстовый файл.
- **Загрузка данных**: Загружает данные библиотеки из текстового файла.
---

## Структура данных

Книга представлена классом `Book` с полями:
- `id` — уникальный идентификатор.
- `title` — название книги.
- `author` — автор книги.
- `year` — год издания.
- `status` — статус книги ("в наличии" или "выдана").
Переопределяет метод __str__ для удобного отображения данных книги.


Библиотека представлена классом `Library`, управляющим коллекцией книг и содержащим методы для взаимодействия с ними:     
- `add_book`: Добавляет новую книгу, проверяя дубликаты и корректность данных.
- `remove_book`: Удаляет книгу по ID.
- `find_books`: Ищет книги по названию, автору или году.
- `display_books`: Отображает все книги.
- `update_book_status`: Изменяет статус книги.
- `save_data_to_file`: Сохраняет данные в файл library.txt.
-  `load_data_from_file`: Выгружает данные из файла library.txt.

---

## Установка
1. Склонируйте репозиторий или загрузите проект на ваш локальный компьютер:
```bash 
git clone ...
``` 
2. Запустите проект:
 ```bash 
python library.py 
```
   
## Использование
После запуска программы вам будет предложено меню с действиями:

Меню:
1. Добавить книгу            
2. Удалить книгу              
3. Найти книгу по названию, автору или году                 
4. Показать все книги                
5. Изменить статус книги                  
6. Сохранить библиотеку                  
7. Загрузить библиотеку                
8. Выход
                 
Примеры команд:               
- Добавление книги:
```bash
Выберите действие: 1           
Введите название книги: Война и мир             
Введите автора книги: Лев Толстой              
Введите год издания: 1869             
Книга 'Война и мир' добавлена в библиотеку.            
```

- Поиск книги:
```bash
Выберите действие: 3
Введите название, автора или год для поиска: Лев Толстой
Найденные книги:
id: 1, Название: Война и мир, Автор: Лев Толстой, Год издания: 1869, Статус: в наличии
```
- Сохранение данных:
```bash
Выберите действие: 6
Данные успешно сохранены в файл library.txt.
```

- Загрузка данных:
```bash
1, Война и мир, Лев Толстой, 1869, в наличии
2, Преступление и наказание, Федор Достоевский, 1866, выдана
3, Мастер и Маргарита, Михаил Булгаков, 1940, в наличии
Каждая строка представляет отдельную книгу.
```

- Запуск тестов:
```bash
python -m unittest test_library.py
```

### Лицензия
Этот проект является учебным и может быть свободно использован для личных или образовательных целей.

## Разработчик: [Аринов Данияр](https://github.com/vegitobluefan)