import pygame, simpleGE, random




class Cat(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cat.png")
        self.setSize(125, 125)
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
        self.moveSpeed = 10 
        
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -=self.moveSpeed
            
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x +=self.moveSpeed
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("tree.png")
        self.sndMeow = simpleGE.Sound("meow.wav")
        self.numCats = 3
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
        self.lblScore = LblScore()
        self.basket = Basket(self)
        self.cats = []
        for i in range(self.numCats):
            self.cats.append(Cat(self))
        
        self.sprites = [self.basket,
                        self.cats,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for cat in self.cats:
            
            if cat.collidesWith(self.basket):
                cat.reset()
                self.sndMeow.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
            
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
                
            
        
        
        
def main():
    game = Game()
    game.start()




if __name__ == "__main__":
    main()

