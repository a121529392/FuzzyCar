import shapely.geometry as sp
import math
from fuzzy_rule import *
from move_method import phi, x_position, y_position


class Train4D():
    def __init__(self, front_distance, left_distance, right_distance, theta):
        self.front_distance = front_distance
        self.left_distance = left_distance
        self.right_distance = right_distance
        self.theta = theta


class Train6D():
    def __init__(self, x, y, front_distance, left_distance, right_distance, theta):
        self.x = x
        self.y = y
        self.front_distance = front_distance
        self.left_distance = left_distance
        self.right_distance = right_distance
        self.theta = theta


class Fuzzy_car():
    def __init__(self, file,front_large_mean, front_large_sigma,
                        front_medium_mean, front_medium_sigma,
                        front_small_mean, front_small_sigma,
                 deviation_large_mean, deviation_large_sigma,
                 deviation_medium_mean, deviation_medium_sigma,
                 deviation_small_mean, deviation_small_sigma,
                 wheel_large_mean, wheel_large_sigma,
                 wheel_medium_mean, wheel_medium_sigma,
                 wheel_small_mean, wheel_small_sigma
                 ):
        self.default_theta = 0  # 方向盤角度
        self.car_length = 6
        self.default_x = None
        self.default_y = None
        self.default_phi = None
        self.final_left_x = None
        self.final_left_y = None
        self.final_right_x = None
        self.final_right_y = None
        self.bound = []
        self.file = file
        self.train4D = []
        self.train6D = []
        self.line = []
        self.phi = []
        self.get_case_data()
        self.front_large_mean = front_large_mean
        self.front_large_sigma = front_large_sigma
        self.front_medium_mean = front_medium_mean
        self.front_medium_sigma = front_medium_sigma
        self.front_small_mean = front_small_mean
        self.front_small_sigma = front_small_sigma

        # 左減右的值
        self.deviation_large_mean = deviation_large_mean
        self.deviation_large_sigma = deviation_large_sigma
        self.deviation_medium_mean = deviation_medium_mean
        self.deviation_medium_sigma = deviation_medium_sigma
        self.deviation_small_mean = deviation_small_mean
        self.deviation_small_sigma = deviation_small_sigma

        self.wheel_large_mean = wheel_large_mean
        self.wheel_large_sigma = wheel_large_sigma
        self.wheel_medium_mean = wheel_medium_mean
        self.wheel_medium_sigma = wheel_medium_sigma
        self.wheel_small_mean = wheel_small_mean
        self.wheel_small_sigma = wheel_small_sigma

    def set_front_value(self, front_large_mean, front_large_sigma,
                        front_medium_mean, front_medium_sigma,
                        front_small_mean, front_small_sigma):
        self.front_large_mean = front_large_mean
        self.front_large_sigma = front_large_sigma
        self.front_medium_mean = front_medium_mean
        self.front_medium_sigma = front_medium_sigma
        self.front_small_mean = front_small_mean
        self.front_small_sigma = front_small_sigma

    def set_deviation_value(self, deviation_large_mean, deviation_large_sigma,
                            deviation_medium_mean, deviation_medium_sigma,
                            deviation_small_mean, deviation_small_sigma):
        print("set_deviation_value")
        self.deviation_large_mean = deviation_large_mean
        print("self.deviation_large_mean")
        print(self.deviation_large_mean)
        self.deviation_large_sigma = deviation_large_sigma
        self.deviation_medium_mean = deviation_medium_mean
        self.deviation_medium_sigma = deviation_medium_sigma
        self.deviation_small_mean = deviation_small_mean
        self.deviation_small_sigma = deviation_small_sigma

    def set_wheel_value(self, wheel_large_mean, wheel_large_sigma,
                        wheel_medium_mean, wheel_medium_sigma,
                        wheel_small_mean, wheel_small_sigma):
        self.wheel_large_mean = wheel_large_mean
        self.wheel_large_sigma = wheel_large_sigma
        self.wheel_medium_mean = wheel_medium_mean
        self.wheel_medium_sigma = wheel_medium_sigma
        self.wheel_small_mean = wheel_small_mean
        self.wheel_small_sigma = wheel_small_sigma

    def write_Train4D_data(self):
        f = open("Train4D.txt", "w+")
        for t_4d in self.train4D:
            f.write("%s,%s,%s,%s" % (t_4d.front_distance, t_4d.left_distance, t_4d.right_distance, t_4d.theta))
            f.write("\n")
        f.close()

    def write_Train6D_data(self):
        f = open("Train6D.txt", "w+")
        for t_6d in self.train6D:
            f.write("%s,%s,%s,%s,%s,%s" % (
                t_6d.x, t_6d.y, t_6d.front_distance, t_6d.left_distance, t_6d.right_distance, t_6d.theta))
            f.write("\n")
        f.close()

    def bool_car_intersert_bound(self, car, area_bound):
        if area_bound.intersection(car).is_empty:
            return False
        else:
            return True

    def get_bound(self):
        for i in self.line:
            hold = []
            for p in i.split(','):
                hold.append(int(p))
            self.bound.append(tuple(hold))
        return self.bound

    def get_finish_line(self):
        return self.final_right_x, self.final_left_x, self.final_right_y, self.final_left_y

    def get_max_diameter(self, bound):
        max_x = bound[0][0]
        max_y = bound[0][1]
        min_x = bound[0][0]
        min_y = bound[0][0]
        for i in bound:
            if i[0] > max_x:
                max_x = i[0]
            if i[0] < min_x:
                min_x = i[0]
            if i[1] > max_y:
                max_y = i[1]
            if i[1] < min_y:
                min_y = i[1]
        diameter = ((max_x - min_x) ** 2 + (max_y - min_y) ** 2) ** (0.5)
        return diameter

    def get_case_data(self):

        f = open(self.file, "r")
        line = f.read()
        line = line.split("\n")
        # print(line)

        position = line[0]
        position = position.split(',')
        self.default_x = int(position[0])
        self.default_y = int(position[1])
        self.default_phi = int(position[2])
        line.pop(0)

        final_position_left = line[0]
        final_position_left = final_position_left.split(',')
        self.final_left_x = int(final_position_left[0])
        self.final_left_y = int(final_position_left[1])
        line.pop(0)

        final_position_right = line[0]
        final_position_right = final_position_right.split(',')
        self.final_right_x = int(final_position_right[0])
        self.final_right_y = int(final_position_right[1])
        line.pop(0)
        self.line = line
        return line

    def get_direction_distance(self, x, y, diameter, phi, area_bound):
        x = int(x)
        y = int(y)
        car_position = (x, y)

        front_point = (x + diameter * math.cos(math.radians(phi)), y + diameter * math.sin(math.radians(phi)))
        left_point = (x + diameter * math.cos(math.radians(phi + 45)), y + diameter * math.sin(math.radians(phi + 45)))
        right_point = (x + diameter * math.cos(math.radians(phi - 45)), y + diameter * math.sin(math.radians(phi - 45)))

        front_line = sp.LineString([car_position, front_point])
        left_line = sp.LineString([car_position, left_point])
        right_line = sp.LineString([car_position, right_point])
        print("X : %s , Y :%s" % (x, y))
        if isinstance(front_line.intersection(area_bound), sp.MultiPoint):
            front_distance = ((front_line.intersection(area_bound)[0].x - x) ** 2 + (
                    front_line.intersection(area_bound)[0].y - y) ** 2) ** (1 / 2)
            for i in range(0, len(front_line.intersection(area_bound)), 1):
                print(front_line.intersection(area_bound)[i])
                hold = ((front_line.intersection(area_bound)[i].x - x) ** 2 + (
                        front_line.intersection(area_bound)[i].y - y) ** 2) ** (1 / 2)
                if hold < front_distance:
                    front_distance = hold

        else:
            front_distance = ((front_line.intersection(area_bound).x - x) ** 2 + (
                    front_line.intersection(area_bound).y - y) ** 2) ** (1 / 2)

        if isinstance(left_line.intersection(area_bound), sp.MultiPoint):
            left_distance = ((left_line.intersection(area_bound)[0].x - x) ** 2 + (
                    left_line.intersection(area_bound)[0].y - y) ** 2) ** (1 / 2)
            for i in range(0, len(left_line.intersection(area_bound)), 1):
                hold = ((left_line.intersection(area_bound)[i].x - x) ** 2 + (
                        left_line.intersection(area_bound)[i].y - y) ** 2) ** (1 / 2)
                if hold < left_distance:
                    left_distance = hold

        else:
            left_distance = ((left_line.intersection(area_bound).x - x) ** 2 + (
                    left_line.intersection(area_bound).y - y) ** 2) ** (1 / 2)

        if isinstance(right_line.intersection(area_bound), sp.MultiPoint):
            right_distance = ((right_line.intersection(area_bound)[0].x - x) ** 2 + (
                    right_line.intersection(area_bound)[0].y - y) ** 2) ** (1 / 2)
            for i in range(0, len(right_line.intersection(area_bound)), 1):
                hold = ((right_line.intersection(area_bound)[i].x - x) ** 2 + (
                        right_line.intersection(area_bound)[i].y - y) ** 2) ** (1 / 2)
                if hold < right_distance:
                    right_distance = hold
        else:
            right_distance = ((right_line.intersection(area_bound).x - x) ** 2 + (
                    right_line.intersection(area_bound).y - y) ** 2) ** (1 / 2)

        return front_distance, left_distance, right_distance

    def bool_finish(self, final_left, final_right, final_car):
        # y=ax+b
        a = (final_left[1] - final_right[1]) / (final_left[0] - final_right[0])
        b = ((final_right[0] * final_left[1]) - (final_left[0] * final_right[1])) / ((final_right[0] - final_left[0]))
        f_y = a * final_car[0] + b
        # print("bool a=%s b=%s ans=%s now_y=%s"%(a,b,f_y,final_car[1]))
        if final_car[1] >= f_y:
            return True
        else:
            return False

    def get_phi(self):
        return self.phi

    def run(self):
        flag = False
        line = self.get_case_data()

        self.get_bound()

        area = sp.Polygon(self.bound)  # 範圍

        area_bound = sp.LineString(self.bound)  # 邊界

        diameter = self.get_max_diameter(self.bound)

        car_position = (self.default_x, self.default_y)
        car = sp.Point(car_position).buffer(3)  # 車子

        theta_t = self.default_theta
        phi_t = self.default_phi

        while True:

            if flag:
                print(self.bool_car_intersert_bound(car, area_bound))
                print(car.within(area))
                if self.bool_car_intersert_bound(car, area_bound) or not car.within(area):
                    break
            flag = True

            final_left = (self.final_left_x, self.final_left_y)
            final_right = (self.final_right_x, self.final_right_y)
            # final_line = sp.LineString([final_left, final_right])
            if car_position[0] >= self.final_left_x and car_position[0] <= self.final_right_x:
                if self.bool_finish(final_left, final_right, car_position):
                    break
            front_distance, left_distance, right_distance = self.get_direction_distance(car_position[0],
                                                                                        car_position[1], diameter,
                                                                                        phi_t,
                                                                                        area_bound)
            left_right_distance = left_distance - right_distance
            rule = gaussian()
            front_mem = {}
            print("f_s :%s %s f_m: %s %s f_l : %s %s " % (
            self.front_small_mean, self.front_small_sigma, self.front_medium_mean, self.front_medium_sigma,
            self.front_large_mean, self.front_large_sigma))
            front_mem[front_distance] = rule.get_front_distance_membership_function_value(front_distance,
                                                                                          self.front_small_mean,
                                                                                          self.front_small_sigma,
                                                                                          self.front_medium_mean,
                                                                                          self.front_medium_sigma,
                                                                                          self.front_large_mean,
                                                                                          self.front_large_sigma)
            left_right_mem = {}
            left_right_mem[left_right_distance] = rule.get_deviation_distance_membership_function_value(
                left_right_distance,
                self.deviation_small_mean, self.deviation_small_sigma,
                self.deviation_medium_mean, self.deviation_medium_sigma,
                self.deviation_large_mean, self.deviation_large_sigma)

            wheel_degree = rule.cal_wheel_membership_function_value(self.wheel_small_mean, self.wheel_small_sigma,
                                                                    self.wheel_medium_mean, self.wheel_medium_sigma,
                                                                    self.wheel_large_mean, self.wheel_large_sigma)

            result = {}
            for i in range(-40, 41, 1):
                result[i] = max(
                    min(front_mem[front_distance].small, left_right_mem[left_right_distance].small,
                        wheel_degree[i].large),
                    min(front_mem[front_distance].small, left_right_mem[left_right_distance].medium,
                        wheel_degree[i].large),
                    min(front_mem[front_distance].small, left_right_mem[left_right_distance].large,
                        wheel_degree[i].small),
                    min(front_mem[front_distance].medium, left_right_mem[left_right_distance].small,
                        wheel_degree[i].large),
                    min(front_mem[front_distance].medium, left_right_mem[left_right_distance].medium,
                        wheel_degree[i].medium),
                    min(front_mem[front_distance].medium, left_right_mem[left_right_distance].large,
                        wheel_degree[i].small),
                    min(front_mem[front_distance].large, left_right_mem[left_right_distance].small,
                        wheel_degree[i].large),
                    min(front_mem[front_distance].large, left_right_mem[left_right_distance].medium,
                        wheel_degree[i].medium),
                    min(front_mem[front_distance].large, left_right_mem[left_right_distance].large,
                        wheel_degree[i].small))

            up = 0
            down = 0
            for i in range(-40, 41, 1):
                up += i * result[i]
                down += result[i]
            if down != 0:
                theta_t = up / down
            if (theta_t > 40):
                theta_t = 40
            elif (theta_t < -40):
                theta_t = -40
            hold_4D = Train4D(front_distance, right_distance, left_distance, theta_t)
            hold_6D = Train6D(car_position[0], car_position[1], front_distance, right_distance, left_distance, theta_t)
            self.train4D.append(hold_4D)
            self.train6D.append(hold_6D)
            self.phi.append(phi_t)

            phi_t = phi(phi_t, theta_t)
            x = x_position(car_position[0], theta_t, phi_t)
            y = y_position(car_position[1], theta_t, phi_t)
            car_position = (x, y)
            car = sp.Point(car_position).buffer(3)

        self.write_Train4D_data()
        self.write_Train6D_data()
