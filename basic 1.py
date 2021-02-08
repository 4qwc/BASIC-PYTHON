# Basic Python programming
# by hs4qwc 7/2/2021

a = 10
b = 50
c = -20
d = 2.50

p = 'Basic Programming' # string

i = {2020,5555,9999} # ตัวแปร แบบ set

a = [222, 333, 444, 555] # list
b = ['ddd', 'eee', 'ttt', 'uuu', 12345,]

#การกำหนดพิ่มค่าภายใน a
#a [3] = 999 # เพิ่มข้อมูลตำแหน่งที่ 3

# การเพิ่มค่า ใน list
a.append(777)
#print('     A = ', a[0:]) # แสดงค่าภายใน a ทั้งหมด

# การลบค่าใน list
b.remove('ttt')  #
#print('B = ', b[0:])

# COPY
c = a.copy() # การก๊อบข้อมูล a
#print('COPY A = ', c)

d = list(b) # การกำหนดให้ d เท่ากับ ข้อมูลภายใน b
#print('D = ', d)

#print('Mumber: ', a, b, c, d)



###########################
#***  การใช้ตัวแปร global function
#a = 'Global variable'
def my_function():
    print('a อยู่ในฟังก์ชั่น  :', a) # เรียกใช้ a ในฟังก์ชั่น

#my_function()
#print("a เรียกใช้ฟังก์ชั่น ", a)

#***************************

#***  การใช้ตัวแปร global function
a = 'Global variable'
def my_function():
    a = 'Local variabel' # จะทำงานในฟังก์ชั่นเท่านั้น
    print('a อยู่ในฟังก์ชั่น  :', a) # เรียกใช้ a ในฟังก์ชั่น

#my_function()
#print("a เรียกใช้ฟังก์ชั่น ", a)

#***********************************
'''
a = 'a global'
def my_function_a():
    a = 'Local'
    def my_function_b():
        nonlocal a
        a = 'NONLOCAL'
        print('a in my_function_b: ', a)

    my_function_b()
    print('A in my_function_a: ', a)

my_function_a()
print('a in main', a)
'''
#********************
# การกำหนดตัวแปรในบรรทัดเดียวกัน
'''
x, y, z = ' :AAA', 'BBB', 555

print('X= ',x)
print('Y= ', y)
print('Z= ', z)

s = str(z )+ x  #ค่า z แปลง int เป็น str
print('S= ' + ':' + s)
'''
#--------------------

# opreators
# ==, !=, <, >, <=, >=
'''
a = 10
b = 20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
'''


#*************
# การใช้งาน Logical operators
# and, or, not

a = 5
b = 10
c = 5
#print('result: ',(a<b and b>c))# เท็จ and = เท็จเสมอ

#print('result: ',(a>b or b>c)) # True or = True

#print('result: ',(not b<c))# ค่าไม่เป็นจริง = False # ค่าเป็นจริง = True

#******************

# ตัวดำเนินการ identity
#คือ สิ่งที่เหมือนกัน กับ ไม่เหมือนกัน
#    is,      is not
# x is y,   x not is y

# การใช้งาน
'''
x = 'ABCD-EFGH-IJKL-MNOP'
i = x
j = 'IJKL-MNOP-EFGH-ABCD'
k = 'P-1234-567/890'
z = 'P-1234-567/890'

print(x is j) # x เหมือน j/ False
print('X is i: ',x is i) # x เหมือน j/ True
print('k is z: ',k is z) # k เหมือน z/ True
print('k is z: ',k is not z) # k ไม่เหมือน z/ False
'''
#*******************

