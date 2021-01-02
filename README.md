# LiteBot

![banner](banner/twitter_header_photo_2.png)

> Мы не несем ответственности за ваш аккаунт, у нас есть базовый объект защиты, но он не гарантирует 100% защиту от скам модулей!

<details markdown='1'><summary>Меню</summary>

[Установка](#установка)

[Конфигурация](#конфигурация)
<details markdown='1'><summary>Документация</summary>

[Loader](#loader)

[Protection](#protection)

[Utils](#utils)

[Создание своего модуля](#создание-своего-модуля)
</details>

</details>

## Установка


### Установка зависимостей

#### Ubuntu
```bash
apt install git python3 python3-pip python3-dev
```

#### Alpine
```bash
apk add git python3 py3-pip python3-dev
```

#### Arch/Manjaro
```bash
pamcan -S git python3 python3-pip python3-dev
```

#### Termux
```bash
pkg install git python
```

### Копипование репозитория и переход в рабочую дирректорию
```bash
git clone https://github.com/DarkGa/LiteBot.git && cd LiteBot
```

### Установка зависимостей
```bash
pip3 install -r requirements.txt
```

## Конфигурация

Основной файл конфигурации `config.ini`, открыв его мы увидим api_id и api_hash, получаем их [тут](https://my.telegram.org) и подставляем.

Далее запускаем бота командой:
```bash
python3 main.py
```

После не долгого ожидания вам предложат ввести номер телефона и подтвердить его чеоез код.

## Loader

```python
core.loader.loader.modules()
```

> Получить список модулей в формате `.module`

> return list(modules)

```python
core.loader.loader.unload(module)
```
> module - название модуля 

Позволяет отгрузить модуль для работы с файлом (при вызове модуля он все еще будет работать).

```python
core.loader.loader.load(module)
```
> module - название модуля 

> Импортирует модуль для использования в будущем.

> return <module 'module_name' from '/path/to/module_name.py'>

```python
core.loader.loader.reload(module)
```
> module - название модуля 

> Позволяет перезагрузить модуль.

```python
core.loader.loader.init()
```

> Позволяет загрузить все модули (используется при старте бота)

## Protection

```python
core.protector.protector.scan(module)
```
> module - название модуля 

> Проверяет модуль на предмет запрещенных строк

> return str(logs)

## Utils

```python
core.utils.utils.buffer
```

> Класс буфера для хранения данных

```python
core.utils.utils.buffer.write(data: list)
```

> Функция для записи данных в буфер для последующего использования

> Принимает данные ввиде списка [ключ, данные]

```python
core.utils.utils.buffer.read(data: str)
```

> Функция для чтения данных из буфера для последующего использования

> Принимает название ключа

> return data

```python
core.utils.utils.buffer.clean(data: str)
```

> Функция для очистки данных в буфере

> Принимает название ключа


```python
core.utils.utils.bash(code: str)
```

> Функция для выполнения bash кода и возврата ответа (если есть)

> Принимает код bash скрипта

> return str(output)


```python
core.utils.utils.db
```

> Класс для работы с базой данных бота

```python
core.utils.utils.db.create_table(table: str, column: str)
```

> Функция для создании таблицы с колонкой

> Принимает название таблицы и колонки

```python
core.utils.utils.db.add_table(table: str, column: str)
```

> Функция для добавления в таблицу новой колонки

> Принимает название таблицы и колонки

```python
core.utils.utils.db.insert_into(table: str, column: str, data)
```

> Функция для записи данных в колонку таблицы

> Принимает название таблицы, колонки и данных

```python
core.utils.utils.db.update(table: str, column: str, data)
```

> Функция для обновлении данных в колонке таблицы

> Принимает название таблицы, колонки и данных

```python
core.utils.utils.db.drop_table(table: str)
```

> Функция для удаления таблицы

> Принимает название таблицы

```python
core.utils.utils.db.select(table: str, column: str)
```

> Функция для получения данных из колонки таблицы

> Принимает название таблицы и колонки

> return list(data)

## Создание своего модуля

> Все модули дожны использовать ассинхронную функцию 

### Стандартное дерево модуля
```python
import modules

class Main:

	version=''
	info=''
	group=''

	async def init(app, m):
		*code*
```
> Строки "version, info, group" не обязательны, но рекомендуется их заполнять для лучшего взаемодействия с пользователем.

### Давайте напишем простой модуль для вывода рандомного числа от 0 до 100

```python
import random

class Main:
	
	async def init(app, m):
		
		await m.edit(f"Получилось число {random.randint(0, 101)}")
```

Мы написали простейший модуль для бота, теперь закинем его в папку modules и перезагрузим модули командой `.reload`


Мой телеграм: https://t.me/mozahist228

Канал с модулями и новостями: https://t.me/LiteBotMN

LiteBot v1.0.8, Copyright (C) 2020-2021 DarkGamer <https://github.com/DarkGa>
Licensed under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE v3
