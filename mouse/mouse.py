import logging
from datetime import datetime

import aubio
import numpy as np
import pyaudio
import autopy

from mouse import constants
from mouse import utils
from mouse.constants import Binds


class LineIn:
    """
    Line input (mic, instrument etc)
    """
    def __init__(self, *args, **kwargs):
        self.pyaudio_instance = pyaudio.PyAudio()

    def record(self):
        """
        Get stream from input source

        :returns: pyaudio stream instance
        """
        stream = self.pyaudio_instance.open(
                            format=pyaudio.paFloat32,
                            channels=1, rate=44100, input=True,
                            frames_per_buffer=1024)
        return stream

    def detect_pitch(self, mouse, stream) -> None:
        """
        Detect pitch of input chunks

        :param mouse: mouse handler instance
        :param stream: pyaudio stream instance

        :returns: None
        """
        pitch_detect = aubio.pitch("default", 2048, 2048//2, 44100)

        pitch_detect.set_unit("Hz")
        pitch_detect.set_silence(-40)
        print("Started. Hit the notes..")

        while True:
            data = stream.read(1024, exception_on_overflow=False)
            samples = np.fromstring(data, dtype=aubio.float_type)
            pitch = pitch_detect(samples)[0]

            # Compute the energy (volume) of the current frame.
            volume = np.sum(samples**2) / len(samples)
            volume = "{:.6f}".format(volume)

            mouse.handle_mouse(pitch)


class Mouse(Binds):
    """
    Mouse handler class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle_mouse(self, pitch: float) -> None:
        """
        Execute mouse events

        :param pitch: pitch of the recorded chunk

        :returns: None
        """
        direction = None
        freq = int(pitch)
        note = utils.pitch_to_note(freq)

        if note == self.UP:
            direction = constants.UP
        elif note == self.DOWN:
            direction = constants.DOWN
        elif note == self.UP_RIGHT:
            direction = constants.UP_RIGHT
        elif note == self.UP_LEFT:
            direction = constants.UP_LEFT
        elif note == self.RIGHT:
            direction = constants.RIGHT
        elif note == self.LEFT:
            direction = constants.LEFT
        elif note == self.DOWN_RIGHT:
            direction = constants.DOWN_RIGHT
        elif note == self.DOWN_LEFT:
            direction = constants.DOWN_LEFT
        else:
            pass

        if direction:
            self._move(direction)

        # autopy.mouse.toggle(autopy.mouse.Button.LEFT, self.left_click_toggle)

    def _move(self, direction: str) -> None:
        """
        Move mouse pointer

        :param direction: Direction to move in

        :returns: None
        """
        current_x, current_y = autopy.mouse.location()

        x, y = constants.MOVEMENT_MAP[direction]
        try:
            autopy.mouse.smooth_move(current_x + x, current_y + y)
        except ValueError:
            print(f"Cannot reach coordinates: ({x}, {y})")
            pass

