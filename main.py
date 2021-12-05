import eel

eel.init('web')


@eel.expose
def processFile(a, b):
    print(a, b, a + b)


eel.start('main.html')