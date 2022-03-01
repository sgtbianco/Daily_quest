#!python

import random

#set quest vars and maybe which_task
def give_task():
    user.vars.set("daily_active", True, timedelta(days=1))
    if user.vars.which_task == 1:
        user.say("For today's task, I'd like you to fetch a rare mushroom that only grows in Johto's forests. Once you've found it, please bring it to me.")
        user.say("You'll be given 24 hours to complete this task. Do not disappoint me.")
    elif user.vars.which_task == 2:
        pokemon_list = ["Yamask", "Woobat", "Frillish", "Skorupi", "Inkay"]
        user.vars.tro_pokemon = random.choice(pokemon_list)
        user.say("Today, I want you to catch a specific Pokemon for me. That way, Team Rocket can get one step closer to world domination... thanks to you!")
        user.say(f"The Pokemon I need you to catch is a {user.vars.tro_pokemon}. Once you've caught it, please bring it to me.")
        user.say("As usual, you have 24 hours to complete this task. Do not disappoint me.")
    else:
        user.say("Today's task is a bit different. We're going to have you recruit a new member. I was told by our spies that there's a potential candidate in {map name}")
        user.say("You might need to be extra convincing, though... if you know what I mean.")

def give_reward():
    pass





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
    if not user.vars.daily_active:
        choice2 = ("Shall we begin today's task?", "Yes!", "No, I need more time to prepare.")
        if choice2[0] == 0:
            user.vars.tro_progress = 2
            give_task()
        else:
            user.say("Very well. Come back when you're ready, but don't take too long or someone else might take your spot.")
    else:
        user.say(f"Come back in {user.expire.daily_active}.")

elif user.vars.tro_progress == 2 and user.vars.daily_active and not user.vars.daily_completed:
    if user.vars.which_task == 2:
        p = user.select_pokemon("Show me the Pokemon the Pokemon that you were supposed to catch.")
        # this does not check if freshly caught
        if p.name == user.vars.tro_pokemon:
            user.vars.tro_consec_days += 1
            user.vars.tro_progress = 1
            give_reward()
        else:
            user.say("That is not the Pokemon I asked for.")
    else:
        user.say("I see you're still twiddling your thumbs while time is ticking down. You must complete your assigned task within {user.expire.daily_active}.")

elif user.vars.tro_progress == 2 and not user.vars.daily_active and not user.vars.daily_completed:
    user.say("I'm disappointed. I expected better from you, but you did not deliver. However, you still show a lot of promise and I have a new task for you.")
    user.say("Do not disappoint me again.")
    # change which_task?
    give_task(user.vars.which_task)

elif user.vars.tro_progress == 2 and not user.vars.daily_active and user.vars.daily_completed:
    user.say("I've been expecting you. Were you able to fulfill the task that was given to you?")



    user.vars.tro_consec_days += 1
    give_reward(user.vars.tro_consec_days)
    # change which_task?