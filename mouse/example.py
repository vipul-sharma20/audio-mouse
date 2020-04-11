from mouse import LineIn, Mouse


def main():
    line_in = LineIn()
    m = Mouse()

    stream = line_in.record()
    line_in.detect_pitch(m, stream)


if __name__ == "__main__":
    main()
