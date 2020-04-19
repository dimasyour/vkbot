import sys
# appending the path of another folder
sys.path.insert(0,'../')
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from keyboard import *
import Constants
import random
from func import checkWeek, weekFull
# TODO: попробовать узнать погоду с помощью кнопки геолокации
# TODO: попробовать сделать голосовуху робота с указанным сообщением с помощью gtts
# TODO: добавить возможность пересылать сообщения
#Файл констант
c = Constants
conn = sqlite3.connect("db.db")
c = conn.cursor()
#Главная функция
def main():
    token = '94376fff72067ddeb1eae787cceff0a590d5fe5bb8d4c11e047b4e9bc89b1a274c6f83f467194058ef684'
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    print('Server started')

    summary = '''
    Вот что я умею:

🔔 /расписание - Просмотреть расписание 
⏲️ /звонок - Сколько до конца пары? 
📣 /объявления - Показать объявления 
👨‍🏫 /преподаватели - Найти преподавателя 
👩‍💻 /студенты - Найти студента 
🗓 /неделя - Что за неделя? 

    '''

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            random_id = get_random_id()
            user_id = event.user_id
            msg = event.text.lower()

            kwargs = {'user_id': user_id,
                      'random_id': random_id}

            if msg in ('/help', 'начать', 'вернуться назад к главной'):
                vk.messages.send(message=summary, keyboard=enable_keyboard_start(),
                                 **kwargs)
            elif msg in ('/rasp','/rasp_1', '🔔 расписание','/расписание', '🔔 назад к факультету','показать предыдущие факультеты'):
                vk.messages.send(message='Выберите желаемый факультет:', keyboard=enable_keyboard_rasp_1(),
                                 **kwargs)
            elif msg in ('/rasp_2','/расписание 2', 'показать следующие факультеты'):
                vk.messages.send(message='Выберите желаемый факультет:', keyboard=enable_keyboard_rasp_2(),
                                 **kwargs)
#----------------------------------------------ФМФИ---------------------------------------------------------------------
            elif msg in ('/fmfi', '🧮 фмфи','/фмфи', 'фмфи', '🧮 назад'):
                    vk.messages.send(message='Выберите год поступления на Факультет математики, физики и информатики:', keyboard=enable_keyboard_rasp_fmfi(),
                                     **kwargs)
            elif msg in ('/fmfi_2019', '🧮 2019','/фмфи_2019', 'фмфи 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fmfi_2019(),
                                        **kwargs)
            elif msg in ('/fmfi_2018', '🧮 2018','/фмфи_2018', 'фмфи 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fmfi_2018(),
                                        **kwargs)
            elif msg in ('/fmfi_2017', '🧮 2017','/фмфи_2017', 'фмфи 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fmfi_2017(),
                                        **kwargs)
            elif msg in ('/fmfi_2016', '🧮 2016','/фмфи_2016', 'фмфи 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fmfi_2016(),
                                        **kwargs)
#----------------------------------------------ЕГФ---------------------------------------------------------------------
            elif msg in ('/egf', '🗺 егф','/егф', 'егф', '🗺 егф', '🗺 назад'):
                    vk.messages.send(message='Выберите год поступления на Естественно-географический факультет:', keyboard=enable_keyboard_rasp_egf(),
                                     **kwargs)
            elif msg in ('/egf_2019', '🗺 2019','/егф_2019', 'егф 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_egf_2019(),
                                        **kwargs)
            elif msg in ('/egf_2018', '🗺 2018','/егф_2018', 'егф 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_egf_2018(),
                                        **kwargs)
            elif msg in ('/egf_2017', '🗺 2017','/егф_2017', 'егф 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_egf_2017(),
                                        **kwargs)
            elif msg in ('/egf_2016', '🗺 2016','/егф_2016', 'егф 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_egf_2016(),
                                        **kwargs)
#----------------------------------------------ФФ-----------------------------------------------------------------------📚
            elif msg in ('/ff','филфак','📚 фф','/фф', 'фф', '📚 фф', '📚 назад'):
                    vk.messages.send(message='Выберите год поступления на Филологический факультет:', keyboard=enable_keyboard_rasp_ff(),
                                     **kwargs)
            elif msg in ('/ff_2019', '📚 2019','/фф_2019', 'фф 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2019(),
                                        **kwargs)
            elif msg in ('/ff_2018', '📚 2018','/фф_2018', 'фф 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2018(),
                                        **kwargs)
            elif msg in ('/ff_2017', '📚 2017','/фф_2017', 'фф 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2017(),
                                        **kwargs)
            elif msg in ('/ff_2016', '📚 2016','/фф_2016', 'фф 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2016(),
                                        **kwargs)
