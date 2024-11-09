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
        self.moveSpeed = 75
        
        
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
            
class Instructions(simpleGE.Scene):
    def __init__(self, lastScore):
        super().__init__()
        self.setImage("tree.png")
        self.response = "Quit"
        self.prevScore = lastScore
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "You are controlling a basket",
            "Move with left and right arrow keys.",
            "Catch as many cats as you can",
            "in the time provided",
            "",
            "Good luck!"]
        self.directions.center = (320,240)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100,400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (530,400)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (320, 400)
        self.lblScore.text = f"Last score: {self.prevScore}"
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
        

        
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
            
    
                
            
        
        
        
def main():
    
    keepGoing = True
    lastScore = 0
    while keepGoing:
        
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
        
        else:
            keepGoing = False
        
    
    
    





if __name__ == "__main__":
    main()

