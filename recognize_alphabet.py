import numpy as np
import math


def alphabet(landmark_list):
    letter = ''

    if landmark_list[8][2] > landmark_list[5][2] and \
            landmark_list[12][2] > landmark_list[9][2] and \
            landmark_list[16][2] > landmark_list[13][2] and \
            landmark_list[20][2] > landmark_list[17][2] and \
            landmark_list[4][2] < landmark_list[5][2] and \
            landmark_list[4][1] > landmark_list[5][1] and \
            landmark_list[9][2] < landmark_list[0][2] and \
            landmark_list[19][1] < landmark_list[9][1]:
        letter = 'А'
    elif landmark_list[12][2] > landmark_list[8][2] and \
            landmark_list[16][2] > landmark_list[13][2] and \
            landmark_list[20][2] > landmark_list[17][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            landmark_list[12][2] < landmark_list[9][2]:
        letter = 'Б'
    elif landmark_list[8][2] < landmark_list[7][2] and \
            landmark_list[12][2] < landmark_list[11][2] and \
            landmark_list[16][2] < landmark_list[15][2] and \
            landmark_list[20][2] < landmark_list[17][2] and \
            landmark_list[4][1] > landmark_list[5][1] and \
            math.hypot(landmark_list[4][1] - landmark_list[14][1], landmark_list[4][2] - landmark_list[14][2]) > \
            math.hypot(landmark_list[4][1] - landmark_list[1][1], landmark_list[4][2] - landmark_list[1][2]):
        letter = 'В'
    elif landmark_list[9][2] > landmark_list[0][2] and \
            landmark_list[4][1] > landmark_list[5][1] and \
            landmark_list[12][2] < landmark_list[10][2] and \
            landmark_list[8][2] > landmark_list[6][2]:
        letter = 'Г'
    elif landmark_list[12][2] < landmark_list[10][2] and \
            landmark_list[8][2] < landmark_list[6][2] and \
            landmark_list[16][2] > landmark_list[15][2] and \
            landmark_list[20][2] > landmark_list[19][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            landmark_list[12][1] < landmark_list[8][1] and \
            math.hypot(landmark_list[8][1] - landmark_list[12][1], landmark_list[8][2] - landmark_list[12][2]) < \
            math.hypot(landmark_list[5][1] - landmark_list[9][1], landmark_list[5][2] - landmark_list[9][2]):
        letter = 'Д'
    elif landmark_list[11][2] < landmark_list[9][2] and \
            landmark_list[11][2] > landmark_list[10][2] and \
            landmark_list[7][2] > landmark_list[6][2] and \
            landmark_list[7][2] < landmark_list[5][2] and \
            landmark_list[19][2] < landmark_list[17][2] and \
            landmark_list[19][2] > landmark_list[18][2] and \
            landmark_list[15][2] < landmark_list[16][2] and \
            landmark_list[15][2] > landmark_list[14][2] and \
            math.hypot(landmark_list[4][1] - landmark_list[12][1], landmark_list[4][2] - landmark_list[12][2]) < \
            math.hypot(landmark_list[12][1] - landmark_list[11][1], landmark_list[12][2] - landmark_list[11][2]):
        letter = 'E'
    elif landmark_list[18][1] > landmark_list[17][1] and \
            landmark_list[15][1] > landmark_list[14][1] and \
            landmark_list[11][1] > landmark_list[10][1] and \
            landmark_list[2][1] > landmark_list[5][1] and \
            landmark_list[10][1] > landmark_list[5][1] and \
            landmark_list[20][2] > landmark_list[5][2] and \
            landmark_list[18][1] > landmark_list[5][1] and \
            math.hypot(landmark_list[4][1] - landmark_list[12][1], landmark_list[4][2] - landmark_list[12][2]) < \
            math.hypot(landmark_list[12][1] - landmark_list[11][1], landmark_list[12][2] - landmark_list[11][2]):
        letter = 'Ж'
    elif landmark_list[12][2] > landmark_list[9][2] and \
            landmark_list[16][2] > landmark_list[13][2] and \
            landmark_list[20][2] > landmark_list[17][2] and \
            landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            landmark_list[5][1] > landmark_list[17][1]:
        letter = 'З'
    elif landmark_list[8][2] > landmark_list[7][2] and \
            landmark_list[12][2] > landmark_list[11][2] and \
            landmark_list[16][2] < landmark_list[15][2] and \
            landmark_list[20][2] < landmark_list[19][2] and \
            landmark_list[0][2] > landmark_list[5][2] and \
            landmark_list[10][1] > landmark_list[5][1]:
        letter = 'И'
    elif landmark_list[8][2] > landmark_list[7][2] and \
            landmark_list[12][2] > landmark_list[11][2] and \
            landmark_list[16][2] < landmark_list[15][2] and \
            landmark_list[20][2] < landmark_list[19][2] and \
            landmark_list[0][2] > landmark_list[5][2] and \
            landmark_list[10][1] < landmark_list[5][1]:
        letter = 'Й'
    elif landmark_list[12][2] < landmark_list[10][2] and \
            landmark_list[8][2] < landmark_list[6][2] and \
            landmark_list[16][2] > landmark_list[15][2] and \
            landmark_list[20][2] > landmark_list[19][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            landmark_list[12][1] < landmark_list[8][1] and \
            math.hypot(landmark_list[8][1] - landmark_list[12][1], landmark_list[8][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[5][1] - landmark_list[9][1], landmark_list[5][2] - landmark_list[9][2]):
        letter = 'К'
    elif landmark_list[0][2] < landmark_list[9][2] and \
            landmark_list[12][2] > landmark_list[11][2] and \
            landmark_list[8][2] > landmark_list[7][2] and \
            landmark_list[16][2] < landmark_list[14][2] and \
            math.hypot(landmark_list[8][1] - landmark_list[12][1], landmark_list[8][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[5][1] - landmark_list[9][1], landmark_list[5][2] - landmark_list[9][2]):
        letter = 'Л'
    elif landmark_list[0][2] < landmark_list[9][2] and \
            landmark_list[12][2] > landmark_list[11][2] and \
            landmark_list[8][2] > landmark_list[7][2] and \
            landmark_list[16][2] > landmark_list[14][2] and \
            math.hypot(landmark_list[8][1] - landmark_list[12][1], landmark_list[8][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[5][1] - landmark_list[9][1], landmark_list[5][2] - landmark_list[9][2]) and \
            math.hypot(landmark_list[16][1] - landmark_list[12][1], landmark_list[16][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[13][1] - landmark_list[9][1], landmark_list[13][2] - landmark_list[9][2]):
        letter = 'М'
    elif landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[12][2] < landmark_list[9][2] and \
            landmark_list[16][2] > landmark_list[14][2] and \
            landmark_list[20][2] < landmark_list[17][2] and \
            landmark_list[4][1] < landmark_list[5][1]:
        letter = 'Н'
    elif landmark_list[12][2] < landmark_list[11][2] and \
            landmark_list[8][2] > landmark_list[6][2] and \
            landmark_list[20][2] < landmark_list[17][2] and \
            landmark_list[16][2] < landmark_list[13][2] and \
            math.hypot(landmark_list[8][1] - landmark_list[4][1], landmark_list[8][2] - landmark_list[4][2]) < \
            math.hypot(landmark_list[15][1] - landmark_list[14][1], landmark_list[15][2] - landmark_list[14][2]) and \
            math.hypot(landmark_list[12][1] - landmark_list[16][1], landmark_list[12][2] - landmark_list[16][2]) < \
            math.hypot(landmark_list[12][1] - landmark_list[4][1], landmark_list[12][2] - landmark_list[4][2]):
        letter = 'О'
    elif landmark_list[0][2] < landmark_list[9][2] and \
            landmark_list[12][2] > landmark_list[11][2] and \
            landmark_list[8][2] > landmark_list[7][2] and \
            landmark_list[16][2] < landmark_list[14][2] and \
            math.hypot(landmark_list[8][1] - landmark_list[12][1], landmark_list[8][2] - landmark_list[12][2]) <= \
            math.hypot(landmark_list[5][1] - landmark_list[9][1], landmark_list[5][2] - landmark_list[9][2]):
        letter = 'П'
    elif landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[12][2] > landmark_list[9][2] and \
            landmark_list[16][2] < landmark_list[14][2] and \
            landmark_list[20][2] < landmark_list[17][2] and \
            landmark_list[4][1] < landmark_list[5][1]:
        letter = 'Р'
    elif landmark_list[18][1] > landmark_list[13][1] and \
            landmark_list[14][1] > landmark_list[13][1] and \
            landmark_list[10][1] > landmark_list[13][1] and \
            landmark_list[2][1] > landmark_list[13][1] and \
            landmark_list[4][2] > landmark_list[6][2] and \
            landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[12][2] < landmark_list[9][2] and \
            landmark_list[16][2] < landmark_list[13][2] and \
            math.hypot(landmark_list[4][1] - landmark_list[12][1], landmark_list[4][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[12][1] - landmark_list[11][1], landmark_list[12][2] - landmark_list[11][2]):
        letter = 'С'
    elif landmark_list[0][2] < landmark_list[9][2] and \
            landmark_list[12][2] > landmark_list[11][2] and \
            landmark_list[8][2] > landmark_list[7][2] and \
            landmark_list[16][2] > landmark_list[14][2] and \
            math.hypot(landmark_list[8][1] - landmark_list[12][1], landmark_list[8][2] - landmark_list[12][2]) <= \
            math.hypot(landmark_list[5][1] - landmark_list[9][1], landmark_list[5][2] - landmark_list[9][2]) and \
            math.hypot(landmark_list[16][1] - landmark_list[12][1], landmark_list[16][2] - landmark_list[12][2]) <= \
            math.hypot(landmark_list[13][1] - landmark_list[9][1], landmark_list[13][2] - landmark_list[9][2]):
        letter = 'Т'
    elif landmark_list[18][2] < landmark_list[17][2] and \
            landmark_list[8][2] > landmark_list[5][2] and \
            landmark_list[12][2] > landmark_list[9][2] and \
            landmark_list[16][2] > landmark_list[13][2] and \
            landmark_list[18][1] < landmark_list[13][1] and \
            math.hypot(landmark_list[4][1] - landmark_list[5][1], landmark_list[4][2] - landmark_list[5][2]) > \
            math.hypot(landmark_list[4][1] - landmark_list[3][1], landmark_list[4][2] - landmark_list[3][2]) and \
            math.hypot(landmark_list[8][1] - landmark_list[4][1], landmark_list[8][2] - landmark_list[4][2]) > \
            math.hypot(landmark_list[8][1] - landmark_list[6][1], landmark_list[8][2] - landmark_list[6][2]):
        letter = 'У'
    elif landmark_list[20][1] > landmark_list[19][1] and \
            landmark_list[16][1] > landmark_list[15][1] and \
            landmark_list[12][1] > landmark_list[11][1] and \
            landmark_list[8][1] > landmark_list[7][1] and \
            landmark_list[4][2] < landmark_list[6][2]:
        letter = 'Ф'
    elif landmark_list[18][1] > landmark_list[13][1] and \
            landmark_list[14][1] > landmark_list[13][1] and \
            landmark_list[10][1] > landmark_list[13][1] and \
            landmark_list[2][1] > landmark_list[13][1] and \
            landmark_list[4][2] > landmark_list[6][2] and \
            landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[12][2] > landmark_list[9][2] and \
            landmark_list[16][2] > landmark_list[13][2] and \
            landmark_list[8][2] > landmark_list[6][2] and \
            math.hypot(landmark_list[4][1] - landmark_list[12][1], landmark_list[4][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[12][1] - landmark_list[11][1], landmark_list[12][2] - landmark_list[11][2]):
        letter = 'Х'
    elif landmark_list[20][2] > landmark_list[18][2] and \
            landmark_list[16][2] > landmark_list[14][2] and \
            landmark_list[10][1] > landmark_list[5][1] and \
            landmark_list[2][1] > landmark_list[5][1] and \
            math.hypot(landmark_list[8][1] - landmark_list[4][1], landmark_list[8][2] - landmark_list[4][2]) < \
            math.hypot(landmark_list[8][1] - landmark_list[6][1], landmark_list[8][2] - landmark_list[6][2]):
        letter = 'Ц'
    elif landmark_list[20][2] > landmark_list[18][2] and \
            landmark_list[16][2] > landmark_list[14][2] and \
            landmark_list[8][2] < landmark_list[7][2] and \
            landmark_list[12][2] < landmark_list[11][2] and \
            landmark_list[10][1] > landmark_list[5][1] and \
            landmark_list[2][1] > landmark_list[5][1]:
        letter = 'Ч'
    elif landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[12][2] < landmark_list[9][2] and \
            landmark_list[16][2] < landmark_list[14][2] and \
            landmark_list[20][2] > landmark_list[17][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            math.hypot(landmark_list[8][1] - landmark_list[16][1], landmark_list[8][2] - landmark_list[16][2]) <= \
            math.hypot(landmark_list[5][1] - landmark_list[13][1], landmark_list[5][2] - landmark_list[13][2]):
        letter = 'Ш'
    elif landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[12][2] < landmark_list[9][2] and \
            landmark_list[16][2] < landmark_list[14][2] and \
            landmark_list[20][2] > landmark_list[17][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            math.hypot(landmark_list[8][1] - landmark_list[12][1], landmark_list[8][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[5][1] - landmark_list[9][1], landmark_list[5][2] - landmark_list[9][2]) and \
            math.hypot(landmark_list[16][1] - landmark_list[12][1], landmark_list[16][2] - landmark_list[12][2]) > \
            math.hypot(landmark_list[13][1] - landmark_list[9][1], landmark_list[13][2] - landmark_list[9][2]):
        letter = 'Щ'
    elif landmark_list[12][2] > landmark_list[9][2] and \
            landmark_list[16][2] > landmark_list[13][2] and \
            landmark_list[20][2] > landmark_list[17][2] and \
            landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[4][1] > landmark_list[5][1] and \
            landmark_list[14][1] < landmark_list[5][1]:
        letter = 'Ъ'
    elif landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[12][2] > landmark_list[11][2] and \
            landmark_list[16][2] > landmark_list[15][2] and \
            landmark_list[20][2] < landmark_list[17][2] and \
            landmark_list[4][1] < landmark_list[5][1]:
        letter = 'Ы'
    elif landmark_list[12][2] > landmark_list[9][2] and \
            landmark_list[16][2] > landmark_list[13][2] and \
            landmark_list[20][2] > landmark_list[17][2] and \
            landmark_list[8][2] < landmark_list[5][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            landmark_list[5][1] < landmark_list[17][1]:
        letter = 'Ь'
    elif landmark_list[11][2] > landmark_list[10][2] and \
            landmark_list[15][2] > landmark_list[14][2] and \
            landmark_list[19][2] > landmark_list[18][2] and \
            landmark_list[8][2] < landmark_list[5][2]:
        letter = 'Э'
    elif landmark_list[18][1] > landmark_list[17][1] and \
            landmark_list[15][1] > landmark_list[14][1] and \
            landmark_list[11][1] > landmark_list[10][1] and \
            landmark_list[2][1] > landmark_list[5][1] and \
            landmark_list[10][1] > landmark_list[5][1] and \
            landmark_list[20][2] < landmark_list[5][2] and \
            math.hypot(landmark_list[4][1] - landmark_list[12][1], landmark_list[4][2] - landmark_list[12][2]) < \
            math.hypot(landmark_list[12][1] - landmark_list[11][1], landmark_list[12][2] - landmark_list[11][2]) and \
            math.hypot(landmark_list[4][1] - landmark_list[16][1], landmark_list[4][2] - landmark_list[16][2]) < \
            math.hypot(landmark_list[14][1] - landmark_list[16][1], landmark_list[14][2] - landmark_list[16][2]):
        letter = 'Ю'
    elif landmark_list[12][2] < landmark_list[10][2] and \
            landmark_list[8][2] < landmark_list[6][2] and \
            landmark_list[16][2] > landmark_list[15][2] and \
            landmark_list[20][2] > landmark_list[19][2] and \
            landmark_list[4][1] < landmark_list[5][1] and \
            landmark_list[12][1] > landmark_list[8][1]:
        letter = 'Я'

    return letter


if __name__ == '__main__':
    print(alphabet(np.ones((21, 3))))
