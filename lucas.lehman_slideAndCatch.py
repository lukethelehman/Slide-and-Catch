import pygame, simpleGE, random




class Cat(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cat.png")
        self.setSize(150, 150)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
        

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
        self.sndMeow = simpleGE.Sound("meow.wav")
        self.basket = Basket(self)
        self.cat = Cat(self)
        
        self.sprites = [self.basket,
                        self.cat]
        
    def process(self):
        if self.cat.collidesWith(self.basket):
            self.cat.reset()
            self.sndMeow.play()
            
        
        
        
def main():
    game = Game()
    game.start()




if __name__ == "__main__":
    main()

