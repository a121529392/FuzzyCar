from matplotlib import pyplot as plt
from matplotlib import animation
from run import Fuzzy_car
import math


def get_left_x_y(car_position, l_dis, l_degree):
    left_pos_x = []
    left_pos_y = []
    print(len(l_degree))
    print(len(car_position))
    for num, i in enumerate(car_position):
        hold_x = [i[0], i[0] + l_dis[num] * math.cos(math.radians(l_degree[num]))]
        hold_y = [i[1], i[1] + l_dis[num] * math.sin(math.radians(l_degree[num]))]
        left_pos_x.append(hold_x)
        left_pos_y.append(hold_y)
    return left_pos_x, left_pos_y


def get_front(car_position, f_dis, wheel_degree):
    front_pos_x = []
    front_pos_y = []
    print(len(wheel_degree))
    print(len(car_position))
    for num, i in enumerate(car_position):
        # print("we : %s"%wheel_degree[num])
        hold_x = [i[0], i[0] + f_dis[num] * math.cos(math.radians(wheel_degree[num]))]
        hold_y = [i[1], i[1] + f_dis[num] * math.sin(math.radians(wheel_degree[num]))]
        front_pos_x.append(hold_x)
        front_pos_y.append(hold_y)
    return front_pos_x, front_pos_y


def get_right_x_y(car_position, r_dis, r_degree):
    right_pos_x = []
    right_pos_y = []
    for num, i in enumerate(car_position):
        hold_x = [i[0], i[0] + r_dis[num] * math.cos(math.radians(r_degree[num]))]
        hold_y = [i[1], i[1] + r_dis[num] * math.sin(math.radians(r_degree[num]))]
        right_pos_x.append(hold_x)
        right_pos_y.append(hold_y)
    return right_pos_x, right_pos_y


