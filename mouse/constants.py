class Binds:
    UP = "A2"
    DOWN = "B2"
    UP_RIGHT = "D3"
    UP_LEFT = "E3"
    RIGHT = "G3"
    LEFT = "A3"
    DOWN_RIGHT = "C4"
    DOWN_LEFT = "D4"
    TOGGLE_LEFT_CLICK = "A4"
    MOVE_X = 10
    MOVE_Y = 10


UP_RIGHT = "up_right"
UP_LEFT = "up_left"
DOWN_RIGHT = "down_right"
DOWN_LEFT = "down_left"
UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

MOVEMENT_MAP = {
    UP_RIGHT: (Binds.MOVE_X, -Binds.MOVE_Y),
    UP_LEFT: (-Binds.MOVE_X, -Binds.MOVE_Y),
    DOWN_RIGHT: (Binds.MOVE_X, Binds.MOVE_Y),
    DOWN_LEFT: (-Binds.MOVE_X, Binds.MOVE_Y),
    UP: (0, -Binds.MOVE_Y),
    DOWN: (0, Binds.MOVE_Y),
    RIGHT: (Binds.MOVE_X, 0),
    LEFT: (-Binds.MOVE_X, 0)}


NOTE_NAME = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

