from tkinter import *
from tkinter import ttk

import os
from run import Fuzzy_car
from draw_car import *

data_dir = "./data"
image_dir = "./img"


class skin():

    def __init__(self):
        self.file = []
        for data in os.listdir(data_dir):
            self.file.append(data)
        title = Label(window, text='Please set the detial of fuzzy rule', font=('Consolas', 14))
        title.place(x=10, y=0)

        testcase = Label(window, text='Choose test case :', font=('Consolas', 12))
        testcase.place(x=10, y=40)

        comboExample = ttk.Combobox(window, values=self.file, font=('Consolas', 12))
        comboExample.place(x=10, y=70)
        comboExample.current(0)

        forward_large_mean = Label(window, text='Forward Large Mean:', font=('Consolas', 12))
        forward_large_mean.place(x=10, y=100)

        forward_large_variance = Label(window, text='Variance:', font=('Consolas', 12))
        forward_large_variance.place(x=300, y=100)

        forward_medium_mean = Label(window, text='Forward Medium Mean:', font=('Consolas', 12))
        forward_medium_mean.place(x=10, y=130)

        forward_medium_variance = Label(window, text='Variance:', font=('Consolas', 12))
        forward_medium_variance.place(x=300, y=130)

        forward_small_mean = Label(window, text='Forward Small Mean:', font=('Consolas', 12))
        forward_small_mean.place(x=10, y=160)

        forward_small_variance = Label(window, text='Variance:', font=('Consolas', 12))
        forward_small_variance.place(x=300, y=160)

        left_right_large_mean = Label(window, text='Left-Right Large Mean:', font=('Consolas', 12))
        left_right_large_mean.place(x=10, y=190)

        left_right_large_variance = Label(window, text='Variance:', font=('Consolas', 12))
        left_right_large_variance.place(x=300, y=190)

        left_right_medium_mean = Label(window, text='Left-Right Medium Mean:', font=('Consolas', 12))
        left_right_medium_mean.place(x=10, y=220)

        left_right_medium_variance = Label(window, text='Variance:', font=('Consolas', 12))
        left_right_medium_variance.place(x=300, y=220)

        left_right_small_mean = Label(window, text='Left-Right Small Mean:', font=('Consolas', 12))
        left_right_small_mean.place(x=10, y=250)

        wheel_small_variance = Label(window, text='Variance:', font=('Consolas', 12))
        wheel_small_variance.place(x=300, y=250)

        wheel_large_mean = Label(window, text='Wheel Large Mean:', font=('Consolas', 12))
        wheel_large_mean.place(x=10, y=280)

        wheel_large_variance = Label(window, text='Variance:', font=('Consolas', 12))
        wheel_large_variance.place(x=300, y=280)

        wheel_medium_mean = Label(window, text='Wheel Medium Mean:', font=('Consolas', 12))
        wheel_medium_mean.place(x=10, y=310)

        wheel_medium_variance = Label(window, text='Variance:', font=('Consolas', 12))
        wheel_medium_variance.place(x=300, y=310)

        wheel_small_mean = Label(window, text='Wheel Small Mean:', font=('Consolas', 12))
        wheel_small_mean.place(x=10, y=340)

        wheel_small_variance = Label(window, text='Variance:', font=('Consolas', 12))
        wheel_small_variance.place(x=300, y=340)

        # set text
        forward_large_mean_text = StringVar()
        forward_large_mean_text.set('20')
        forward_large_mean_entry = Entry(window, textvariable=forward_large_mean_text, width=8, font=('Consolas', 12))
        forward_large_mean_entry.place(x=200, y=100)

        forward_large_variance_text = StringVar()
        forward_large_variance_text.set('10')
        forward_large_variance_entry = Entry(window, textvariable=forward_large_variance_text, width=8,
                                             font=('Consolas', 12))
        forward_large_variance_entry.place(x=400, y=100)

        forward_medium_mean_text = StringVar()
        forward_medium_mean_text.set('10')
        forward_medium_mean_entry = Entry(window, textvariable=forward_medium_mean_text, width=8, font=('Consolas', 12))
        forward_medium_mean_entry.place(x=200, y=130)

        forward_medium_variance_text = StringVar()
        forward_medium_variance_text.set('5')
        forward_medium_variance_entry = Entry(window, textvariable=forward_medium_variance_text, width=8,
                                              font=('Consolas', 12))
        forward_medium_variance_entry.place(x=400, y=130)

        forward_small_mean_text = StringVar()
        forward_small_mean_text.set('5')
        forward_small_mean_entry = Entry(window, textvariable=forward_small_mean_text, width=8, font=('Consolas', 12))
        forward_small_mean_entry.place(x=200, y=160)

        forward_small_variance_text = StringVar()
        forward_small_variance_text.set('10')
        forward_small_variance_entry = Entry(window, textvariable=forward_small_variance_text, width=8,
                                             font=('Consolas', 12))
        forward_small_variance_entry.place(x=400, y=160)

        # l_r_large
        l_r_large_mean_text = StringVar()
        l_r_large_mean_text.set('6')
        l_r_large_mean_entry = Entry(window, textvariable=l_r_large_mean_text, width=8, font=('Consolas', 12))
        l_r_large_mean_entry.place(x=220, y=190)

        l_r_large_variance_text = StringVar()
        l_r_large_variance_text.set('4')
        l_r_large_variance_entry = Entry(window, textvariable=l_r_large_variance_text, width=8,
                                         font=('Consolas', 12))
        l_r_large_variance_entry.place(x=400, y=190)

        l_r_medium_mean_text = StringVar()
        l_r_medium_mean_text.set('0')
        l_r_medium_mean_entry = Entry(window, textvariable=l_r_medium_mean_text, width=8, font=('Consolas', 12))
        l_r_medium_mean_entry.place(x=220, y=220)

        l_r_medium_variance_text = StringVar()
        l_r_medium_variance_text.set('3')
        l_r_medium_variance_entry = Entry(window, textvariable=l_r_medium_variance_text, width=8,
                                          font=('Consolas', 12))
        l_r_medium_variance_entry.place(x=400, y=220)

        l_r_small_mean_text = StringVar()
        l_r_small_mean_text.set('-8')
        l_r_small_mean_entry = Entry(window, textvariable=l_r_small_mean_text, width=8, font=('Consolas', 12))
        l_r_small_mean_entry.place(x=220, y=250)

        l_r_small_variance_text = StringVar()
        l_r_small_variance_text.set('4')
        l_r_small_variance_entry = Entry(window, textvariable=l_r_small_variance_text, width=8,
                                         font=('Consolas', 12))
        l_r_small_variance_entry.place(x=400, y=250)

        # wheel
        wheel_large_mean_text = StringVar()
        wheel_large_mean_text.set('20')
        wheel_large_mean_entry = Entry(window, textvariable=wheel_large_mean_text, width=8, font=('Consolas', 12))
        wheel_large_mean_entry.place(x=180, y=280)

        wheel_large_variance_text = StringVar()
        wheel_large_variance_text.set('20')
        wheel_large_variance_entry = Entry(window, textvariable=wheel_large_variance_text, width=8,
                                           font=('Consolas', 12))
        wheel_large_variance_entry.place(x=400, y=280)

        wheel_medium_mean_text = StringVar()
        wheel_medium_mean_text.set('0')
        wheel_medium_mean_entry = Entry(window, textvariable=wheel_medium_mean_text, width=8, font=('Consolas', 12))
        wheel_medium_mean_entry.place(x=180, y=310)

        wheel_medium_variance_text = StringVar()
        wheel_medium_variance_text.set('20')
        wheel_medium_variance_entry = Entry(window, textvariable=wheel_medium_variance_text, width=8,
                                            font=('Consolas', 12))
        wheel_medium_variance_entry.place(x=400, y=310)

        wheel_small_mean_text = StringVar()
        wheel_small_mean_text.set('-20')
        wheel_small_mean_entry = Entry(window, textvariable=wheel_small_mean_text, width=8, font=('Consolas', 12))
        wheel_small_mean_entry.place(x=180, y=340)

        wheel_small_variance_text = StringVar()
        wheel_small_variance_text.set('20')
        wheel_small_variance_entry = Entry(window, textvariable=wheel_small_variance_text, width=8,
                                           font=('Consolas', 12))
        wheel_small_variance_entry.place(x=400, y=340)

        self.btn_train = Button(window, text='Run', font=('Consolas', 12), command=lambda: run()).place(x=200, y=370)

        def run():
            testcase = "%s/%s" % (data_dir, str(comboExample.get()))
            fuzzy = Fuzzy_car(testcase,
                              float(forward_large_mean_entry.get()), float(forward_large_variance_entry.get()),
                              float(forward_medium_mean_entry.get()), float(forward_medium_variance_entry.get()),
                              float(forward_small_mean_entry.get()), float(forward_small_variance_entry.get()),
                              float(l_r_large_mean_entry.get()), float(l_r_large_variance_entry.get()),
                              float(l_r_medium_mean_entry.get()), float(l_r_medium_variance_entry.get()),
                              float(l_r_small_mean_entry.get()), float(l_r_small_variance_entry.get()),
                              float(wheel_large_mean_entry.get()), float(wheel_large_variance_entry.get()),
                              float(wheel_medium_mean_entry.get()), float(wheel_medium_variance_entry.get()),
                              float(wheel_small_mean_entry.get()), float(wheel_small_variance_entry.get())
                              )
            # fuzzy.set_deviation_value(float(l_r_large_mean_entry.get()), float(l_r_large_variance_entry.get()),
            #                           float(l_r_medium_mean_entry.get()), float(l_r_medium_variance_entry.get()),
            #                           float(l_r_small_mean_entry.get()), float(l_r_small_variance_entry.get()))
            #
            # fuzzy.set_front_value(float(forward_large_mean_entry.get()), float(forward_large_variance_entry.get()),
            #                       float(forward_medium_mean_entry.get()), float(forward_medium_variance_entry.get()),
            #                       float(forward_small_mean_entry.get()), float(forward_small_variance_entry.get()))
            #
            # fuzzy.set_wheel_value(float(wheel_large_mean_entry.get()), float(wheel_large_variance_entry.get()),
            #                       float(wheel_medium_mean_entry.get()), float(wheel_medium_variance_entry.get()),
            #                       float(wheel_small_mean_entry.get()), float(wheel_small_variance_entry.get()))

            fuzzy.run()
            draw_moving_car(testcase,
                              float(forward_large_mean_entry.get()), float(forward_large_variance_entry.get()),
                              float(forward_medium_mean_entry.get()), float(forward_medium_variance_entry.get()),
                              float(forward_small_mean_entry.get()), float(forward_small_variance_entry.get()),
                              float(l_r_large_mean_entry.get()), float(l_r_large_variance_entry.get()),
                              float(l_r_medium_mean_entry.get()), float(l_r_medium_variance_entry.get()),
                              float(l_r_small_mean_entry.get()), float(l_r_small_variance_entry.get()),
                              float(wheel_large_mean_entry.get()), float(wheel_large_variance_entry.get()),
                              float(wheel_medium_mean_entry.get()), float(wheel_medium_variance_entry.get()),
                              float(wheel_small_mean_entry.get()), float(wheel_small_variance_entry.get()))


window = Tk()

window.title('My Window')

window.geometry('500x500')

app = skin()
window.mainloop()
