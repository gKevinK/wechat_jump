# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimg
import time
import math
import random
import os

ADB_PATH = r"platform-tools\adb.exe"
WIDTH = 1080
HEIGHT = 1920

while True:
    os.popen(ADB_PATH + r" shell screencap -p /sdcard/1.png").read()
    os.popen(ADB_PATH + r" pull /sdcard/1.png").read()
    img = mimg.imread("1.png")
    plt.imshow(img)
    pos = plt.ginput(2)
    plt.close()
    vector = (pos[1][0] - pos[0][0], -pos[1][1] + pos[0][1])
    print(vector)
    if vector[0] > 0:
        leng = vector[0] / 2 + vector[1] * math.sqrt(3) / 2
    else:
        leng = -vector[0] / 2 + vector[1] * math.sqrt(3) / 2
    leng *= 2 / math.sqrt(3)
    t = leng * 1.37

    scrposx = int((0.6 + 0.1 * random.random()) * WIDTH)
    scrposy = int((0.8 + 0.1 * random.random()) * HEIGHT)
    scrpos = [str(scrposx), str(scrposy), str(scrposx), str(scrposy)]
    scrposstr = ' '.join(scrpos) + ' '
    command = ADB_PATH + " shell input swipe " + scrposstr + str(int(t))
    os.popen(command).read()
    # print()
    time.sleep(1)
