# Mini-project 4 - Implementation of classic arcade game Pong
#
# Ernestas Poskus

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
score1 = 0
score2 = 0
currentWay = True  
paddle1_pos = float(HEIGHT / 2)
paddle2_pos = float(HEIGHT / 2)
paddle1_vel = float(0)
paddle2_vel = float(0)
pad_acc = 5        # accelerator value for paddles

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = float(HEIGHT / 2)
    paddle2_pos = float(HEIGHT / 2)
    paddle1_vel = float(0)
    paddle2_vel = float(0)
    currentWay = True
    ball_init(currentWay)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
      
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 3, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
 
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
        
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # draw scores
    c.draw_text(str(score1), [150,100], 45, "Lime")
    c.draw_text(str(score2), [450,100], 45, "Lime")
        

		
		
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS): # if hit left wall
        
        if (paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            # velocity incremented by 1/10
            ball_vel[0] += ball_vel[0] * 0.10
            ball_vel[1] += ball_vel[1] * 0.10
        else:
            score2 += 1
            currentWay = True
            ball_init(currentWay)
            
    if (ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS):  # if hit right wall

        if (paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            # velocity incremented by 1/10
            ball_vel[0] += ball_vel[0] * 0.10
            ball_vel[1] += ball_vel[1] * 0.10
        else:
            score1 += 1
            currentWay = False
            ball_init(currentWay)    

    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += pad_acc
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= pad_acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel += pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= pad_acc


def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right:
        ball_vel = [random.randrange(2, 4) , -(random.randrange(1, 3))]
    else:
        ball_vel = [ -(random.randrange(2, 4)) , -(random.randrange(1, 3))]

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,100)

# start frame
new_game()
frame.start()