#----------------------------------------------ИФ---------------------------------------------------------------------🏛
            elif msg in ('/if','истфак','🏛 иф','/иф', 'иф', '🏛 иф', '🏛 назад'):
                    vk.messages.send(message='Выберите год поступления на Исторический факультет:', keyboard=enable_keyboard_rasp_ff(),
                                     **kwargs)
            elif msg in ('/if_2019', '🏛 2019','/иф_2019', 'иф 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2019(),
                                        **kwargs)
            elif msg in ('/if_2018', '🏛 2018','/иф_2018', 'иф 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2018(),
                                        **kwargs)
            elif msg in ('/if_2017', '🏛 2017','/иф_2017', 'иф 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2017(),
                                        **kwargs)
            elif msg in ('/if_2016', '🏛 2016','/иф_2016', 'иф 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ff_2016(),
                                        **kwargs)
#----------------------------------------------ФЭУС---------------------------------------------------------------------📊
            elif msg in ('/feus','фэус','📊 фэус','/фэус', 'фэус', '📊 фэус', '📊 назад'):
                    vk.messages.send(message='Выберите год поступления на Факультет экономики, упраления и сервиса:', keyboard=enable_keyboard_rasp_feus(),
                                     **kwargs)
            elif msg in ('/feus_2019', '📊 2019','/фэус_2019', 'фэус 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_feus_2019(),
                                        **kwargs)
            elif msg in ('/feus_2018', '📊 2018','/фэус_2018', 'фэус 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_feus_2018(),
                                        **kwargs)
            elif msg in ('/feus_2017', '📊 2017','/фэус_2017', 'фэус 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_feus_2017(),
                                        **kwargs)
            elif msg in ('/feus_2016', '📊 2016','/фэус_2016', 'фэус 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_feus_2016(),
                                        **kwargs)
#----------------------------------------------ФФКиС---------------------------------------------------------------------🥇
            elif msg in ('/ffkis','ффкис','🥇 ии','/ффкис', 'ффкис', '🥇 ффкис', '🥇 назад'):
                    vk.messages.send(message='Выберите год поступления на Факультет физической культуры и спорта:', keyboard=enable_keyboard_rasp_ffkis(),
                                     **kwargs)
            elif msg in ('/ffkis_2019', '🥇 2019','/ффкис_2019', 'ффкис 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ffkis_2019(),
                                        **kwargs)
            elif msg in ('/ffkis_2018', '🥇 2018','/ффкис_2018', 'ффкис 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ffkis_2018(),
                                        **kwargs)
            elif msg in ('/ffkis_2017', '🥇 2017','/ффкис_2017', 'ффкис 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ffkis_2017(),
                                        **kwargs)
            elif msg in ('/ffkis_2016', '🥇 2016','/ффкис_2016', 'ффкис 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_ffkis_2016(),
                                        **kwargs)
#----------------------------------------------ФПСО---------------------------------------------------------------------💑
            elif msg in ('/fpso','фпсо','💑 фпсо','/фпсо', 'фпсо', '💑 фпсо', '💑 назад'):
                    vk.messages.send(message='Выберите год поступления на Факультет психологии и специального образования:', keyboard=enable_keyboard_rasp_fpso(),
                                     **kwargs)
            elif msg in ('/fpso_2019', '💑 2019','/фпсо_2019', 'фпсо 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fpso_2019(),
                                        **kwargs)
            elif msg in ('/fpso_2018', '💑 2018','/фпсо_2018', 'фпсо 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fpso_2018(),
                                        **kwargs)
            elif msg in ('/fpso_2017', '💑 2017','/фпсо_2017', 'фпсо 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fpso_2017(),
                                        **kwargs)
            elif msg in ('/fpso_2016', '💑 2016','/фпсо_2016', 'фпсо 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fpso_2016(),
                                        **kwargs)
#----------------------------------------------ФНО---------------------------------------------------------------------👪
            elif msg in ('/fno','фно','👪 фно','/фно', 'фно', '👪 фно', '👪 назад'):
                    vk.messages.send(message='Выберите год поступления на Факультет начального образования:', keyboard=enable_keyboard_rasp_fno(),
                                     **kwargs)
            elif msg in ('/fno_2019', '👪 2019','/фно_2019', 'фно 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fno_2019(),
                                        **kwargs)
            elif msg in ('/fno_2018', '👪 2018','/фно_2018', 'фно 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fno_2018(),
                                        **kwargs)
            elif msg in ('/fno_2017', '👪 2017','/фно_2017', 'фно 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fno_2017(),
                                        **kwargs)
            elif msg in ('/fno_2016', '👪 2016','/фно_2016', 'фно 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fno_2016(),
                                        **kwargs)
