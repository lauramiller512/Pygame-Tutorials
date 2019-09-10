import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Tower Defense")

isJump = False
jumpCount = 10

x = 40
y = 40
width = 40
height = 60
vel = 10 #movement speed of the character

run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #recognizes when player closes the window
			run = False


	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 0:
		x -= vel

	if keys[pygame.K_RIGHT] and x < 560: #stops the char from running past the width of the screen minus the width of our char (600-40)
		x += vel	

	if not(isJump):
		if keys[pygame.K_UP] and y > 0:
			y -= vel

		if keys[pygame.K_DOWN] and y < 540:
			y += vel

		if keys[pygame.K_SPACE]:
			isJump = True

	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y  -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10

	grey = (128, 128, 128)
	screen.fill(grey)  #change background color
	pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
	pygame.display.update() #refreshes the screen so the char remains a rectangle

pygame.quit()
