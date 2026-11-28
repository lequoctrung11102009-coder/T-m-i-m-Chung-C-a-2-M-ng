balls = ["b", "r", "b", "w", "w", "r"]
red = 0
white = 0
blue = 0

for i in range(len(balls)):
    if balls[i] == "r":
        red += 1
    elif balls[i] == "w":
        white += 1
    elif balls[i] == "b":
        blue += 1
new_balls = []
for i in range(red):
    new_balls.append("r")
for i in range(white):
    new_balls.append("w")
for i in range(blue):
    new_balls.append("b")
print(new_balls)