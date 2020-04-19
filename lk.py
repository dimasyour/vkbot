from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from dbworker import *

def enable_keyboard_my(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('📋 Расписание '+get_user_group(183173666), VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('👥 Моя группа', VkKeyboardColor.POSITIVE)
    keyboard.add_button('📋 Посмотреть', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('⏳ Какая сейчас пара?', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📅 Неделя', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Вернуться назад к главной', VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()

def enable_keyboard_week(user_id):
    keyboard = VkKeyboard(False)
    keyboard.add_button(get_user_group(user_id), VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ПН', VkKeyboardColor.POSITIVE)
    keyboard.add_button('ВТ', VkKeyboardColor.POSITIVE)
    keyboard.add_button('СР', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('ЧТ', VkKeyboardColor.POSITIVE)
    keyboard.add_button('ПТ', VkKeyboardColor.POSITIVE)
    keyboard.add_button('СБ', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Вернуться назад к главной', VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()