def draw_moving_car(file,front_large_mean, front_large_sigma,
                        front_medium_mean, front_medium_sigma,
                        front_small_mean, front_small_sigma,
                 deviation_large_mean, deviation_large_sigma,
                 deviation_medium_mean, deviation_medium_sigma,
                 deviation_small_mean, deviation_small_sigma,
                 wheel_large_mean, wheel_large_sigma,
                 wheel_medium_mean, wheel_medium_sigma,
                 wheel_small_mean, wheel_small_sigma):
    fuzzy = Fuzzy_car(file,front_large_mean, front_large_sigma,
                        front_medium_mean, front_medium_sigma,
                        front_small_mean, front_small_sigma,
                 deviation_large_mean, deviation_large_sigma,
                 deviation_medium_mean, deviation_medium_sigma,
                 deviation_small_mean, deviation_small_sigma,
                 wheel_large_mean, wheel_large_sigma,
                 wheel_medium_mean, wheel_medium_sigma,
                 wheel_small_mean, wheel_small_sigma)
    fuzzy.run()
    bound = fuzzy.get_bound()
    print(bound)
    bound_x = []
    bound_y = []
    for i in bound:
        bound_x.append(i[0])
        bound_y.append(i[1])

    f = open("Train6D.txt", "r")
    line = f.read()
    line = line.split("\n")

    car_position = []
    car_position_x = []
    car_position_y = []
    wheel_degree = []
    f_dis = []
    r_dis = []
    l_dis = []
    l_degree = []
    r_degree = []
    theta=[]
    default_degree=90
    for l in line:
        if len(l) == 0:
            break
        else:
            l = l.split(',')
            hold = (float(l[0]), float(l[1]))
            car_position_x.append(float(l[0]))
            car_position_y.append(float(l[1]))
            car_position.append(hold)
            f_dis.append(float(l[2]))
            r_dis.append(float(l[3]))
            l_dis.append(float(l[4]))
            theta.append(float(l[5]))
            # default_degree=default_degree-float(l[5])
            # wheel_degree.append(default_degree)

    wheel_degree=fuzzy.get_phi()
    for i in wheel_degree:
        r_degree.append(i-45)
        l_degree.append(45+i)

    left_pos_x, left_pos_y = get_left_x_y(car_position, l_dis, l_degree)
    front_pos_x, front_pos_y = get_front(car_position, f_dis, wheel_degree)
    right_pos_x, right_pos_y = get_right_x_y(car_position, r_dis, r_degree)

    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(7, 6.5)

    ax = plt.axes(xlim=(-50, 60), ylim=(-50, 90))
    car = plt.Circle((car_position[0][0], car_position[0][1]), 3, fc='#60a3e0')
    # dir=plt.plot(final_x, final_y)
    plt.plot(bound_x, bound_y, 'k-')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    textstr = "init"
    time_text = ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
                        verticalalignment='top', bbox=props)

    left_line, = ax.plot(left_pos_x[0], left_pos_y[0], '#eaff29')
    front_line, = ax.plot(front_pos_x[0], front_pos_y[0], '#ffeb3b')
    right_line, = ax.plot(right_pos_x[0], right_pos_y[0], '#eaff29')

    click_text = "Click to Start"
    click = ax.text(-40, -40, click_text, fontsize=15, bbox=props)
    final_right_x, final_left_x, final_right_y, final_left_y = fuzzy.get_finish_line()
    final_x = [final_right_x, final_left_x]
    final_y = [final_right_y, final_left_y]

    plt.plot(final_x, final_y, color='#ff000d')

    # plt.axis('equal')
    anim_running = False
    Frist_flag = True
    Quit=False
    def onClick(event):
        nonlocal anim_running
        nonlocal Frist_flag
        if anim_running:
            anim_car.event_source.start()
            anim_running = False
        else:
            Frist_flag = False
            anim_car.event_source.start()
            anim_running = True

    def keypress(event):
        nonlocal Quit

        if Quit:
            plt.close()
            Quit = False
        else:
            Quit=False


    def init_car():
        car.center = (car_position[0][0], car_position[0][1])
        time_text.set_text('initial')
        click.set_text("Click to Start")
        # left_line.set_data(left_pos_x[0][0],left_pos_y[0][1])
        left_line.set_data(left_pos_x[0][0], left_pos_y[0][0])
        right_line.set_data(right_pos_x[0][0], right_pos_y[0][0])
        front_line.set_data(front_pos_x[0][0], front_pos_y[0][0])
        # left_line.set_ydata(left_pos_y[0])
        ax.add_patch(car)
        # ax.add_patch(left_line)

        return car, time_text, click, left_line,front_line,right_line,

    def animate_car(i):
        nonlocal anim_running
        nonlocal Quit
        if Frist_flag:
            anim_car.event_source.stop()

        if anim_running:
            click.set_text("Click to Stop")
            # anim_running= False
        else:
            click.set_text("Click to Start")
            anim_car.event_source.stop()
        x = car_position_x[i]
        y = car_position_y[i]
        car.center = (x, y)
        car.set_color('#60a3e0')
        time_text.set_text(
            'Front Distance : %s \nLeft Distance : %s\nRight Distance : %s\nWheel degree : %s' % (
            f_dis[i], l_dis[i], r_dis[i], theta[i]))
        if i == len(car_position_x) - 1:
            car.set_color("#29ff8d")
            click.set_text("Click to Restart \n or Press Key to Quit")
            Quit = True
            anim_car.event_source.stop()
        left_line.set_data(left_pos_x[i], left_pos_y[i])
        right_line.set_data(right_pos_x[i], right_pos_y[i])
        front_line.set_data(front_pos_x[i], front_pos_y[i])
        print(left_pos_x[i])
        # left_line.set_ydata(left_pos_y[i][0])
        return car, time_text, click, left_line,front_line,right_line,

    fig.canvas.mpl_connect('button_press_event', onClick)
    fig.canvas.mpl_connect('key_press_event', keypress)
    anim_car = animation.FuncAnimation(fig, animate_car,
                                       init_func=init_car,
                                       # frames=360,
                                       frames=len(car_position_x),
                                       interval=100,
                                       blit=True)
    plt.show()



