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
            self.pos.left = width - 30
        if self.pos.right > width:
            self.pos.right = 30
        if self.pos.top < 0:
            self.pos.top = height - 30
        if self.pos.bottom > height:
            self.pos.bottom = 30 #hyperbolic
        screen.blit(self.image, self.pos)


size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = pygame.image.load("Code\Asteroid clone\Assets\Borneswore_PlayerMk1.png").convert()
playerRect = player.get_rect()
startPos = [265,255]
posSet = playerRect = playerRect.move(startPos)
screen.blit(player, posSet)
momenThrow = [0,0]
momenCharge = [True,True,True]
keysTimer = 0
momenChargeTimer = 0
chargeFig3 = pygame.image.load("Code\Asteroid clone\Assets\chargeFull1Mk2.png").convert()
chargeFig2 = pygame.image.load("Code\Asteroid clone\Assets\chargePoint2Mk2.png").convert()
chargeFig1 = pygame.image.load("Code\Asteroid clone\Assets\chargePoint3Mk2.png").convert()
chargeFig0 = pygame.image.load("Code\Asteroid clone\Assets\chargeEmptyMk2.png").convert()
chargeFig3Rect = chargeFig3.get_rect()
chargeFig2Rect = chargeFig2.get_rect()
chargeFig1Rect = chargeFig1.get_rect()
chargeFig0Rect = chargeFig0.get_rect()
chargeFig = [chargeFig0, chargeFig1, chargeFig2, chargeFig3]
chargeRect = [chargeFig0Rect, chargeFig1Rect, chargeFig2Rect, chargeFig3Rect]
chargeStartPos = [0,448] #left off here

playerProjection = pygame.image.load("Code\Asteroid clone\Assets\Borneswore_Projectile1.png").convert()
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
    momenChargeTimer += clock.get_time() 
    if momenChargeTimer >= 2500 and momenCharge != [True,True,True]:
        momenChargeTimer = 0
    if momenChargeTimer == 0 and momenCharge != [True,True,True]:
        momenCharge.append(True)
    
    screen.fill((0,0,0))
    if momenCharge == [True,True,True]: #Charge GUI
        screen.blit(chargeFig3, chargeStartPos)
    if momenCharge == [True,True]:
        screen.blit(chargeFig2, chargeStartPos)
    if momenCharge == [True]:
        screen.blit(chargeFig1, chargeStartPos)
    if momenCharge == []:
        screen.blit(chargeFig0, chargeStartPos) #Charge GUI
    screen.blit(player,playerRect)
    playerKeys = pygame.key.get_pressed() # --- player movement ---
    playerRect = playerRect.move(momenThrow)
    if playerKeys[pygame.K_RIGHT] and momenCharge != [] and keysTimer == 0: 
        momenThrow[0] += 1
        screen.blit(player,playerRect)
        momenCharge.pop()
        o = moveShot(playerProjection, [-1,0], [playerRect.left, playerRect.top])
        oR.append(o)
    for o in oR:
        o.moveOb()
    if playerKeys[pygame.K_LEFT] and momenCharge != [] and keysTimer == 0:
        momenThrow[0] -=1
        screen.blit(player,playerRect)
        momenCharge.pop()
        o = moveShot(playerProjection, [1,0], [playerRect.left+60, playerRect.top])
        oL.append(o)
    for o in oL:
        o.moveOb()
    if playerKeys[pygame.K_DOWN] and momenCharge != [] and keysTimer == 0:
        momenThrow[1] += 1
        screen.blit(player,playerRect)
        momenCharge.pop()
        o = moveShot(playerProjection, [0,-1], [playerRect.left, playerRect.top])
        oD.append(o)
    for o in oD:
        o.moveOb()
    if playerKeys[pygame.K_UP] and momenCharge != [] and keysTimer == 0:
        momenThrow[1] -= 1
        screen.blit(player,playerRect)
        momenCharge.pop() # --- player movement ---
        o = moveShot(playerProjection, [0,1], [playerRect.left, playerRect.top+60])
        oU.append(o)
    for o in oU:
        o.moveOb()
    if playerRect.left < 0: #hyperbolic
            playerRect.left = width - 70
    if playerRect.right > width:
            playerRect.right = 70
    if playerRect.top < 0:
            playerRect.top = height - 70
    if playerRect.bottom > height:
            playerRect.bottom = 70 #hyperbolic

    clock.tick(30)
    pygame.display.update()

    '''
    Ideas:
    - Have projectiles collide with each other
    - make the charge GUI smaller and a part of the hyperbolic plane
    - Target system
    - Targets have a random set of health
    - targets gain momentum from projectiles
    - player has one life
    - score
    - start screen
    - game over screen
    - targets get increasingly cracked per hit
    '''
