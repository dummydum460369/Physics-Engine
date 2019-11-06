class body:
    def __init__(self, list_id, pos_x, pos_y, vel_x, vel_y, acc_x, acc_y, mass=None, height=None, width=None,
                 radius=None,
                 obj_type='Dynamic'):
        self.mass = mass
        self.position = [pos_x, pos_y] if not radius else [pos_x - radius, pos_y - radius]
        self.velocity = [vel_x, vel_y]
        self.acceleration = [acc_x, acc_y]
        self.fps = 60
        self.width = width if width else radius
        self.height = height if height else radius
        self.position2 = [self.position[0] + self.width, self.position[1] + self.height]
        self.radius = radius
        self.id = list_id
        self.collided_x = False
        self.collided_y = True
        self.temp_acc_x = 0
        self.type = obj_type
        self.hit_x_list = []
        self.hit_y_list = []

    def correct_mass(self, bodies):
        if self.type == 'Static' and not self.mass:
            max = 0
            for obj in bodies:
                if obj.id == self.id or not obj.mass:
                    continue
                else:
                    if obj.mass >= max:
                        max = obj.mass * 10000000000000000
            self.mass = max

    def update_position(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position2 = [self.position[0] + self.width, self.position[1] + self.height]

    def check_collision(self, bodies=None):
        if bodies is None:
            bodies = []
        for obj in bodies:
            if obj.id == self.id:
                continue
            # x axis motion
            if (obj.position[1] < self.position[1] < obj.position2[1] or obj.position[1] < self.position2[1] <
                    obj.position2[1]) and obj not in self.hit_y_list:
                if obj.position[0] < self.position[0] + self.velocity[0] < obj.position2[0]:
                    if obj.type == 'Static':
                        self.position[0] = self.position[0] - (self.position[0] - obj.position2[0])
                        self.velocity[0] = (((self.mass - obj.mass) * self.velocity[0]) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity[0]) / (self.mass + obj.mass))
                        self.hit_x_list.append(obj)
                    elif obj.type == 'Dynamic':
                        self.position[0] = self.position[0] - (self.position[0] - obj.position[0])
                        self.velocity[0] = (((self.mass - obj.mass) * self.velocity) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity) / (self.mass + obj.mass))
                        obj.velocity[0] = ((2 * self.mass * self.velocity[0]) / (self.mass + obj.mass)) - (
                                ((self.mass - obj.mass) * obj.velocity[0]) / (self.mass + obj.mass))
                        self.hit_x_list.append(obj)
                elif obj.position[0] < self.position2[0] + self.velocity[0] < obj.position2[0]:
                    if obj.type == 'Static':
                        self.position[0] += obj.position[0] - self.position2[0]
                        self.velocity[0] = (((self.mass - obj.mass) * self.velocity[0]) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity[0]) / (self.mass + obj.mass))
                        self.hit_x_list.append(obj)
                    elif obj.type == 'Dynamic':
                        self.position[0] += obj.position[0] - self.position2[0]
                        self.velocity[0] = (((self.mass - obj.mass) * self.velocity[0]) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity[0]) / (self.mass + obj.mass))
                        obj.velocity[0] = ((2 * self.mass * self.velocity[0]) / (self.mass + obj.mass)) - (
                                ((self.mass - obj.mass) * obj.velocity[0]) / (self.mass + obj.mass))
                        self.hit_x_list.append(obj)

            if not ((obj.position[1] < self.position[1] < obj.position2[1] or obj.position[1] < self.position2[1] <
                     obj.position2[1]) and obj in self.hit_y_list):
                if obj in self.hit_x_list:
                    self.hit_x_list.remove(obj)
            if (obj.position[1] < self.position[1] < obj.position2[1] or obj.position[1] < self.position2[1] <
                    obj.position2[1]) and obj in self.hit_y_list:
                if not(obj.position[0] < self.position[0] + self.velocity[0] < obj.position2[0]):
                    self.hit_x_list.remove(obj)
                elif not(obj.position[0] < self.position2[0] + self.velocity[0] < obj.position2[0]):
                    self.hit_x_list.remove(obj)




                # if obj in self.hit_x_list and abs(self.position[0] - obj.position[0]) > self.width:
                #     self.hit_x_list.remove(obj)
                # if self in obj.hit_x_list and abs(self.position[0] - obj.position[0]) > self.width:
                #     obj.hit_x_list.remove(self)

            # if self.position[1] < obj.position[1] < self.position[1] + self.height or obj.position[1] < self.position[1] < obj.position[1] + obj.height:
            #     if obj.position[0] <= self.position[0] + self.width <= obj.position[0] + obj.width:
            #         print('hitx', obj.id)
            #         self.position[0] -= self.velocity[0] + 0.1
            #         self.velocity[0] = 0
            #
            #     elif obj.position[0] <= self.position[0] <= obj.position[0] + obj.width:
            #         print('hitx', obj.id)
            #         self.position[0] += self.velocity[0] +0.1
            #         self.velocity[0] = 0
            #     else:
            #         pass
            # # y axis motion
            if (obj.position[0] < self.position[0] < obj.position2[0] or obj.position[0] < self.position2[0] <
                    obj.position2[0]) and obj not in self.hit_x_list:
                if obj.position[1] < self.position[1] + self.velocity[1] < obj.position2[1]:
                    if obj.type == 'Static':
                        self.position[1] = self.position[1] - (self.position[1] - obj.position2[1])
                        self.velocity[1] = (((self.mass - obj.mass) * self.velocity[1]) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity[1]) / (self.mass + obj.mass))
                        self.hit_y_list.append(obj)
                    elif obj.type == 'Dynamic':
                        self.position[1] = self.position[1] - (self.position[1] - obj.position[1])
                        self.velocity[1] = (((self.mass - obj.mass) * self.velocity[1]) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity[1]) / (self.mass + obj.mass))
                        obj.velocity[1] = ((2 * self.mass * self.velocity[1]) / (self.mass + obj.mass)) - (
                                ((self.mass - obj.mass) * obj.velocity[1]) / (self.mass + obj.mass))
                        self.hit_y_list.append(obj)
                elif obj.position[1] < self.position2[1] + self.velocity[1] < obj.position2[1]:
                    if obj.type == 'Static':
                        self.position[1] += obj.position[1] - self.position2[1]
                        self.velocity[1] = (((self.mass - obj.mass) * self.velocity[1]) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity[1]) / (self.mass + obj.mass))
                        self.hit_y_list.append(obj)
                    elif obj.type == 'Dynamic':
                        self.position[1] += obj.position[1] - self.position2[1]
                        self.velocity[1] = (((self.mass - obj.mass) * self.velocity[1]) / (self.mass + obj.mass)) + (
                                (2 * obj.mass * obj.velocity[1]) / (self.mass + obj.mass))
                        obj.velocity[1] = ((2 * self.mass * self.velocity[1]) / (self.mass + obj.mass)) - (
                                ((self.mass - obj.mass) * obj.velocity[1]) / (self.mass + obj.mass))
                        self.hit_y_list.append(obj)
            if not ((obj.position[0] < self.position[0] < obj.position2[0] or obj.position[0] < self.position2[0] <
                    obj.position2[0]) and obj in self.hit_x_list):
                if obj in self.hit_y_list:
                    self.hit_y_list.remove(obj)
            if (obj.position[1] < self.position[1] < obj.position2[1] or obj.position[1] < self.position2[1] <
                    obj.position2[1]) and obj in self.hit_y_list:
                if not (obj.position[1] < self.position[1] + self.velocity[1] < obj.position2[1]):
                    self.hit_y_list.remove(obj)
                elif not (obj.position[1] < self.position2[1] + self.velocity[1] < obj.position2[1]):
                    self.hit_y_list.remove(obj)
                # else:
                #     if obj in self.hit_y_list and abs(self.position[1] - obj.position[1]) > self.height:
                #         self.hit_y_list.remove(obj)
                #     if self in obj.hit_y_list and abs(self.position[1] - obj.position[1]) > self.height:
                #         obj.hit_y_list.remove(self)

            # if self.position[0] < obj.position[0] < self.position[0] + self.width or obj.position[0] < self.position[1] < obj.position[1] + obj.height:
            #     if obj.position[1] <= self.position[1] + self.height <= obj.position[1] + obj.height:
            #         print('hity', obj.id)
            #         self.position[1] -= self.velocity[1]
            #         self.velocity[1] = 0
            #     elif obj.position[1] <= self.position[1] <= obj.position[1] + obj.height:
            #         print('hity', obj.id)
            #         self.position[1] += self.velocity[1]
            #         self.velocity[1] = 0
            #     else:
            #         pass

    def update(self, objects=None):
        if objects is None:
            objects = []
        self.check_collision(objects)
        self.update_position()
        self.check_collision(objects)
