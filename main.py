import pygame

screen = pygame.display.set_mode([500, 500])

running = True
c = pygame.time.Clock()
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# SCREEN
	screen.fill((255, 255, 255))
	# FLIP
	c.tick(60)
	pygame.display.flip()