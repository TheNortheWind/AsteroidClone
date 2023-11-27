import sys, pygame
pygame.init()

class moveShot: # working on
    def __init__(self, image, speed, startPos):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()
        self.startPos = startPos
        posSet = self.pos = self.pos.move(self.startPos)
        screen.blit(self.image, posSet)
    def moveOb(self):
        self.pos = self.pos.move(self.speed)
        if self.pos.left < 0: #hyperbolic
            self.pos.left = width - 50
        if self.pos.right > width:
            self.pos.right = 50
        if self.pos.top < 0:
            self.pos.top = height - 30
        if self.pos.bottom > height:
            self.pos.bottom = 30 #hyperbolic
        screen.blit(self.image, self.pos)


size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = pygame.image.load("Code\Asteroid clone\greenrect30x50(AssetTestAsteroid).png").convert()
playerRect = player.get_rect()
momenThrow = [0,0]
momenCharge = [True,True,True]
keysTimer = 0
momenChargeTimer = 0

oR = []
oL = []
oD = []
oU = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keysTimer += clock.get_time()
    if keysTimer >= 200: 
        keysTimer = 0
    momenChargeTimer += clock.get_time() # working on
    if momenChargeTimer >= 2500 and momenCharge != [True,True,True]:
        momenChargeTimer = 0
    if momenChargeTimer == 0 and momenCharge != [True,True,True]:
        momenCharge.append(True)
    
    screen.fill((0,0,0))
    screen.blit(player,playerRect)
    playerKeys = pygame.key.get_pressed() # --- player movement ---
    playerRect = playerRect.move(momenThrow)
    if playerKeys[pygame.K_RIGHT] and momenCharge != [] and keysTimer == 0: # working on
        momenThrow[0] += 1
        screen.blit(player,playerRect)
        momenCharge.pop()
        o = moveShot(player, [-1,0], [playerRect.left-50, playerRect.top])
        oR.append(o)
    for o in oR:
        o.moveOb()
    if playerKeys[pygame.K_LEFT] and momenCharge != [] and keysTimer == 0:
        momenThrow[0] -=1
        screen.blit(player,playerRect)
        momenCharge.pop()
        o = moveShot(player, [1,0], [playerRect.left+50, playerRect.top])
        oL.append(o)
    for o in oL:
        o.moveOb()
    if playerKeys[pygame.K_DOWN] and momenCharge != [] and keysTimer == 0:
        momenThrow[1] += 1
        screen.blit(player,playerRect)
        momenCharge.pop()
        o = moveShot(player, [0,-1], [playerRect.left, playerRect.top-30])
        oD.append(o)
    for o in oD:
        o.moveOb()
    if playerKeys[pygame.K_UP] and momenCharge != [] and keysTimer == 0:
        momenThrow[1] -= 1
        screen.blit(player,playerRect)
        momenCharge.pop() # --- player movement ---
        o = moveShot(player, [0,1], [playerRect.left, playerRect.top+30])
        oU.append(o)
    for o in oU:
        o.moveOb()
    if playerRect.left < 0: #hyperbolic
            playerRect.left = width - 50
    if playerRect.right > width:
            playerRect.right = 50
    if playerRect.top < 0:
            playerRect.top = height - 30
    if playerRect.bottom > height:
            playerRect.bottom = 30 #hyperbolic

    clock.tick(30)
    pygame.display.update()
