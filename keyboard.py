from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def enable_keyboard_start(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('✅ Моё расписание', VkKeyboardColor.POSITIVE)
    keyboard.add_button('🔔 Расписание', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('⏲️ Звонок', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📣 Объявления', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('👨‍🏫 Преподаватели', VkKeyboardColor.PRIMARY)
    keyboard.add_button('👩‍💻 Студенты', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🗓 Неделя', VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()

def enable_keyboard_start_admin(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('✅ Моё расписание', VkKeyboardColor.POSITIVE)
    keyboard.add_button('🔔 Расписание', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('⏲️ Звонок', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📣 Объявления', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('👨‍🏫 Преподаватели', VkKeyboardColor.PRIMARY)
    keyboard.add_button('👩‍💻 Студенты', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🗓 Неделя', VkKeyboardColor.PRIMARY)
    keyboard.add_button('Админ-панель', VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()

def enable_keyboard(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('/help', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('/m', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/n', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/f жанры', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('/w', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/exr', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/c', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/fmfi', VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()
#--------------ВЫБОР ФАКУЛЬТЕТА 1------------------------#
def enable_keyboard_rasp_1(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Вернуться назад к главной', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🧮 ФМФИ', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🗺 ЕГФ', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('📚 ФФ', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🏛 ИФ', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📊 ФЭУС', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Показать следующие факультеты', VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()

#--------------ВЫБОР ФАКУЛЬТЕТА 2------------------------#
def enable_keyboard_rasp_2(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Вернуться назад к главной', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🥇 ФФКиС', VkKeyboardColor.PRIMARY)
    keyboard.add_button('💑 ФПСО', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('👪 ФНО', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🎭 ФКИ', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🇬🇧 ФИЯ', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Показать предыдущие факультеты', VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФМФМ------------------------#
def enable_keyboard_rasp_fmfi(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('🧮 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🧮 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🧮 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🧮 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФМФМ 2019------------------------#\w\w\w\w-\w\d\d\-\w\w\w\
def enable_keyboard_rasp_fmfi_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФМФИ-б19ИДо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФМФИ-б19МИо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФМФИ-б19МФо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФМФИ-б19ПИо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🧮 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФМФМ 2018------------------------#
def enable_keyboard_rasp_fmfi_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФМФИ-б18Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФМФИ-б18МФо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФМФИ-б18ПИо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🧮 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФМФМ 2017------------------------#
def enable_keyboard_rasp_fmfi_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФМФИ-б17Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФМФИ-б17МФо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФМФИ-б17ПИо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🧮 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФМФМ 2016------------------------#
def enable_keyboard_rasp_fmfi_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФМФИ-б16ИИо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФМФИ-б16Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФМФИ-б16МИо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФМФИ-б16ФИо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФМФИ-б16ФТо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🧮 Назад', VkKeyboardColor.NEGATIVE)


    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ЕГФ------------------------#
def enable_keyboard_rasp_egf(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('🗺 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🗺 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🗺 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🗺 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ЕГФ 2019------------------------#
def enable_keyboard_rasp_egf_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ЕГФ-б19БГо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б19БХо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ЕГФ-б19ЕСо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б19ЭПо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🗺 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ЕГФ 2018------------------------#
def enable_keyboard_rasp_egf_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ЕГФ-б18БГо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б18БХо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ЕГФ-б18ЕСо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б18ЭПо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🗺 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ЕГФ 2017------------------------#
def enable_keyboard_rasp_egf_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ЕГФ-б17БГо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б17БГо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б17БХо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ЕГФ-б17ЕСо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б17ЭПо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🗺 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ЕГФ 2016------------------------#
def enable_keyboard_rasp_egf_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ЕГФ-б16БГо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ЕГФ-б16БХо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🗺 Назад', VkKeyboardColor.NEGATIVE)


    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФФ------------------------#
def enable_keyboard_rasp_ff(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('📚 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📚 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('📚 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📚 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФ 2019------------------------#
def enable_keyboard_rasp_ff_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФ-б19Жо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФ-б19РЛо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФ-б19РЛо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📚 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФ 2018------------------------#
def enable_keyboard_rasp_ff_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФ-б18Жо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФ-б18РЛо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФ-б18РЛо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📚 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФ 2017------------------------#
def enable_keyboard_rasp_ff_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФ-б17Жо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФ-б17РЛо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФ-б17РЛо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📚 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФ 2016------------------------#
def enable_keyboard_rasp_ff_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФ-б16Жо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФ-б16РЛо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФ-б16РЛо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФ-б16РСо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФ-б16СОо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📚 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ИФ------------------------#
def enable_keyboard_rasp_if(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('🏛 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🏛 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🏛 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🏛 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ИФ 2019------------------------#
def enable_keyboard_rasp_if_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ИФ-б19ИОо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ИФ-б19ИОо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ИФ-б19ИПо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🏛 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ИФ 2018------------------------#
def enable_keyboard_rasp_if_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ИФ-б18ИОо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ИФ-б18ИОо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ИФ-б18ИПо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🏛 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ИФ 2017------------------------#
def enable_keyboard_rasp_if_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ИФ-б17ИОо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ИФ-б17ИОо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ИФ-б17ИПо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🏛 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ИФ 2016------------------------#
def enable_keyboard_rasp_if_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ИФ-б16ИОо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ИФ-б16ИОо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ИФ-б16По', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🏛 Назад', VkKeyboardColor.NEGATIVE)


    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФЭУС------------------------#
def enable_keyboard_rasp_feus(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('📊 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📊 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('📊 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('📊 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФЭУС 2019------------------------#
def enable_keyboard_rasp_feus_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФЭУС-б19ЭЯо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б19ЭЯо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📊 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФЭУС 2018------------------------#
def enable_keyboard_rasp_feus_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФЭУС-б18МОо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б18Фо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФЭУС-б18ЭЯо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б18ЭЯо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📊 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФЭУС 2017------------------------#
def enable_keyboard_rasp_feus_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФЭУС-б17МОо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б17Фо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФЭУС-б17ЭЯо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б17ЭЯо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📊 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФЭУС 2016------------------------#
def enable_keyboard_rasp_feus_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФЭУС-б16Бо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б16МОо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФЭУС-б16Со', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б16Фо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФЭУС-б16Эо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФЭУС-б16ЭЯо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('📊 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФФКиС------------------------#
def enable_keyboard_rasp_ffkis(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('🥇 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🥇 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🥇 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🥇 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФКиС 2019------------------------#
def enable_keyboard_rasp_ffkis_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФКС-б19По1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФКС-б19По2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФКС-б19Фо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('🥇 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФКиС 2018------------------------#
def enable_keyboard_rasp_ffkis_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФКС-б18По1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФКС-б18По2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФКС-б18По3', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🥇 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФКиС 2017------------------------#
def enable_keyboard_rasp_ffkis_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФКС-б17По1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФКС-б17По2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФКС-б17По3', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФКС-б17По4', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🥇 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФФКиС 2016------------------------#
def enable_keyboard_rasp_ffkis_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФФКС-б16По1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФФКС-б16По2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФФКС-б16По3', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🥇 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФПСО------------------------#
def enable_keyboard_rasp_fpso(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('💑 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('💑 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('💑 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('💑 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФПСО 2019------------------------#
def enable_keyboard_rasp_fpso_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФПСО-б19ДДо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б19Ло', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФПСО-б19Ло1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б19Ло2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б19ПОо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('💑 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФПСО 2018------------------------#
def enable_keyboard_rasp_fpso_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФПСО-б18ДДо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б18Ло', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФПСО-б18Ло1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б18ПОо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('💑 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФПСО 2017------------------------#
def enable_keyboard_rasp_fpso_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФПСО-б17ДДо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФПСО-б17Ло', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б17ПОо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('💑 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФПСО 2016------------------------#
def enable_keyboard_rasp_fpso_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФПСО-б16Ло', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б16Оо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФПСО-б16По', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФПСО-б16ПОо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФПСО-б16ПОо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('💑 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФНО------------------------#
def enable_keyboard_rasp_fno(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('👪 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('👪 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('👪 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('👪 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФНО 2019------------------------#
def enable_keyboard_rasp_fno_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФНО-б19ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б19ДНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФНО-б19НВо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б19НИо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФНО-б19НЯо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('👪 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФНО 2018------------------------#
def enable_keyboard_rasp_fno_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФНО-б18ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б18ДНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФНО-б18НИо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б18НЯо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('👪 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФНО 2017------------------------#
def enable_keyboard_rasp_fno_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФНО-б17ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б17ДНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФНО-б17НИо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б17НЯо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('👪 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФНО 2016------------------------#
def enable_keyboard_rasp_fno_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФНО-б16ДНо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б16ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФНО-б16НВо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б16НИо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФНО-б16НЯо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФНО-б16Со', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('👪 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФКИ------------------------#
def enable_keyboard_rasp_fki(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('🎭 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🎭 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🎭 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🎭 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФКИ 2019------------------------#
def enable_keyboard_rasp_fki_2019(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФКИ-б19Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФКИ-б19Мо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🎭 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФКИ 2018------------------------#
def enable_keyboard_rasp_fki_2018(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФКИ-б18Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФКИ-б18Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФКИ-б18Мо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🎭 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФКИ 2017------------------------#
def enable_keyboard_rasp_fki_2017(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФКИ-б17Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФКИ-б17Ко', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФКИ-б17Мо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФКИ-б17Хо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🎭 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФКИ 2016------------------------#
def enable_keyboard_rasp_fki_2016(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('ФКИ-б16Ио', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФКИ-б16Ко', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФКИ-с16Жо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФКИ-б16Мо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФКИ-б16Хо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🎭 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ГОД ПОСТУПЛЕНИЯ ФИЯ------------------------#
def enable_keyboard_rasp_fib(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('🇬🇧 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🇬🇧 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_button('🇬🇧 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('🔔 Назад к факультету', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()
#--------------ФИЯ 2019 1ч------------------------#
def enable_keyboard_rasp_fib_2019_1(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать следующие группы ФИЯ 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б19АНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19АНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б19АНо3', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19АФо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б19АФо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19ДНз1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19ДНз2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФИЯ 2019 2 ч------------------------#
def enable_keyboard_rasp_fib_2019_2(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать предыдущие группы ФИЯ 2019', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б19ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19ДНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б19ЗРо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19ППо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б19ППо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19ППо3', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б19ФАо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФИЯ 2018 1ч------------------------#
def enable_keyboard_rasp_fib_2018_1(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать следующие группы ФИЯ 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б18АНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б18АНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б18АНо3', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б18АФо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б18АФо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б18АФо3', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б18ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФИЯ 2018 2 ч------------------------#
def enable_keyboard_rasp_fib_2018_2(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать предыдущие группы ФИЯ 2018', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б18ДНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б18ЗРо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б18ППо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б18ППо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б18ППо3', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б18ТМо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФИЯ 2017 1ч------------------------#
def enable_keyboard_rasp_fib_2017_1(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать следующие группы ФИЯ 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б17АНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б17АНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б17АФо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б17АФо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б17АФо3', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б17ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФИЯ 2017 2 ч------------------------#
def enable_keyboard_rasp_fib_2017_2(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать предыдущие группы ФИЯ 2017', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б17ДНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б17ЗРо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б17ППо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б17ППо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б17ТМо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФИЯ 2016 1ч------------------------#
def enable_keyboard_rasp_fib_2016_1(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать следующие группы ФИЯ 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б16ЗРо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б16НАо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б16ППо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б16ППо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б16ТМо', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б16ФАо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

#--------------ФИЯ 2017 2 ч------------------------#
def enable_keyboard_rasp_fib_2016_2(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Показать предыдущие группы ФИЯ 2016', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б16АНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б16АНо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б16АФо1', VkKeyboardColor.DEFAULT)
    keyboard.add_button('ФИЯ-б16АФо2', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('ФИЯ-б16ДНо1', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('🇬🇧 Назад', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()
#--------------Админ------------------------#
def enable_keyboard_admin(geo_button=False):
    keyboard = VkKeyboard(False)
    keyboard.add_button('Объявление', VkKeyboardColor.DEFAULT)
    keyboard.add_button('Инфо', VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('Вернуться назад к главной', VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

