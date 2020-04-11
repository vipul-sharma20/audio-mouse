from math import log2, pow

from mouse import constants


def pitch_to_note(pitch: float) -> str:
    """
    Convert pitch of recorded chunk to note value

    :param pitch: pitch of the recorded chunk

    :returns: Note value (eg: A4, B2 etc)
    """
    pitch = int(pitch)

    if not pitch:
        return ''

    A4 = 440
    C0 = A4*pow(2, -4.75)

    h = round(12*log2(pitch/C0))
    octave = h // 12
    n = h % 12

    return constants.NOTE_NAME[n] + str(octave)

