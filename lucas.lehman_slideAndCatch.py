import pygame, simpleGE, random



class Basket(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("basket.png")
        self.setSize(120,100)
        self.position = (140, 430)
        self.moveSpeed = 5 
        
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -=self.moveSpeed
            
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x +=self.moveSpeed

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("tree.png")
        self.basket = Basket(self)
        
        self.sprites = [self.basket]
        
        
        
def main():
    game = Game()
    game.start()




if __name__ == "__main__":
    main()

