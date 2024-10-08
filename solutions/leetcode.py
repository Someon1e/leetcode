def test(result, correct):
    print(
        ("\x1b[92m" if result == correct else "\x1b[91m")
        + str(result)
        + " = "
        + str(correct)
        + "\x1b[0m",
    )


def in_place(f, *args):
    f(*args)
    return args
