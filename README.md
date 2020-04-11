# audio-mouse

Control mouse with audio input.

This project is intended to use a guitar as an input source and use the notes
played on it to simulate mouse movements. But you can always use your voice and
control the mouse movements as long as you can hit those pitches which are
configured to trigger the mouse events

## Install

`pip install audio-mouse`

## Examples

### Basic example

```python
from mouse import LineIn, Mouse


def main():
    line_in = LineIn()
    mouse_handler = Mouse()

    stream = line_in.record()
    line_in.detect_pitch(mouse_handler, stream)


if __name__ == "__main__":
    main()
```

### Configuring notes/pitches

You can configure the notes you want to act as trigger for specific mouse
movements for example, you can configure that when a pitch of A2 is played the
mouse pointer moves up etc.


```python
from mouse import LineIn, Mouse


def main():
    line_in = LineIn()
    mouse_handler = Mouse()

    mouse_handler.UP = "A2"
    mouse_handler.DOWN = "B2"
    mouse_handler.RIGHT = "G3"
    # Events that are not configured will use the defaults (check constants.py)

    stream = line_in.record()
    line_in.detect_pitch(mouse_handler, stream)


if __name__ == "__main__":
    main()
```

### Configuring X/Y mouse speed

you can configure `Mouse.MOUSE_X` and `Mouse.MOUSE_Y` to update the speed of
the mouse.

```python
from mouse import LineIn, Mouse


def main():
    line_in = LineIn()
    mouse_handler = Mouse()

    mouse_handler.MOUSE_X = 10
    mouse_handler.MOUSE_Y = 10

    stream = line_in.record()
    line_in.detect_pitch(mouse_handler, stream)


if __name__ == "__main__":
    main()
```

## In action

Checkout this 30 seconds video for a demo:

[https://imgur.com/a/ECJwEFy](https://imgur.com/a/ECJwEFy)

## Scribbles

Looks like we can make a visual representation of what we play and speak and
use it for some analysis maybe? IDK. Play something and without listening to it
one can visually analyze some patterns maybe? Can make a note transcriber.
Maybe something like converting the recorded pitches to notes and then tabs? IDK

## License

MIT

