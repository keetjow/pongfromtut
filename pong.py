import pygame, sys, random

def ballMovement():
	global ball_speed_x, ball_speed_y
	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= screen_width:
		ball.x = screen_width/2 - 15
		ball.y = screen_height/2 - 15
		ball_speed_x *= random.choice((1, -1))
		ball_speed_y *= random.choice((1, -1))
	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1
	ball.x += ball_speed_x
	ball.y += ball_speed_y

pygame.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10 ,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10 ,140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 10 * random.choice((1, -1))
ball_speed_y = 10 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				player_speed += 7
			if event.key == pygame.K_UP:
				player_speed -= 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				player_speed -= 7
			if event.key == pygame.K_UP:
				player_speed += 7
			

	player.y += player_speed

	er = ball.center[1] - opponent.midright[1]
	if er < 0:
		opponent.y -= opponent_speed
	if er > 0:
		opponent.y += opponent_speed
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height



	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height
	ballMovement()

	screen.fill(bg_color)
	pygame.draw.rect(screen, light_grey, player)
	pygame.draw.rect(screen, light_grey, opponent)
	pygame.draw.ellipse(screen, light_grey, ball)

	pygame.display.flip()
	clock.tick(60)