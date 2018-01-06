## 1.Что это такое ?

Этот код позволяет сформировать и отобразить спискок друзей со страницы в vk.com

## 2.Системные требования
Для работы с программой понадобится Python3.5 (который скорее всего у вас уже установлен, если Вы используете Linux)  
Также может понадобиться установить модуль `vk`, сделать это можно выполнив `pip3 install -r requirements.txt`
```
# pip3 install -r requirements.txt
```

## 3.Где можно скачать  
Можно форкнуть здесь - [кто из друзей онлайн ?](https://github.com/aligang/8_vk_friends_online)  
и затем скачать 
```
git clone https://github.com/<юзернейм-аккаунта-на-гите>/8_vk_friends_online
```

## 4.Как этим пользоваться...  
*a.Данный код может быть исползован как самостоятельная программа,*  
*при этом программа запросит логин/пароль от вашей учётной записи в vk.com

```bash
$  python3 vk_friends_online.py 
Введите логин от своего аккаунта в vk.com(e-mail или номер телефона):
usermail@gmail.com
Введите пароль от своего аккаунта в vk.com:

--------------------------------------
Кто из Ваших друзей сейчас на связи :
-------------------------------------
John Doe
Jane Doe

```

## 5.Какие функции могут быть переиспользованы в вашем коде
Функция `get_online_friends` формирует список словарей, в которых указана информация  
о друзьях со статусом "online"  
Функция `print_online_friends` выводит список, полученный на выходе функции `get_online_friends`,
на поток ввода-вывода в человекочитаемом виде

Импортировать и использовать функцию коди можно  следующим образом:  
```python
from vk_friends_online import get_online_friends
from lang_frequency import get_most_frequent_words


friends_online_list = get_online_friends(login, password)
```

## 6. Цели
Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)