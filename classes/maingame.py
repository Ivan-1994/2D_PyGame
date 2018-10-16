class MainGame:
    def __init__(self, pygame):
        self.new_x = 0
        self.new_y = 0
        self.img_x = 5
        self.img_y = 5
        self.bool_pos = False
        self.pygame = pygame

    def events_game(self, event):
        if event.type == self.pygame.QUIT:
            return False

        if event.type == self.pygame.KEYDOWN:
            if event.key == self.pygame.K_ESCAPE:
                print('111')
                return False

        if event.type == self.pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.new_x = event.pos[0]
                self.new_y = event.pos[1]
                self.bool_pos = True

        return True

    def bool_position_x(self):
        if self.new_x == self.img_x:
            return False
        return True

    def bool_position_y(self):
        if self.new_y == self.img_y:
            return False
        return True

    def next_position(self):
        if self.bool_position_x() and self.new_x > self.img_x:
            self.img_x += 1
        if self.bool_position_x() and self.new_x < self.img_x:
            self.img_x -= 1

        if self.bool_position_y() and self.new_y > self.img_y:
            self.img_y += 1
        if self.bool_position_y() and self.new_y < self.img_y:
            self.img_y -= 1

        if not self.bool_position_x() and not self.bool_position_y():
            self.bool_pos = False


"""  
    Если передвигается на 20пх
    x: 100 < 86 < 80
    y: 80 < 71 < 60
    
    71-60=11
    80-71=9
    
"""