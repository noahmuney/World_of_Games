from Utils import SCORES_FILE_NAME


def add_score(diff):
    POINTS_OF_WINNING = (diff * 3) + 5
    try:
        file = open(SCORES_FILE_NAME, "r")
        existing = file.read()
        file.close()
    except FileNotFoundError:
        file = open(SCORES_FILE_NAME, "w+")
        file.write(str(POINTS_OF_WINNING))
    else:
        file = open(SCORES_FILE_NAME, "w+")
        file.write(str(int(existing) + POINTS_OF_WINNING))
    finally:
        file.close()

