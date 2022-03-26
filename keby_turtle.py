import turtle
t=turtle.Pen() #ดึงความสามารถการใช้ปากกา
t.shape('turtle') #แปลงร่างเป็นรูปเต่า

def go(x,y):
    '''Function ย้ายเต่า'''
    t.penup()
    t.goto(x,y)
    t.pendown()

def triangle():
    '''function นี้วาดสามเหลี่ยมด้านเท่า'''
    for i in range(3):
            t.fd(115.47)
            t.lt(120)
		
def square():
    '''function นี้วาดสี่เหลี่ยมด้านเท่า'''
    for i in range(4):
            t.forward(100)
            t.left(90)

def pentagon():
    '''function นี้วาดห้าเหลี่ยมด้านเท่า'''
    for i in range(5):
            t.forward(64.98)
            t.left(72)

def hexagon():
    '''function นี้วาดหกเหลี่ยมด้านเท่า'''
    for i in range(6):
            t.forward(57.74)
            t.left(60)

def heptagon():
    '''function นี้วาดเจ็ดเหลี่ยมด้านเท่า'''
    for i in range(7):
            t.forward(48.16)
            t.left(51.4285714286)

def octagon():
    '''function นี้วาดเจ็ดเหลี่ยมด้านเท่า'''
    for i in range(8):
            t.forward(41.42)
            t.left(45)

go(-250,150)
triangle()
go(-50,150)
square()
go(150,150)
pentagon()
go(-250,-150)
hexagon()
go(-50,-150)
heptagon()
go(150,-150)
octagon()
