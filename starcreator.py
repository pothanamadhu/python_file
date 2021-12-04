import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(10)
col=['yellow','blue','white','green','white','red','pink']
c=0
for i in range(60):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==6:
        c=0
    else:
        c=c+1
