# MODULE
def help():
    print('............................')
    FF = '\ndef f_1(a):\n \ta += 1 # เพิ่มค่า 1\n\treturn a''\ndef f_add(a, b):\n\treturn a + b # รวมค่า a+b'
    print('function: ',FF)
    print('............................')


def f_1(a):
    a = a+1
    return a

def f_add(a, b):
    return a + b

print('............................')
