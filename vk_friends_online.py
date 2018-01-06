#!/usr/bin/env python3


import vk
import getpass
import sys
import os


APP_ID = 6319840
# чтобы получить app_id,
# нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input("Введите логин от своего аккаунта в vk.com"
                  "(e-mail или номер телефона):\n")
    return login


def get_user_password():
    password = getpass.getpass(
        prompt="Введите пароль от своего аккаунта в vk.com:\n"
    )
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api_connection_context = vk.API(session)
    friends = api_connection_context.friends.get(fields="online")
    online_friends_list = []
    positive_online_status = 1
    for friend in friends:
        if friend["online"] == positive_online_status:
            online_friends_list.append(friend)
    return online_friends_list


def print_online_friends(online_friends_list):
    print(
        "--------------------------------------"
        "\nКто из Ваших друзей сейчас на связи :"
        "\n-------------------------------------"
    )
    for friend_online in online_friends_list:
        print("{} {}".format(
                friend_online["first_name"],
                friend_online["last_name"]
            ))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online_list = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit("Указаны неверные логин/пароль."
                 "\nПерезапустите программу и укажите корректные креденшилы")
    print_online_friends(friends_online_list)
