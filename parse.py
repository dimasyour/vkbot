# import datetime
# from openpyxl import load_workbook
import re

# wb = load_workbook('rasp.xlsx')
# sheet_ranges = wb['sheet2']
# column_a = sheet_ranges['A']
# column_b = sheet_ranges['B']
# column_d = sheet_ranges['D']
# column_c = sheet_ranges['C']
# column_f = sheet_ranges['F']
    #weeksTodayStr = datetime.datetime.now()
    #weekTodayStr = weeksTodayStr.strftime("%U")
    #weekTodayInt = int(weekTodayStr)
    #weekTodayInt = weekTodayInt+0
# i = 4
# x = '0'
# for i in range(len(column_c)):
#     if  column_b[i].value == '11:40-13:10' and column_a[5].value == 'понедельник':
#         predmet = column_c[i].value
#         print(predmet)
#     elif column_b[i].value == '13:30-15:00' and column_a[5].value == 'понедельник':
#     	predmet2 = column_c[i].value
#     	print(predmet2)
#     elif column_c[i].value == 'Согласовано:':
#         print('stop')
# i=5
# for i in range(len(column_c)):
#     print(i)
#     print(column_a[i].value)
# welcome = "Hello world! Goodbye world!"
# index = welcome.find("wor")
# print(index)       # 6
# i=1
# while i < 29:
#     if ((column_a[i].value) != None):
#         print(column_b[i].value)
#         i = i+1
#     elif ((column_a[i].value) == None):
#         i = i + 1

# for i in range(4,21):
#     if (column_b[i].value == None):
#         i+=1
#     else:
#         print(column_b[i].value+' | '+column_c[i].value)

# for i in range(4,21):
#     if (column_b[i].value == None):
#          i+=1
#     elif (column_b[i].value != None) and (column_b[i+1].value == None):
#          print(column_b[i].value+' | '+column_c[i].value+' / '+column_c[i+1].value)

# for i in range(4,21):
#     if (column_c[i].value == None):
#         i+=1
#     elif (column_c[i].value != None) and (column_d[i].value == None) and (column_c[i+1].value == None):
#         print('пара у 2')
# print('/////////')
# for i in range(4,21):
#     if (column_c[i].value == None):
#         i+=1
#     elif (column_c[i].value != None) and (column_d[i].value == None) and (column_d[i+1].value == None):
#         print('пара у 1')
# 23-25,27, 29,30,32-36 н.-п.
# result = re.split(r',', '23-25,27, 29,30,32-36 н.-п.')
# print(result)
# f = result
# f = [x.replace('н.-п.','').replace('н.-л.','').replace(' ','') for x in f]
# print(f)
# print(f[0].split('-',2))

# list2 = [0,0,0,0]

# print('----------')
# for i in range(len(f)):
#     if(f.)
# i=0
# for i in range(5):
#    f[i].replace('-',' ')
# s = "23-25,27, 29,30,32-36 н.-п."

# for i in range(len(f)):
#     for j in range(len(f[i])):
#         if (f[i][j] != '') and (f[i][j] != ''):
#             print(f[i])
#         else:
#             print('hello')
#     print()

# for i in range(0, len(f)):
#     if (len(f[i]) > 2):
#         for j in range(4):
#             list2[j] = f[j].split('-',1)

# print(list2)
# gf = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# for i in range(len(list2)):
#     for j in range(len(list2[i])):
#         if (len(list2[i]) > 1):
#             print(list2[i][j])
#             io = 23
#             for io in range(25):
#                 gr[2] = list2[i][j]

spisok = ['23-25', '27-41', '29', '30', '32-36']
newspisok = []
for i in spisok:
    if not i.isdigit():
        a = i.split('-', 1)
        for number in range(int(a[0]),int(a[1])+1):
            newspisok.append (number)
    else:
        newspisok.append (int(i))


print (newspisok)