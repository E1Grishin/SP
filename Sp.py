import keyboard as kb
import pygame as pg
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import time

root = Tk()
root.withdraw()

pg.mixer.init()
pg.font.init()
arial12 = pg.font.SysFont('arial', 12)
hsesans = pg.font.SysFont('HSE Sans', 25)

pg.display.set_caption('SoundPlay')

class key:
    def __init__(self, key, previous_action: int, current_action: int):
        """
        Create an object
        :param key: Key bind
        :param previous_action: 1 if in previous cycle key was pressed, else 0
        :param current_action: 1 if in current cycle key was pressed, else 0
        """
        self.key = key
        self.previous_action = previous_action
        self.current_action = current_action

    def on_press(self):
        """
        Checks if key was pressed
        :return: bool
        """
        if self.previous_action == 0 and self.current_action == 1:
            return True
        else:
            return False

    def on_release(self):
        """
        Checks if key was released
        :return: bool
        """
        if self.previous_action == 1 and self.current_action == 0:
            return True
        else:
            return False

def write_saves(list, file_path):
    """
    Write saves to file
    :param list: list which contains saves
    :param file_path: path to file in which saves are contained
    :return: Nothing
    """
    f = open(file_path, 'r+')
    for i in range(len(list)):
        f.write(str(list[i]) + '\n')

def read_saves(list, file_path):
    """
    Read saves from file
    :param list: list which contains saves
    :param file_path: path to file in which saves are contained
    :return: list
    """
    f = open(file_path, "r+")
    list.clear()
    for i in range(9):
        list.append(f.readline().replace('\n',''))
    return list

class switch:
    def __init__(self, list_of_images, height, width, lmb, conditon ):
        """
        Create an object
        :param list_of_images: List with images
        :param height: height of an object
        :param width: width of an object
        :param lmb: Left mouse button is pressed, if yes than lmb = 1, else lmb = 0
        :param conditon: Two conditions: on(True), off(False)
        """
        self.list_of_images = list_of_images
        self.height = height
        self.width = width
        self.lmb = lmb
        self.condition = conditon
    def draw(self, x, y):
        """
        Draw an object on a surface
        :param x: pixel on x-axis
        :param y: pixel on y-axis
        :return: bool
        """
        mouse = pg.mouse.get_pos()

        if (x < mouse[0] < x + self.width) and (y < mouse[1] < y + self.height):

            if self.lmb == 1:
                return True

        if self.condition == True:

            bt = pg.image.load(self.list_of_images[4])
            bt = pg.transform.scale(bt, (self.width, self.height))
            Window.blit(bt, (x, y))

        else:
            bt = pg.image.load(self.list_of_images[0])
            bt = pg.transform.scale(bt, (self.width, self.height))
            Window.blit(bt, (x, y))

class button:
    def __init__(self, list_of_images, height, width, lmb ):
        """
        Create an object
        :param list_of_images: List with images
        :param height: height of an object
        :param width: width of an object
        :param lmb: Two conditions: on(True), off(False)
        """
        self.list_of_images = list_of_images
        self.height = height
        self.width = width
        self.lmb = lmb


    def draw(self, x, y,):
        """
        :param x: pixel on x-axis
        :param y: pixel on y-axis
        :return:
        """
        mouse = pg.mouse.get_pos()

        if (x < mouse[0] < x + self.width) and (y < mouse[1] < y + self.height):
            bt = pg.image.load(self.list_of_images[0])
            bt = pg.transform.scale(bt, (self.width,  self.height))
            Window.blit(bt, (x, y))
            if self.lmb == 1:
                return True

        else:
            bt = pg.image.load(self.list_of_images[9])
            bt = pg.transform.scale(bt, (self.width, self.height))
            Window.blit(bt, (x, y))

