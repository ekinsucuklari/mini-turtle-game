import turtle #bu görüntü ekranımızı yapmamızı ve hareketlerimizi sağlayan bir kütüphane
import random

pencere = turtle.Screen() #ekran oldu
pencere.screensize(600, 600)
pencere.title("Çünkü Deden Kaplumbağa")
pencere.bgcolor("blue")
pencere.tracer(1) #nesnelerin hareketini artırabiliriz

oyuncu = turtle.Turtle()#nesne yaptık
oyuncu.color("white")
oyuncu.shape("triangle")
oyuncu.shapesize(2)
oyuncu.penup() 

score = 0

yaziPuan = turtle.Turtle()
yaziPuan.speed(0)
yaziPuan.shape("square")
yaziPuan.color("white")
yaziPuan.penup()
yaziPuan.hideturtle()
yaziPuan.goto(-200,200)
yaziPuan.write("Puan: {}".format(score),align="center",font=("Courier",24,"normal"))

speed = 1 #bu global bir değişkendir fonskiyon içinden ulaşmak için belirtilmelidir

def solaDon():
    oyuncu.left(30)

def sagaDon():
    oyuncu.right(30)

def hiziArtir():
    global speed 
    speed += 1

def hiziAzalt():
    global speed 
    speed -= 1

pencere.listen()#olanları algılayacak
pencere.onkey(solaDon,'Left')
pencere.onkey(sagaDon,'Right')
pencere.onkey(hiziArtir,'Up')
pencere.onkey(hiziAzalt,'Down')

maxHedef = 5
hedefler = []
for i in range(maxHedef):
    hedefler.append(turtle.Turtle())
    hedefler[i].penup()
    hedefler[i].color("yellow")
    hedefler[i].shape("turtle")
    hedefler[i].speed(0)
    hedefler[i].setposition(random.randint(-300,300),random.randint(-300,300)) #random kütüphanesini eklemek gerekti

while True:
    oyuncu.forward(speed)#oyuncunun hızı

    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180)
    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)

    for i in range(maxHedef):
        hedefler[i].forward(1)
        if hedefler[i].xcor() >500 or hedefler[i].ycor() < -500:
            hedefler[i].right(random.randint(150,250))
        if hedefler[i].ycor() >500 or hedefler[i].ycor() < -500:
            hedefler[i].right(random.randint(150,250))

        if oyuncu.distance(hedefler[i]) < 40: #hedefe çarpınca olanlar
            hedefler[i].setposition(random.randint(-300,300),random.randint(-300,300))
            hedefler[i].right(random.randint(0,360))
            score += 1
            yaziPuan.clear()
            yaziPuan.write("Puan: {}".format(score),align="center",font=("Courier",24,"normal"))