#----------------------------------------------ФКИ---------------------------------------------------------------------🎭
            elif msg in ('/fki','фки','🎭 фки','/фки', 'фки', '🎭 фки', '🎭 назад'):
                    vk.messages.send(message='Выберите год поступления на Факультет культуры и искусства:', keyboard=enable_keyboard_rasp_fki(),
                                     **kwargs)
            elif msg in ('/fki_2019', '🎭 2019','/фки_2019', 'фки 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fki_2019(),
                                        **kwargs)
            elif msg in ('/fki_2018', '🎭 2018','/фки_2018', 'фки 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fki_2018(),
                                        **kwargs)
            elif msg in ('/fki_2017', '🎭 2017','/фки_2017', 'фки 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fki_2017(),
                                        **kwargs)
            elif msg in ('/fki_2016', '🎭 2016','/фки_2016', 'фки 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fki_2016(),
                                        **kwargs)
#----------------------------------------------ФИЯ---------------------------------------------------------------------🇬🇧
            elif msg in ('/fib','иняз','🇬🇧 фия','/фия', 'фия', '🇬🇧 фия', '🇬🇧 назад'):
                    vk.messages.send(message='Выберите год поступления на Факультет иностранных языков:', keyboard=enable_keyboard_rasp_fib(),
                                     **kwargs)
            elif msg in ('/fib_2019','/fib_2019_1', '🇬🇧 2019','/фия_2019', 'фия 2019','показать предыдущие группы фия 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2019_1(),
                                        **kwargs)
            elif msg in ('/fib_2019_2', '🇬🇧 2019_2','/фия_2019_2', 'фия 2019_2','показать следующие группы фия 2019'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2019_2(),
                                        **kwargs)
            elif msg in ('/fib_2018','/fib_2018_1', '🇬🇧 2018','/фия_2018', 'фия 2018','показать предыдущие группы фия 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2018_1(),
                                        **kwargs)
            elif msg in ('/fib_2018_2', '🇬🇧 2018_2','/фия_2018_2', 'фия 2018_2','показать следующие группы фия 2018'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2018_2(),
                                        **kwargs)
            elif msg in ('/fib_2017','/fib_2017_1', '🇬🇧 2017','/фия_2017', 'фия 2017','показать предыдущие группы фия 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2017_1(),
                                        **kwargs)
            elif msg in ('/fib_2017_2', '🇬🇧 2017_2','/фия_2017_2', 'фия 2017_2','показать следующие группы фия 2017'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2017_2(),
                                        **kwargs)
            elif msg in ('/fib_2016','/fib_2016_1', '🇬🇧 2016','/фия_2016', 'фия 2016','показать предыдущие группы фия 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2016_1(),
                                        **kwargs)
            elif msg in ('/fib_2016_2', '🇬🇧 2016_2','/фия_2016_2', 'фия 2016_2','показать следующие группы фия 2016'):
                        vk.messages.send(message=c.chooseGroup[random.randint(0,len(c.chooseGroup)-1)], keyboard=enable_keyboard_rasp_fib_2016_2(),
                                        **kwargs)
#-----------------------------------------------------------------------------------------------------------------------
            elif msg in ('/zvonok', '⏲️ звонок','/звонок'):
                vk.messages.send(message='summary', keyboard=enable_keyboard(),
                                 **kwargs)
            elif msg in ('/ob', '📣 объявления','/объявления','объявление','/объявление'):
                vk.messages.send(message='summary', keyboard=enable_keyboard(),
                                 **kwargs)
            elif msg in ('/find_teacher', '👨‍🏫 преподаватели','/преподаватели','преподаватели','/преподаватель'):
                vk.messages.send(message='summary', keyboard=enable_keyboard(),
                                 **kwargs)
            elif msg in ('/find_student', '👩‍💻 студенты','/студенты','студенты','/студент'):
                vk.messages.send(message='summary', keyboard=enable_keyboard(),
                                 **kwargs)
            elif msg in ('/my', '✅ моё расписание','мое расписание','моё расписание','✅ мое расписание','/myrasp'):
                vk.messages.send(message='Твоя группа: ', keyboard=enable_keyboard_my(),
                                 **kwargs)
            else:
                vk.messages.send(message='''Я не понимаю то, что Вы написали\n.
                                 Отправьте /help, чтобы увидеть сводку по командам''',
                                 **kwargs)


main()
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            if not check_if_exists(event.user_id):
                register_new_user(event.user_id)

            if event.text.lower() == "привет":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Привет!",
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )

            elif event.text.lower() == "регистрация":
                if get_user_wish(event.user_id) == 0:
                    set_user_wish(event.user_id, 1)
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Вы успешно зарегистрированы на рассылку!",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                else:
                    set_user_wish(event.user_id, 0)
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Вы успешно удалены из базы!",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )

            elif event.text.lower() == "ссылка":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="https://www.youtube.com/channel/UCCCcDxRXwTE-rtpcyMzxjAA?view_as=subscriber",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                else:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Вы не зарегистрированы, напишите команду 'Регистрация'",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message="Неизвестная команда",
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )