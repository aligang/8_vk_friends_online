#!/usr/bin/env python3


import vk
import getpass
import sys


APP_ID = 6319840


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
        scope="friends"
    )
    api_connection_context = vk.API(session)
    online_friends_id_list = api_connection_context.friends.getOnline()
    online_friends_list = api_connection_context.users.get(
        user_ids=online_friends_id_list
    )
    return online_friends_list


def print_online_friends(online_friends_list):
    print(
        "-------------------------------------"
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
                 "\nПерезапустите программу и "
                 "укажите корректные логин и пароль")
    print_online_friends(friends_online_list)
