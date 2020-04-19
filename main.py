#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import random
import re
import vk_api, random
import Constants
from vk_api.longpoll import *
from vk_api.utils import get_random_id
from keyboard import *
from func import *
from lk import *
from dbworker import *

ans = Constants

token = os.environ.get('TOKEN_SGSPU')

vk_session = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()
print('Соединение установлено...')

dictStart = '''
Вот что я умею:

🔔 /расписание - Просмотреть расписание 
⏲️ /звонок - Сколько до конца пары? 
📣 /объявления - Показать объявления 
👨‍🏫 /преподаватели - Найти преподавателя 
👩‍💻 /студенты - Найти студента 
🗓 /неделя - Что за неделя? 
'''
dictReg = '''
⚠Введите название группы:
пример ниже:

Моя группа - ФМФИ-б18ПИо
'''
global Random

def random_id():
    Random = 0
    Random += random.randint(0, 1000000000);
    return Random

def elsereg():
    vk.messages.send(
    user_id=event.user_id,
    message="Вы не зарегистрированы, нажмите на кнопку 'Регистрация'",
    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
    random_id=random_id()
)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            mygroup =get_user_group(event.user_id)
            msg = event.text.lower()
            if not check_if_exists(event.user_id):
                register_new_user(event.user_id)

            if event.text.lower() in ('/help', 'начать', 'вернуться назад к главной'):
                if get_admin_status(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=dictStart,
                        keyboard=enable_keyboard_start_admin(),
                        random_id=random_id()
                    )
                else:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=dictStart,
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )

            elif event.text.lower() == "регистрация":
                if get_user_wish(event.user_id) == 0:
                    set_user_wish(event.user_id, 1)
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Вы успешно зарегистрированы!",
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )
                else:
                    set_user_wish(event.user_id, 0)
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Вы успешно удалены из базы!",
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )

            elif event.text.lower() in ('/rasp','/rasp_1', '🔔 расписание','/расписание', '🔔 назад к факультету','показать предыдущие факультеты'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Выберите желаемый факультет:",
                        keyboard=enable_keyboard_rasp_1(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/rasp_2','/расписание 2', 'показать следующие факультеты'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Выберите желаемый факультет:",
                        keyboard=enable_keyboard_rasp_2(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
#----------------------------------------------ФМФИ---------------------------------------------------------------------
            elif event.text.lower() in ('/fmfi', '🧮 фмфи','/фмфи', 'фмфи', '🧮 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Факультет математики, физики и информатики:',
                        keyboard=enable_keyboard_rasp_fmfi(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fmfi_2019', '🧮 2019','/фмфи_2019', 'фмфи 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fmfi_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fmfi_2018', '🧮 2018','/фмфи_2018', 'фмфи 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fmfi_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fmfi_2017', '🧮 2017','/фмфи_2017', 'фмфи 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fmfi_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fmfi_2016', '🧮 2016','/фмфи_2016', 'фмфи 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fmfi_2016(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
#----------------------------------------------ЕГФ---------------------------------------------------------------------🗺
            elif event.text.lower() in ('/egf', '🗺 егф','/егф', 'егф', '🗺 егф', '🗺 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Естественно-географический факультет:',
                        keyboard=enable_keyboard_rasp_egf(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/egf_2019', '🗺 2019','/егф_2019', 'егф 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_egf_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/egf_2018', '🗺 2018','/егф_2018', 'егф 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_egf_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/egf_2017', '🗺 2017','/егф_2017', 'егф 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_egf_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/egf_2016', '🗺 2016','/егф_2016', 'егф 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_egf_2016(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
#----------------------------------------------ФФ---------------------------------------------------------------------📚
            elif event.text.lower() in ('/ff','филфак','📚 фф','/фф', 'фф', '📚 фф', '📚 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Филологический факультет:',
                        keyboard=enable_keyboard_rasp_ff(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ff_2019', '📚 2019','/фф_2019', 'фф 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ff_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ff_2018', '📚 2018','/фф_2018', 'фф 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ff_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ff_2017', '📚 2017','/фф_2017', 'фф 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ff_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ff_2016', '📚 2016','/фф_2016', 'фф 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ff_2016(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
#----------------------------------------------ИФ---------------------------------------------------------------------
            elif event.text.lower() in ('/if','истфак','🏛 иф','/иф', 'иф', '🏛 иф', '🏛 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Исторический факультет:',
                        keyboard=enable_keyboard_rasp_if(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/if_2019', '🏛 2019','/иф_2019', 'иф 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_if_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/if_2018', '🏛 2018','/иф_2018', 'иф 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_if_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/if_2017', '🏛 2017','/иф_2017', 'иф 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_if_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/if_2016', '🧮 2016','/иф_2016', 'иф 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_if_2016(),
                        random_id=random_id()
                    )
#----------------------------------------------ФЭУС---------------------------------------------------------------------📊
            elif event.text.lower() in ('/feus','фэус','📊 фэус','/фэус', 'фэус', '📊 фэус', '📊 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Факультет экономики, упраления и сервиса: ',
                        keyboard=enable_keyboard_rasp_feus(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/feus_2019', '📊 2019','/фэус_2019', 'фэус 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_feus_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/feus_2018', '📊 2018','/фэус_2018', 'фэус 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_feus_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/feus_2017', '📊 2017','/фэус_2017', 'фэус 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_feus_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/feus_2016', '📊 2016','/фэус_2016', 'фэус 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_feus_2016(),
                        random_id=random_id()
                    )
#----------------------------------------------ФФКиС---------------------------------------------------------------------🥇
            elif event.text.lower() in ('/ffkis','ффкис','🥇 ффкис','/ффкис', 'ффкис', '🥇 ффкис', '🥇 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Факультет физической культуры и спорта:',
                        keyboard=enable_keyboard_rasp_ffkis(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ffkis_2019', '🥇 2019','/ффкис_2019', 'ффкис 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ffkis_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ffkis_2018', '🥇 2018','/ффкис_2018', 'ффкис 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ffkis_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ffkis_2017', '🥇 2017','/ффкис_2017', 'ффкис 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ffkis_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/ffkis_2016', '🥇 2016','/ффкис_2016', 'ффкис 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_ffkis_2016(),
                        random_id=random_id()
                    )
#----------------------------------------------ФПСО---------------------------------------------------------------------💑
            elif event.text.lower() in ('/fpso','фпсо','💑 фпсо','/фпсо', 'фпсо', '💑 фпсо', '💑 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Факультет психологии и специального образования:',
                        keyboard=enable_keyboard_rasp_fpso(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fpso_2019', '💑 2019','/фпсо_2019', 'фпсо 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fpso_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fpso_2018', '💑 2018','/фпсо_2018', 'фпсо 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fpso_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fpso_2017', '💑 2017','/фпсо_2017', 'фпсо 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fpso_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fpso_2016', '💑 2016','/фпсо_2016', 'фпсо 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fpso_2016(),
                        random_id=random_id()
                    )
#----------------------------------------------ФНО---------------------------------------------------------------------👪
            elif event.text.lower() in ('/fno','фно','👪 фно','/фно', 'фно', '👪 фно', '👪 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Факультет начального образования:',
                        keyboard=enable_keyboard_rasp_fno(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fno_2019', '👪 2019','/фно_2019', 'фно 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fno_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fno_2018', '👪 2018','/фно_2018', 'фно 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fno_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fno_2017', '👪 2017','/фно_2017', 'фно 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fno_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fno_2016', '👪 2016','/фно_2016', 'фно 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fno_2016(),
                        random_id=random_id()
                    )
#----------------------------------------------ФКИ---------------------------------------------------------------------🎭
            elif event.text.lower() in ('/fki','фки','🎭 фки','/фки', 'фки', '🎭 фки', '🎭 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Факультет культуры и искусства:',
                        keyboard=enable_keyboard_rasp_fki(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fki_2019', '🎭 2019','/фки_2019', 'фки 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fki_2019(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fki_2018', '🎭 2018','/фки_2018', 'фки 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fki_2018(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fki_2017', '🎭 2017','/фки_2017', 'фки 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fki_2017(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fki_2016', '🎭 2016','/фки_2016', 'фки 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fki_2016(),
                        random_id=random_id()
                    )
#----------------------------------------------ФИЯ---------------------------------------------------------------------🇬🇧
            elif event.text.lower() in ('/fib','иняз','🇬🇧 фия','/фия', 'фия', '🇬🇧 фия', '🇬🇧 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Факультет иностранных языков:',
                        keyboard=enable_keyboard_rasp_fib(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2','иняз','🇬🇧 фия','/фия', 'фия', '🇬🇧 фия', '🇬🇧 назад'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите год поступления на Естественно-географический факультет:',
                        keyboard=enable_keyboard_rasp_fib_2(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2019','/fib_2019_1', '🇬🇧 2019','/фия_2019', 'фия 2019','показать предыдущие группы фия 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2019_1(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2019_2', '🇬🇧 2019_2','/фия_2019_2', 'фия 2019_2','показать следующие группы фия 2019'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2019_2(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2018','/fib_2018_1', '🇬🇧 2018','/фия_2018', 'фия 2018','показать предыдущие группы фия 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2018_1(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2018_2', '🇬🇧 2018_2','/фия_2018_2', 'фия 2018_2','показать следующие группы фия 2018'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2018_2(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2017','/fib_2017_1', '🇬🇧 2017','/фия_2017', 'фия 2017','показать предыдущие группы фия 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2017_1(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2017_2', '🇬🇧 2017_2','/фия_2017_2', 'фия 2017_2','показать следующие группы фия 2017'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2017_2(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2016','/fib_2016_1', '🇬🇧 2016','/фия_2016', 'фия 2016','показать предыдущие группы фия 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2016_1(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text.lower() in ('/fib_2016_2', '🇬🇧 2016_2','/фия_2016_2', 'фия 2016_2','показать следующие группы фия 2016'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=ans.chooseGroup[random.randint(0,len(ans.chooseGroup)-1)],
                        keyboard=enable_keyboard_rasp_fib_2016_2(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
#-----------------------------------------------------------------------------------------------------------------------
            elif event.text.lower() in ('/zvonok', '⏲️ звонок','/звонок'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Сейчас: '+para(1)+'\n⌛Закончится через - '+str(para(2))+' минут!',
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('/ob', '📣 объявления','/объявления','объявление','/объявление'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Тут будет раздел с объявлениями: ',
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('/find_teacher', '👨‍🏫 преподаватели','/преподаватели','преподаватели','/преподаватель'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Тут будет раздел с преподавателями: ',
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )
            elif re.match(r'Моя группа', event.text):
                    mygroup_parse = re.split(r':', event.text)
                    print(mygroup_parse)
                    user_group = mygroup_parse[1]
                    set_user_group(event.user_id,user_group)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Твоя группа - %s' % user_group + '\nуспешно обновленна в базе!',
                        keyboard=enable_keyboard_my(),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('/week', '🗓 неделя','/неделя','недели','/weeks'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=''+weekFull(),
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('/week_lk', '📅 неделя', '/weeks_lk'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=''+weekFull(),
                        keyboard=enable_keyboard_my(),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('/админ', 'админ','/admin','администратор','admin','админ-панель'):
                if get_admin_status(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Админ: '+str(event.user_id),
                        keyboard=enable_keyboard_start_admin(),
                        random_id=random_id()
                    )
                elif get_admin_status(event.user_id) == 0:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Вы не являетесь администратором!',
                        keyboard=enable_keyboard_admin(),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('/week', '🗓 неделя','/неделя','недели','/weeks'):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=''+weekFull(),
                        keyboard=enable_keyboard_start(),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('/my', '✅ моё расписание','мое расписание','моё расписание','✅ мое расписание','/myrasp'):
                if (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) != 0):
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Твоя группа: '+get_user_group(event.user_id),
                        keyboard=enable_keyboard_my(),
                        random_id=random_id()
                    )
                elif (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) == 0):
                    vk.messages.send(
                        user_id=event.user_id,
                        message=dictReg,
                        keyboard=enable_keyboard_my(),
                        random_id=random_id()
                    )
            elif event.type == VkEventType.MESSAGE_NEW and event.to_me and ((re.match(r"\w\w\w\w-\w\d\d\w\w\w" ,event.text)) or (re.match(r"\w\w\w\w-\w\d\d\w\w" ,event.text))):
                if (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) != 0):
                    set_user_group(event.user_id,event.text)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Ваш выбор: '+get_user_group(event.user_id),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
            elif event.text.lower() in ('пн', 'вт','ср','чт','пт','сб'):
                if (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) != 0):
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выбранный день недели: '+event.text+'\nВыбранная группа: '+get_user_group(event.user_id),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
                    if (event.text == 'ПН' or event.text == 'пн'):
                        vk.messages.send(
                        user_id=event.user_id,
                        message=get_mon(get_user_group(event.user_id)),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
                    elif (event.text == 'ВТ' or event.text == 'вт'):
                        vk.messages.send(
                        user_id=event.user_id,
                        message=get_tue(get_user_group(event.user_id)),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
                    elif (event.text == 'СР' or event.text == 'ср'):
                        vk.messages.send(
                        user_id=event.user_id,
                        message=get_mon(get_user_group(event.user_id)),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
                    elif (event.text == 'ЧТ' or event.text == 'чт'):
                        vk.messages.send(
                        user_id=event.user_id,
                        message=get_thu(get_user_group(event.user_id)),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
                    elif (event.text == 'ПТ' or event.text == 'пт'):
                        vk.messages.send(
                        user_id=event.user_id,
                        message=get_fri(get_user_group(event.user_id)),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
                    elif (event.text == 'СБ' or event.text == 'сб'):
                        vk.messages.send(
                        user_id=event.user_id,
                        message=get_sab(get_user_group(event.user_id)),
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
            elif event.text in ('📋 Расписание '+get_user_group(event.user_id), 'Расписание '+get_user_group(event.user_id)):
                if (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) != 0):
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Меню студента группы '+mygroup+': ',
                        keyboard=enable_keyboard_my(),
                        random_id=random_id()
                    )
                elif (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) == 0):
                    vk.messages.send(
                        user_id=event.user_id,
                        message=dictReg,
                        keyboard=enable_keyboard_my(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            elif event.text in ('📋 Посмотреть'):
                if (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) != 0):
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберите день '+mygroup+': ',
                        keyboard=enable_keyboard_week(event.user_id),
                        random_id=random_id()
                    )
                elif (get_user_wish(event.user_id) == 1) and (get_user_group(event.user_id) == 0):
                    vk.messages.send(
                        user_id=event.user_id,
                        message=dictReg,
                        keyboard=enable_keyboard_my(),
                        random_id=random_id()
                    )
                else:
                    elsereg()
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message="Неизвестная команда.\nПопробуйте снова...",
                    keyboard=enable_keyboard_start(),
                    random_id=random_id()
                )