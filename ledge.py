import random_num

class platform:
    
    def __init__ (self):
        self.x_pos = random_num.platform_rand_x()
        self.y_pos = random_num.platform_rand_y()

    def x_range (self, start_range, end_range):
        self.x_pos = random_num.platform_controlled_x(start_range, end_range)
        self.y_pos = random_num.platform_rand_y

    def relational_y (self, prev_y):
        self.x_pos = random_num.platform_rand_x
        self.y_pos = random_num.platform_relational_y(prev_y)

    def x_range_relational_y (self, start_range, end_range, prev_y):
        self.x_pos = random_num.platform_controlled_x(start_range, end_range)
        self.y_pos = random_num.platform_relational_y(prev_y)