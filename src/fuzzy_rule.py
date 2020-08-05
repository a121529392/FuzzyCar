import math

class Wheel():
    def __init__(self, small_value,medium_value,large_value):
        self.small = small_value
        self.medium=medium_value
        self.large=large_value

class Front_Distance():
    def __init__(self, small_value,medium_value,large_value):
        self.small = small_value
        self.medium=medium_value
        self.large=large_value


class Deviation_left_right():
    def __init__(self, small_value,medium_value,large_value):
        self.small = small_value
        self.medium=medium_value
        self.large=large_value


class gaussian():

    def gaussian_function(self,x, mean, sigma):
        ans=math.exp(-(x - mean) ** 2 / sigma ** 2)
        return ans

    def incressing_gaussian_function(self,x, mean, sigma):
        if (x > mean):
            return 1
        else:
            ans = math.exp(-(x - mean) ** 2 / sigma ** 2)
            return ans

    def decreasing_gaussian_function(self,x, mean, sigma):
        if (x < mean):
            return 1
        else:
            ans = math.exp(-(x - mean) ** 2 / sigma ** 2)
            return ans

    def cal_wheel_membership_function_value(self,wheel_small_mean,wheel_small_sigma,
                                            wheel_medium_mean,wheel_medium_sigma,
                                            wheel_large_mean,wheel_large_sigma):
        wheel_degree={}
        for i in range(-40,41,1):
            s_v=self.decreasing_gaussian_function(i,wheel_small_mean,wheel_small_sigma)
            m_v = self.gaussian_function(i, wheel_medium_mean, wheel_medium_sigma)
            l_v = self.incressing_gaussian_function(i, wheel_large_mean, wheel_large_sigma)
            hold=Wheel(s_v,m_v,l_v)
            wheel_degree[i]=hold
        return wheel_degree

    def get_front_distance_membership_function_value(self,distance,
                                                     front_small_mean,front_small_sigma,
                                                     front_medium_mean,front_medium_sigma,
                                                     front_large_mean,front_large_sigma):
        s_v = self.decreasing_gaussian_function(distance, front_small_mean, front_small_sigma)
        m_v = self.gaussian_function(distance, front_medium_mean, front_medium_sigma)
        l_v = self.incressing_gaussian_function(distance, front_large_mean, front_large_sigma)
        return Front_Distance(s_v, m_v, l_v)

    def get_deviation_distance_membership_function_value(self,distance,
                                                         deviation_small_mean,deviation_small_sigma,
                                                         deviation_medium_mean,deviation_medium_sigma,
                                                         deviation_large_mean,deviation_large_sigma):
        s_v = self.decreasing_gaussian_function(distance, deviation_small_mean, deviation_small_sigma)
        m_v = self.gaussian_function(distance, deviation_medium_mean, deviation_medium_sigma)
        l_v = self.incressing_gaussian_function(distance, deviation_large_mean, deviation_large_sigma)
        return Deviation_left_right(s_v, m_v, l_v)


