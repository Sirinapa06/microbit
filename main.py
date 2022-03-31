def on_logo_pressed():
    music.play_melody("D G - D E C C - ", 120)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
