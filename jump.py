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
FACTOR = 1.37

while True:
    # Get screenshot
    os.popen(ADB_PATH + r" shell screencap -p /sdcard/1.png").read()
    os.popen(ADB_PATH + r" pull /sdcard/1.png").read()

    # Show
    img = mimg.imread("1.png")
    # plt.switch_backend('TkAgg')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed') # Tk backend
    #mng.window.showMaximized() # Qt backend
    #mng.frame.Maximize(True) # wx backend
    plt.imshow(img)
    pos = plt.ginput(2)
    plt.close()

    # Calculate time
    vector = (pos[1][0] - pos[0][0], -pos[1][1] + pos[0][1])
    print(vector)
    if vector[0] > 0:
        leng = vector[0] / 2 + vector[1] * math.sqrt(3) / 2
    else:
        leng = -vector[0] / 2 + vector[1] * math.sqrt(3) / 2
    leng *= 2 / math.sqrt(3)
    t = leng * FACTOR

    scrposx = int(0.6 * WIDTH) + random.uniform(-100, 100)
    scrposy = int(0.8 * HEIGHT) + random.uniform(-100, 100)
    scrpos = [str(scrposx), str(scrposy),
              str(scrposx + random.uniform(-5, 5)),
              str(scrposy + random.uniform(-5, 5))]
    scrposstr = ' '.join(scrpos) + ' '
    command = ADB_PATH + " shell input swipe " + scrposstr + str(int(t))
    os.popen(command).read()
    # print()
    time.sleep(1)
