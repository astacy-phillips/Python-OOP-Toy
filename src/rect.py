class Rect:
    def __init__(self, bounds, color, rect):
        self.bounds = bounds
        self.rect = rect
        self.color = color

    def update(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rect)
