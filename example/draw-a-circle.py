from apcs import Window

def frame():
    Window.out.circle(50, 50, 100)

Window.size(500, 500)
Window.frame(frame)
Window.start()