# การใช้ตัวดำเนินการ Membership operators
# คือ เป็นสมาชิกหรือไม่เป็นสมาชิก
#   in ,    not in
'''
LIST = ['COCONAT', 'ORANGE', 'APPLE']
buy1 = 'ORANGE' #
buy2 = 'MANGO'

print ('BUY1:',buy1 in LIST ) # เช็คว่ามีชื่อผลไม้ที่ซื้อหรือไม่ True
print ('ฺBUY2:', buy2 in LIST ) # เช็คว่ามีชื่อผลไม้ที่ซื้อหรือไม่ False

print ('ฺสิ่งที่ไม่มีในรายการ BUY1:', buy1 not in LIST ) # เช็คว่ามีชื่อผลไม้ที่ซื้อหรือไม่ False
print ('ฺสิ่งที่ไม่มีในรายการ BUY2:', buy2 not in LIST ) # เช็คว่ามีชื่อผลไม้ที่ซื้อหรือไม่ False

#result
#สิ่งที่ไม่มีในรายการ BUY1: False
#สิ่งที่ไม่มีในรายการ BUY2: True
'''
#------------------------


#*****************
# การใช้งาน Bitwise
# ตัวดำเนินการด้านบิตข้อมูล
# &, |, ^, ~,  <<, >>

'''
PA = 0b11100111 #E7 DEX 231 BIN:0b1110 0111
PB = 136 #DEX 170 HEX 0xAA  BIN:0b1000 1000
PC = 1
PD = 0
PE = 0xAAFF #BIN: 1111 1111 HEX:0xFF

print('PA:     ', bin(PA))    #0b11100111
print('PB:     ', bin(PB))    #0b10001000

print('PA & PB:', bin(PA&PB))# 0b10000000 HEX0x80
print("PA | PB:", bin(PA|PB))# 0b11101111
print("PA ^ PB:", bin(PA^PB)) #0b1101111
PB = 255 #11111111
print('PC: ',bin(~PC))#0b10
print('PD: ',bin(~PD))# 0b1

print(bin(PB))
print(bin(PB<<1))#0b111111110
print(bin(PB>>1))#0b1111111

print(bin(PE))
'''

#-----------------------

# *** IF ***-
#i = 100
#e = 400
TEXT = 'HELLO TEST'

# คำสั่งแบบ 2 ทางเลือก
'''
if i>e:
    print(TEXT)
    print('ทำงานใน IF')
else:
    print("ทำงานใน ELSE")

'''
#----------------------
# คำสั่งแบบ หลายทางเลือก
'''
i = 10
e = 10
if i>=e:
    i+=10
    print('ทำงาน i>e, True ',i)
    if i==20:
       print('I = ', i)
       i=0
    print('ค่าสุดท้าย I:',i)

elif i<=e:
    print('ทำงาน i<=e, False')

else:
    print('ไม่เข้าเงื่อนไขข้างต้น!\nจบการทำงาน')
'''

#***********************

# กาวทำงาน for, while   loop
#for กำหนดรอบที่แน่นอน
# while รอบไม่แน่นอน
a =101
b = 10
'''
for i in range(0, a, b):#0=ค่าจะเริ่มต้นทำงาน,
                           #a=ค่าสิ้นสุด,
                           # b=ค่าช่วงการทำงาน
    print(i)
'''
#---------------
'''
for i in range(0, 10):
    print(':', i,  end='') # end คือ ไม่ขึ้นบรรทัดใหม่
'''
#-----------------
'''
for i in range(10, 0, -1):
    print(':', i, end='')
'''

#******  WHILE *****

# การทำงาน while จะตรวจสอบเงื่อนไขใน while loop ถ้าเป็นจริง จะทำงานไปเรื่อยๆ จนกว่าเป็นเท็จ
'''
i = 0

while i<100:
    print(i, end=',')
    i+=1

print('>>')
'''
#------------------


# คำสั่งช่วยควบคุมในเงื่อนไข
'''
    break = หยุดการทำในลูป
    continue = ทำงานข้ามไปอีกรอบ ตามที่กำหนดให้ข้ามตำแหน่งใด
    pass =  ไม่มีการทำใดๆ ในสเตทเม้น ใช้ตอนรอรอบการทำต่อไป
'''

