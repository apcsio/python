from apcs import Window

x = 50
dx = 5

def frame():
    global x, dx
    Window.out.circle(x, 200, 50)
    x = x + dx

    if x > 450:
        dx = -5
    if x < 50:
        dx = 5

    

Window.size(500, 500)
Window.frame(frame)
Window.start()
