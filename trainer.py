#!python


poke_list = ["Absol", "Empoleon", "Sigilyph", "Magmortar", "Tangrowth", "Noivern"]
nature_list = [Nature.Jolly, Nature.Modest, Nature.Timid, Nature.Modest, Nature.Sassy, Nature.Timid]
ability_list = ["Justified", "Torrent", "Magic Guard", "Vital Spirit", "Regenerator", "Infiltrator"]
move_list = [("Lovely Kiss", "Ice Beam", "Psychic", "Nasty Plot"),
             ("Fiery Dance", "Quiver Dance", "Giga Drain", "Bug Buzz"),
             ("Swords Dance", "Earthquake", "Iron Head", "Rock Tomb"),
             ("Icicle Crash", "Ice Shard", "Low Kick", "Poison Jab"),
             ("Moonblast", "Ice Beam", "Flamethrower", "Focus Blast"),
             ("Swords Dance", "Bullet Punch", "Bug Bite", "Roost")]

for poke, nature, ability, skills in zip(poke_list, nature_list, ability_list, move_list):
    p = Pokemon(poke, 100)
    p.nature = nature
    p.ability = ability
    p.skills = skills
    npc.team.append(p)


def start_battle():
    user.pause()
    if user.battle(npc, no_exp=True, no_teleport=True) == 1:
        user.say("Ok... Ok... You win.")
        user.say("I guess I'll consider joining Team Rocket.")
        user.vars.daily_completed = True
    else:
        user.say("Haha! I always knew that Team Rocket were just a bunch of losers!")


if npc.last_fight and user.vars.daily_active and not user.vars.daily_completed:
    user.say("You're back...? You really don't know when to give up. I guess I'll have to teach you the same lesson again!")
    start_battle()

elif user.vars.which_task == 3 and user.vars.daily_active and not user.vars.daily_completed:
    user.say("Wait... You want me to join who?! I guess I'll have to teach you a lesson.")
    start_battle()