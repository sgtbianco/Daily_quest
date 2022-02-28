#!python


def give_task(day):
    user.vars.set("daily_active", True, timedelta(days=1))
    if day == 1:
        user.say("For today's task, I'd like you to fetch a rare mushroom that only grows in Johto's forests. Once you've found it, please bring it to me.")
        user.say("You'll be given 24 hours to complete this task. Do not disappoint me.")
    elif day == 2:
        user.say("Today, I want you to catch a specific Pokemon for me. That way, Team Rocket can get one step closer to world domination... thanks to you!")
        user.say(f"The Pokemon I need you to catch is a {Pokemon.name}. Once you've caught it, please bring it to me.")
        user.say("As usual, you have 24 hours to complete this task. Do not disappoint me.")
    else:
        user.say("Today's task is a bit different. We're going to have you recruit a new member. I was told by our spies that there's a potential candidate in {map name}")    



if not user.vars.tro_innit:
    choice1 = user.select("Ah, there you are! I've been waiting for you. You're the new Team Rocket recruit, right?",
                            "Yes...? (Lets see where this goes.)", "Huh?")
    if choice1[0] == 0:
        user.vars.tro_innit == True
        user.vars.tro_progress = 1
        user.vars.tro_consec_days = 0
        user.vars.daily_active = False
        user.vars.daily_completed = False
        user.vars.which_task = 1
        user.say("Perfect! We have a lot to discuss. I must say that my expectations are already high.")
        user.say("The Team Rocket scout I spoke with favorably recommended you after seeing your prowess in battle.")
        user.say("You're now officially on trial to become a Team Rocket grunt. We'll have you run some errands to prove your worth to us.")
        user.say("I suspect this won't be troublesome for a skilled individual such as yourself, but this is part of the protocol to join our prestigious organization")
        user.say("If you successfully complete your assigned tasks for a whole week, you'll become one of us.")
        user.say("Of course, no labor is free, so I'll make sure to reward you every time.")
        user.say("Eventually, you can even receive better rewards as you acquire more experience.")

    else:
        user.say("Oh... Move along, kid, and forget whatever you just heard... or else.")


if user.vars.tro_progress == 1:
    choice2 = ("Without further ado, shall we begin?", "Yes!", "No, I need more time to prepare.")
    if choice2[0] == 0:
        user.vars.tro_progress = 2
        give_task(user.vars.which_task)
        #user.vars.set("daily_active", True, timedelta(days=1))
    else:
        user.say("Very well. Come back when you're ready, but don't take too long or someone else might take your spot.")
    
elif user.vars.tro_progress == 2 and user.vars.daily_active and not user.vars.daily_completed:
    user.say("I see you're still twiddling your thumbs while time is ticking down. You must complete your assign task within {user.expire.daily_active}.")