# break
'''
i=0
while i < 10:
    i+=1
    if i>3:
        break
    print(i)
print('...')
'''

# continue
'''
i=0
while i<10:
    i+=1
    if i >= 5 and i <= 7:
        continue
    print(i)

print('...')
'''

# pass
'''
i = 0
while i < 10:
    i+=1
    pass
    print(i)

print('......')
'''

#---***

#///////////////////
#FUNCTION
'''
def Function_1():
    print('Hello Function 1')
    #print('Z = ',z)



def ADD(i, x):# รับค่า พารามิเตอร์เข้ามา
    print('FUNCTION_ADD')
    return i + x

e = 80
f = 20
Function_1()

A = ADD(e, f)
print('E+F = A: '+  str(e)+ '+' + str(f)+ '=' + str( A))# แปลง int ให้เป็น string ก่อนแสดงผล
'''


#*******
# global variabel
'''
i = 20
def F_1():
    global i  # การเรียกใช้ตัวแปรภายใฟังก์ชั่นให้ใช้ global
    print('Function_1')
    i+=5
    print(i)

F_1()
'''
#*************************************

# การใช้งานโมดูล เรียกใช้โดย import moddule
# ในที่นี้ นำฟังก์ชั่นที่สร้างขึ้นนี้ นำไป save เป็น Ex_module.py
# MODULE
'''
def f_1(a):
    a = a+1 # เพิ่มค่า 1
    return a

def f_add(a, b):
    return a + b # รวมค่า a+b
'''
# การใช้งานโมดูล เรียกใช้โดย import moddule
# ในที่นี้ นำฟังก์ชั่นที่สร้างขึ้นนี้ นำไป save เป็น Ex_module.py
'''
import Ex_module as num

a = 50
b = 20

i = num.f_add(a, b) # การใช้โมดูลบวกค่า a+b
print('module a+b ',i)
i = num.f_1(i) # การใช้โมดูลบวกค่า  i +1
print('module +1 ',i)
print('.......')
'''

# num.help() # เรียกดูฟังก์ชันใน module

#****************************************

import math

#help(math)
#-------------------------------


#from sound.effeats import echo

#-------------------------------

# การใช้ INPUT() รับข้อมูลจากคีย์บอร์ด

#name = input('Enter Name: ')
#print('สวัสดี:',name)
'''
i = input('ENTER NUMBER: ')
if (int(i)):
    print('คุณป้อนเลข: ',i) # เช็ค input ที่ป้อนเข้ามา
'''

#**************
#String Format() จัดรูปแบบการแสดงผล ฟอร์แมทข้อมูล
'''
price  = 100
food = 200
sum = price + food

txt = "ซื้ออาหาร {} บาท\n รายจ่าย {} บาท\n ยอดรวม {:.2f} บาท\n" #.2f ค่าทศนิยม 2 ตำแหน่ง
print(txt.format(food, price, sum)) #การใช้งาน fomat string แบบ 1  \n=ขึ้นบรรทัดใหม่

print(f'ซื้ออาหาร {food}บาท\n รายจ่าย {price} บาท\n ยอดรวม {sum:.2f} บาท\n') #การใช้งาน fomat string แบบ 2

txt2 = f'ซื้ออาหาร {food} บาท\n รายจ่าย {price} บาท\n ยอดรวม {sum:.2f} บาท'
print(txt2)

print('..........')
'''
#***************************************************************

# การใช้ DATE TIME
'''
import datetime as dt
T = dt.datetime.now()
print('DateTime: ', T)

#date
print('วันที่:',T.day)
print('เดือน:',T.month)
print('ปี:',T.year)
print('.....')

#Time
print(T.hour)
print(T.minute)
print(T.second)
print(T.microsecond)

'''
#-----------------------------

# เช็ค ERROR codecs

try:
    print(i/r)

except:
    print('check error')

#************************************
