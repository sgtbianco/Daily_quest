#!python

import random

# this daily doesnt consider days that pass between 2 completed quests i think


def give_task():
    user.vars.set("daily_active", True, timedelta(days=1))
    if user.vars.which_task == 1:
        user.say("Team Rocket Officer: For today's task, I'd like you to fetch a rare mushroom that only grows in Johto's forests. Once you've found it, please bring it to me.")
        user.say("Team Rocket Officer: You'll be given 24 hours to complete this task. Do not disappoint me.")
    elif user.vars.which_task == 2:
        pokemon_list = ["Yamask", "Woobat", "Frillish", "Skorupi", "Inkay"]
        user.vars.tro_pokemon = random.choice(pokemon_list)
        user.say("Team Rocket Officer: Today, I want you to catch a specific Pokemon for me. That way, Team Rocket can get one step closer to world domination... thanks to you!")
        user.say(f"Team Rocket Officer: The Pokemon I need you to catch is a {user.vars.tro_pokemon}. Once you've caught it, please bring it to me.")
        user.say("Team Rocket Officer: As usual, you have 24 hours to complete this task. Do not disappoint me.")
    else:
        user.say("Team Rocket Officer: Today's task is a bit different. We're going to have you recruit a new member. I was told by our spies that there's a potential candidate in {map name}.")
        user.say("Team Rocket Officer: You might need to be extra convincing, though... if you know what I mean.")


def give_reward():
    money_reward = 5000 * user.vars.tro_rank
    user.money += money_reward
    user.say(f"You received {money_reward} Pokedollars!")
    if user.vars.which_task == 1:
        item_reward = 3 * user.vars.tro_rank
        user.items["PP Up"] += item_reward
        user.say(f"You reveived {item_reward}x PP Up!")

    elif user.vars.which_task == 2:
        item_reward = 3 * user.vars.tro_rank
        user.items["Max Repel"] += item_reward
        user.say(f"You reveived {item_reward}x Max Repel!")

    else:
        item_reward = 3 * user.vars.tro_rank
        user.items["Rare Candy"] += item_reward
        user.say(f"You reveived {item_reward}x Rare Candy!")

    if user.tro_consec_days % 7 == 0 and user.vars.tro_rank == 1:
        user.say("Team Rocket Officer: It seems that you completed all 7 tasks that you've been assigned.")
        user.say("Team Rocket Officer: Congrats kid! You're officially a part of Team Rocket. Your new rank is 'Team Rocket Grunt.'")
        user.say("Team Rocket Officer: To celebate, I'll even give you a bonus.")
        user.items["Master Ball"] += 1
        user.say("You received a Master Ball.")
        user.say("Team Rocket Officer: From now on, you'll receive greater rewards for completing assigned daily tasks.")
        user.say("Team Rocket Officer: Now get out of here! I have important matters to take care of.")
        user.vars.tro_rank = 2
    elif user.tro_consec_days % 28 == 0:
        user.say("Team Rocket Officer: Wow! you completed a whole months worth of tasks without fail.")
        user.say("Team Rocket Officer: Here is a special reward for all of your hard work.")
        user.items["Reroll Ticket"] += 1
        user.say("You received a Reroll Ticket.")
    elif user.tro_consec_days % 7 == 0:
        user.say("Team Rocket Officer: It seems that you completed all 7 taks that you've been assigned.")
        user.say("Team Rocket Officer: As a bonus reward, take this.")
        user.items["Master Ball"] += 1
        user.say("You received a Master Ball.")



def next_task():
    if user.vars.which_task == 1:
        user.vars.which_task = 2

    elif user.vars.which_task == 2:
        user.vars.which_task = 3
    else:
        user.vars.which_task = 1



if not user.vars.tro_innit:
    choice1 = user.select("Team Rocket Officer: Ah, there you are! I've been waiting for you. You're the new Team Rocket recruit, right?",
                            "Yes...? (Lets see where this goes.)", "Huh?")
    if choice1[0] == 0:
        user.vars.tro_innit == True
        user.vars.tro_progress = 1
        user.vars.tro_consec_days = 0
        user.vars.daily_active = False
        user.vars.daily_completed = False
        user.vars.which_task = 1
        user.vars.tro_rank = 1
        user.say("Team Rocket Officer: Perfect! We have a lot to discuss. I must say that my expectations are already high.")
        user.say("Team Rocket Officer: The Team Rocket scout I spoke with favorably recommended you after seeing your prowess in battle.")
        user.say("Team Rocket Officer: You're now officially on trial to become a Team Rocket grunt. We'll have you run some errands to prove your worth to us.")
        user.say("Team Rocket Officer: I suspect this won't be troublesome for a skilled individual such as yourself, but this is part of the protocol to join our prestigious organization.")
        user.say("Team Rocket Officer: If you successfully complete your assigned tasks for a whole week, you'll become one of us.")
        user.say("Team Rocket Officer: Of course, no labor is free, so I'll make sure to reward you every time.")
        user.say("Team Rocket Officer: Eventually, you can even receive better rewards as you acquire more experience.")

    else:
        user.say("Team Rocket Officer: Oh... Move along, kid, and forget whatever you just heard... or else.")


if user.vars.tro_progress == 1:
    if not user.vars.daily_active:
        choice2 = ("Team Rocket Officer: Shall we begin today's task?", "Yes!", "No, I need more time to prepare.")
        if choice2[0] == 0:
            user.vars.tro_progress = 2
            give_task()
        else:
            user.say("Team Rocket Officer: Very well. Come back when you're ready, but don't take too long or someone else might take your spot.")
    else:
        user.say(f"Team Rocket Officer: Come back in {user.expire.daily_active} for your next task.")

elif user.vars.tro_progress == 2 and user.vars.daily_active and not user.vars.daily_completed:
    if user.vars.which_task == 2:
        p = user.select_pokemon("Team Rocket Officer: Show me the Pokemon the Pokemon that you were supposed to catch.")
        # this does not check if freshly caught
        if p.name == user.vars.tro_pokemon:
            user.say("Team Rocket Officer: Very good! This Pokemon will do. Here's a reward for your efforts.")
            user.vars.tro_consec_days += 1
            user.vars.tro_progress = 1
            give_reward()
        else:
            user.say("Team Rocket Officer: That is not the Pokemon I asked for.")
    else:
        user.say("Team Rocket Officer: I see you're still twiddling your thumbs while time is ticking down. You must complete your assigned task within {user.expire.daily_active}.")

elif user.vars.tro_progress == 2 and not user.vars.daily_active and not user.vars.daily_completed:
    user.say("Team Rocket Officer: I'm disappointed. I expected better from you, but you did not deliver. However, you still show a lot of promise and I have a new task for you.")
    user.say("Team Rocket Officer: Do not disappoint me again.")
    user.vars.tro_progress = 1
    user.vars.tro_consec_days = 0
    next_task()

elif user.vars.tro_progress == 2 and user.vars.daily_active and user.vars.daily_completed:
    user.say("Team Rocket Officer: I've been expecting you. Were you able to fulfill the task that was given to you?")
    user.say("Team Rocket Officer: Very good! I expected nothing less from you. Here's a reward for your efforts.")
    user.vars.tro_progress = 1
    user.vars.daily_active = False
    user.vars.daily_completed = False
    user.vars.tro_consec_days += 1
    give_reward()