if __name__ == "__main__":
    pg.init()

    Window = pg.display.set_mode((1000, 900))

    bl = []
    pbl =[]
    for i in range(10):
        bl.append("but/" + str(i) + "Button.png")
        pbl.append("bt test/" + str(i) + "Button.png")
    sl = []
    for i in range(5):
        sl.append("swanim/" + str(i) + ".png")

    FPS = 30
    clock = pg.time.Clock()

    run = True
    t = 0
    cf = 0

    space = key("space", 0, 0)

    btn = { }
    preset_but = { }
    swt_cnd = [[False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False]]
    sounds = []
    keys = []
    key_binds = []
    now_plaing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    preset = 0
    curent_key = 0
    settings_but = { }

    for i in range(9):
        keys.append(key(None, 0, 0))

    #main loop
    while run:

        read_saves(key_binds, "saves/keys" + str(preset + 1) + ".txt")
        read_saves(sounds, "saves/sounds" + str(preset + 1) + ".txt")

        lmb = 0
        for i in pg.event.get():
            if i.type == pg.MOUSEBUTTONDOWN:
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    lmb = 1
            if i.type == pg.QUIT:
                run = False

        for i in range(0, 9):
            btn[i] = button(bl, 200, 200, lmb)
        for i in range(3):
            preset_but[i] = button(pbl, 150, 300, lmb)
        for i in range(2):
            settings_but[i] = button(pbl, 100, 200, lmb)

        swt = switch(sl, 50, 100, lmb, swt_cnd[preset][curent_key])

        cf += 1
        if cf > FPS:
            cf = 0




        f = "bg_an/Bg" + str(t) + ".gif"
        clock.tick(FPS)
        bg = pg.image.load(f)
        t+=1
        if t>74:
            t=0
        bg = pg.transform.scale(bg, Window.get_size())
        Window.fill((200, 0, 150))
        Window.blit(bg,(0,0))

        bar = pg.image.load("bar.png")
        Window.blit(bar, (0, 600))

        if swt.draw(50, 650):
            swt_cnd[preset][curent_key] = not swt_cnd[preset][curent_key]

        for i in range(3):
            if preset_but[i].draw(50, 25 + 200*i):
                preset = i

        for i in range(0,9):
            if i<3:
                if btn[i].draw(400 + i*200, 10):
                    curent_key = i
            elif i<6:
                if btn[i].draw(400 + i%3*200,210):
                    curent_key = i
            else:
                if btn[i].draw(400 + i%3*200, 410):
                    curent_key = i
        for i in range(2):
            if settings_but[i].draw(450 + 250*i, 650):
                if i == 0:
                    key_binds[curent_key] = kb.read_key()
                    write_saves(key_binds, "saves/keys" + str(preset + 1) + ".txt")
                else:
                    sounds[curent_key] = filedialog.askopenfilename(filetypes=[("mp3 files", ".mp3")])
                    write_saves(sounds, "saves/sounds" + str(preset + 1) + ".txt")



        for i in range(9):
            try:
                a = int(key_binds[i])
            except:
                a = str(key_binds[i])
            keys[i].key = a

            if kb.is_pressed(keys[i].key):
                keys[i].current_action = 1
            else:
                keys[i].current_action = 0

            if kb.is_pressed('space'):

                if keys[i].on_press():
                    s = pg.mixer.Sound(sounds[i])
                    s.play(loops=-1)
                    now_plaing[i] = s


            else:
                if swt_cnd[preset][i] == True:
                    try:
                        s = open(sounds[i])
                        if keys[i].on_press():
                            try:
                                now_plaing[i].stop()
                            except:
                                pass
                            s = pg.mixer.Sound(sounds[i])
                            s.play(loops=-1)
                            now_plaing[i] = s
                        if keys[i].on_release():
                            now_plaing[i].stop()
                    except:
                        print("key " + str(i) + ": can not open file")

                else:
                    try:
                        now_plaing[i].stop()
                    except:
                        pass
                    finally:
                        if keys[i].on_press():
                            try:
                                s = pg.mixer.Sound(sounds[i])
                                s.play()
                            except:
                                print("key " + str(i) + ": can not open file")
            keys[i].previous_action = keys[i].current_action


        pg.draw.rect(Window, (150, 150, 150), (0, 600, 1000, 25) )
        txt = hsesans.render(("Preset: "+ str(preset + 1) + " Key: " + str(curent_key + 1)), True, (255, 255, 255), None)
        Window.blit(txt, (450, 604))


        pg.display.update()

    write_saves(key_binds, "saves/keys" + str(preset + 1) + ".txt")
    write_saves(sounds, "saves/sounds" + str(preset + 1) + ".txt")

#sudo python3 main.py