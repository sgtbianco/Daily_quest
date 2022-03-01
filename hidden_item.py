#!python

if user.vars.which_task == 1 and user.vars.daily_active and not user.vars.daily_completed:
    user.vars.daily_completed = True
    user.say("Oh! Is this the rare mushroom I was asked to find?")
    user.say("You received a rare mushroom.")
    user.say("I better hurry up and return it to the Team Rocket Officer.")