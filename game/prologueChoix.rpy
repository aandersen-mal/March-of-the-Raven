#Debut du jeu ou le joueur customize Gwen

label startPrologue :

    #Steph stp ajoute un place holder d'image

    "You were born on an auspicious day young Ravenbride"
    "At only one day old, your parents didn't have the contempt they had for you now"
    "After a lot of deliberation they came up with your name"
    $ mcname = renpy.input("What is your name?", length=32, default="Gwen")
    $ mcname = mcname.strip()

    if not mcname:
        $ mcname = "Gwen"

    "The servants were overjoyed at the birth of a new heir to the Duchy, and they insisted to call you by your title."
    "Which was...."
    menu:
        "My Liege":
            pass
        "My Lord":
            $ title = "My Lord"
            $ HerHis = "He"
            $ herhis = "he"
            $ Their = "His"
            $ their = "his"
            $ Them = "Himself"
            $ them = "himself"
        "My Lady":
            $ title = "My Lady"
            $ HerHis = "She"
            $ herhis = "she"
            $ Their = "Her"
            $ their = "her"
            $ Them = "Herself"
            $ them = "herself"

    "Yes, it was a very proper household."
    "As time went on, your family allowed people from outside the duchy to see you. You earned yourself a lot of praise during that time."
    "What was it about?"
    menu :
        "Your cuteness":
            $beauty += 5

        "The intelligent glint in your eyes":
            $intelligence +=5

        "The fact you never cried, no matter who held you":
            $etiquette +=5

        "How everyone left with a smile after seeing you":
            $popularity +=5

    "As you grew up, you impressed your parents by the fact that..."
    menu:
        "You learned to walk at the impressive age of 8 months":
            $combat +=5

        "You knew exactly who to charm to obtain the best sweets":
            $cunning +=5

        "You learned how to talk at the impressive age of 8 months":
            $charisma += 5

        "You quickly managed to mold the water into shapes during your bath time":
            $magic +=5

    "You were really a talented kid. Everyone could see that"
    "As you grew up, you had to attend a lot of balls and official gathering alonside your parents"
    "How did that made you feel?"

    menu:
        "Excited. You were constantly pestering your mother to know when the next outing was":
            $jaugeIntroExtro += 15

        "Bored. You knew there was nothing you could do to escape these public functions, and they were clearly made for the adults":
            pass

        "Anxious. You knew you had an important role in the nobility, and you couldn't help but feel that every eyes was on you, waiting to make a mistake":
            $jaugeIntroExtro -= 15

    "Social season was soon over, leaving you with a wide array of classes."
    "What was your favorite?"
    menu :
        "Magic class" :
            $magic += 5
        "Etiquette class":
            $etiquette += 5
        "Combat class":
            $combat += 5
        "General Studies":
            $intelligence += 5
        "Politics studies":
            $cunning += 5
        "Debate class":
            $charisma += 5
        "You prefered to play with the children of the staff":
            $popularity += 5
            $jaugeIntroExtro += 5
        "You prefered to go shopping with your maid":
            $beauty += 5
        "You prefered to read quietly in your room":
            $intelligence += 5
            $jaugeIntroExtro -= 5

    "Everything was smooth sailing for you...until you discovered your unique ability."
    "It started innocently enough, you saw a red flag waving on your favorite maid head."
    "Of course, you had to touch it, making it disappear. Everything seemed well again, until you went to bed"
    "In your dream, you saw your maid falling down the stairs, pushed by her ex lover who also worked for the duchy"
    "You woke up in sweats. Just in time to hear a small commotion near your bedroom."
    "It was the scene you just witnessed ! And from the look of it, you had seconds to react before your favorite maid was no more"
    "You...."

    menu :

        "Yelled as loud as you could to alert the guards and hopefully prevent the murder":
            $jaugeIntroExtro += 5
            "Fortunately, the ex lover was distracted by your sudden appearance, allowing the maid to free herself"
            "It also alerted the guards on duty, and the culprit was quickly apprehended."
            "Your quick actions saved your maid ! congratulations !"
            $savedMaid = 1

        "Used your magic to push the ex lover away from your maid":
            if magic >= 5:
                "A small gust of wind quickly picked up, pushing and surprising the ex lover."
                "The maid quickly freed herself and called for the guards."
                "Your quick actions saved your maid ! congratulations !"
                $savedMaid = 1
            else:
                "You tried to summon a small gust of wind, but your reserves were to small to make a difference."
                "As you saw in your dream, your maid was pushed down the stairs, and the ex lover quickly flew the scene."
                "It Left you with some pretty traumatic memories"
                $savedMaid = 0

        "Rushed to take on the ex lover yourself":
            if combat = 10:
                "Sure you were young, but you were also praised to be a genius when it came to hand to hand combat."
                "You managed to make the ex lover stumble, allowing the maid to free herself and call for the guards."
                "Your quick actions saved your maid ! congratulations !"
                $savedMaid = 1
            else :
                "You weren't fast enough to reach the duo."
                "As you saw in your dream, your maid was pushed down the stairs, and the ex lover quickly flew the scene."
                "It Left you with some pretty traumatic memories"
                $savedMaid = 0
jump introlucy
