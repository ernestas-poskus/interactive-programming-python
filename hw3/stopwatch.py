# Mini-project 3 - "Stopwatch: The Game"
#
# Ernestas Poskus

# importing
import simplegui


# define global variables
time = 0
stopwatch = "0:00.0"
score = "0/0"
running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #Format Milis
    millisec = str(t)   
    aux = len(millisec)
    millisec = millisec[aux-1]
    
    #Format Seconds
    sec = int((t / 10) % 60);
    if len(str(sec))<2:
        sec = "0" + str(sec)
    else:
        sec = str(sec)
    
    #Format Minutes
    min = int(((t / (10*60)) % 60));
    if len(str(min))>1:
        min = str(min)
        aux = len(min)
        min = min[aux-1]
    else:
        min = str(min)
    
    return min+":"+sec+"."+millisec	
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    if running != True:
        timer.start()
        running = True

def stop():
    global running
    if running == True:
        timer.stop()
        global stopwatch
        intent = stopwatch[len(stopwatch)-1]
        if intent=="0":
            update(True)
        else:
            update(False)
        running = False
    
def reset():
    global running
    global time
    global score
    if running == True:
        timer.stop()
        running = False
    time = -1
    score = "0/0"
    tick()

# helpers
def update(intent):
    global score
    slash = score.find("/")
    success = int(score[:slash])
    attempts = int(score[slash+1:])
    if intent == True:
        success +=1
    attempts +=1
    score = str(success) + "/" + str(attempts)	
	
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    global stopwatch
    time +=1
    stopwatch = format(time)

# define draw handler
def clock(canvas):
    canvas.draw_text(stopwatch, [75,118], 36, "White")
    canvas.draw_text(score, [250,24], 12, "Lime")
    
# create frame
f = simplegui.create_frame("StopWatch", 300, 200,100)
f.set_canvas_background("Black")
button1 = f.add_button("Start", start, 100)
button2 = f.add_button("Stop", stop, 100)
button3 = f.add_button("Reset", reset, 100)
timer = simplegui.create_timer(500, tick)

# register event handlers
f.set_draw_handler(clock)

# start frame
f.start()

# Please remember to review the grading rubric
