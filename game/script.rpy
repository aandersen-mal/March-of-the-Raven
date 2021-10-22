# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#https://www.renpy.org/doc/html/side_image.html

define e = Character("Eileen")
define g = Character("Gwen", window_left_padding=150, image="gwen")
define c = Character("Clyde")

image side gwen neutral = im.FactorScale("gwen neutral.png", 0.5,0.5)
image side gwen sad = im.FactorScale("gwen sad.png", 0.5,0.5)


# The game starts here.

label start:

    jump startintro



    return
