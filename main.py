import turtle as turtle_module
import random
# import colorgram
#
# colors = colorgram.extract('Image.jpg', 30)
#
# colours = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colours.append(new_color)
#
# print(colours)
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(9, 56, 73), (133, 162, 179), (51, 105, 124), (7, 89, 106), (174, 160, 138), (106, 98, 80), (230, 220, 198),
       (76, 105, 98), (48, 46, 37), (145, 165, 156), (37, 50, 46), (18, 95, 90), (209, 197, 161), (143, 134, 100),
       (70, 70, 47), (84, 143, 159), (202, 212, 205), (100, 143, 131), (104, 86, 91), (193, 99, 83), (48, 39, 42),
       (187, 205, 210), (177, 200, 189), (160, 146, 152), (172, 199, 204), (55, 63, 74), (89, 52, 47), (87, 51, 56),
       (185, 96, 106), (120, 127, 138)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(360)
tim.setheading(0)
tim.speed("fastest")

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
