import random
from datetime import datetime

eliteTable = [
    'Elite-Table',
    'Nocturnal: Crits on 19s in dim light and 18s in darkness.',
    'Adaptive Defense: When under 75% HP, you gain 1 AC. When under 50% HP, you gain resistance to physical damage. When under 25% HP, you gain an additional +1 AC.',
    'Ambusher: Starts stealthed with its passive stealth. Gains proficiency or expertise (if already proficient) in stealth. Gains +10 to initiative. Surprises if it starts combat.',
    'Armored: Gain +2 AC and Physical damage DR equal to your CR.',
    'Assassin: Starts stealthed with its passive stealth. Can sneak as a bonus action. Gains proficiency or expertise (if already proficient) in stealth. Deals an extra 2d6/4d6/6d6/8d6 damage when attacking from stealth.',
    "Berserker: Gains 5/10/15/20ft of movement speed and deals an additional 2/4/6/8 damage on all attacks. Gains the 'Reckless' feature. Reckless: You can choose to gain advantage on melee attack rolls. Enemies have advantage to hit you.", 
    'Blooming: Can spend its action to heal all allies in a 20ft radius for 2d8+WIS/4d8+WIS/6d8+WIS/8d8+WIS',
    'Charming: Charisma increases by 6. Can spend its action to charm the player, Charisma DC or be charmed for 1 minute. Can repeat save at the end of their turn to end the effect.',
    'Conjurer: Can spend its action to conjure a minion of a CR equivalent to 1/4 its CR.',
    "Corrosive Weapon: Attacks reduce the target's AC by 1 every time they hit, to a maximum of -5. If they are wearing nonmagical armor, the armor breaks upon reaching -5. The penalty is removed after the encounter.", 
    "Corrosive Armor: Being attacked reduces the target's weapon damage by -1, to a maximum of -5. If they are wielding a nonmagical weapon, the weapon breaks upon reaching -5. The penalty is removed after the encounter.", 
    'Curse: Deals an extra 1d4/1d6/1d8/1d10 necrotic damage on one of its attacks. This attack causes a DC-Con/Cha Wisdom saving throw which, on failure, reduces the next saving throw done by the target by the necrotic damage.',
    'Duellist: Can use its reaction to attack someone who missed its AC. Gains a second reaction that it can only use on this.',
    'Eagle Eyed: Gains +5 on perception checks and passive perception and +2 to weapon accuracy.',
    "Executioner: Deals an additional 1d6/2d6/3d6/4d6 damage if you're bloodied.", 
    'Flaming: Attacks do an extra 1d4/2d4/3d4/4d4 fire damage. Once per turn when it hits a target, they must make a DC Con DEX saving throw in order to avoid burning. If they fail, they are on fire and take 1d4/2d4/3d4/4d4 fire damage at the start of each of their turns, or until they put the fire out as an action.',
    'Fungal: Immune to poison and the poisoned condition. When something with a body dies within 15ft of it, there is a 25% chance for it to be raised as a Fungal Zombie. Their mental scores become 3, their speed is reduced by 10 and they start at half HP, but are allied to the Fungal monster.',
    'Gang Leader: Has 3 minions that follow it around of a CR equal to its CR/4. If these minions die, they can spend their action to summon one minion of the same type.',
    'Grave Walker: When the target dies, it comes back to life as a ghostly version of itself. It has 1/4 as much HP and HP max, its AC becomes 10+Highest Mental Bonus, and all of its attacks deal necrotic damage instead. They gain resistance to acid, cold, fire, lightning, thunder, and nonmagical physical damage, Incorporeal Movement, and their move speed becomes a hover speed as well. Loses all other tags. Incorporeal Movement: The ghost can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.',
    'Guardian: Can spend a bonus action to redirect all of the attacks going to one target within 10ft of it to itself. When it redirects this attack, it has resistance to the damage.',
    "Horrific: At the start of this unit's turn, everyone within 15ft of them must make a Wisdom saving throw against a CON DC or be frightened of them until the end of their next turn.", 
    'Hound Master: This unit has a beast or monstrosity of CR/2 that they consider their pet. This monster also has its own modifiers, but may not have minions of its own.',
    'Hunter: Has the alert feat and deals an extra 1d6/2d6/3d6/4d6 on its first ranged attack in a turn. If they have no ranged attack, they instead apply this to their first melee attack.',
    'Infested: At the start of their turn, has a 25% chance to spawn a swarm of rot grubs, wasps, centipedes or beetles.',
    'Inspiring: Can spend a bonus action to give an ally an extra d6/d8/d10/d12 to their rolls. Additionally, it can chose up to six friendly creatures to gain temp HP equal to its CR plus its Charisma modifier. Charisma +4.',
    'Leech: As a bonus action, it can choose to deal 1d10+Con/2d10+Con/3d10+Con/4d10+Con necrotic damage to one of its allies within 60ft and heal that amount. It can use this ability as an action on PCs, and it becomes a DC Con Constitution saving throw.',
    "Lethal: Once per turn with one of its attacks it can cause a bleed effect. When struck by this attack, the target must make a Constitution saving throw DC Str or Dex or take 1d4/2d4/3d4/4d4 slashing damage at the start of their turn. This can be ended with the same DC medicine check as an action or by regaining HP from a healer's kit or potion. Otherwise, this effect ends after a minute.", 
    'Misty: The area 30ft around the target is always considered lightly obscured and dim light.',
    "Mutated: Gains an additional melee attack that deals 1d8/2d8/3d8/4d8 plus strength or dex that deals bludgeoning, slashing or piercing damage due to having an extra appendage that has transformed into a weapon. This melee attack is incorporated into the creature's multiattack. If they don't have multiattack, they gain it from this feature.", 'Necromancer: Can use an action to revive a corpse on the field as an undead. Their mental scores become 3, their speed is reduced by 10 and they start at half HP, but are allied to the necromancer. The necromancer cannot do this multiple times on the same corpse.',
    'Overwhelming: Once per turn on an attack, can cause a Strength save DC Strength/Dex where on failure, the opponent is knocked prone or pushed 10/20/30/40ft away.',
    'Piercing: Gains the piercer feat. If they do not have an attack that deals piercing damage, another one of their physical attacks deals piercing damage instead. Piercer: Once per turn, when you hit a creature with an attack that deals piercing damage, you can re-roll one of the attack’s damage dice, and you must use the new roll. When you score a critical hit that deals piercing damage to a creature, you can roll one additional damage die when determining the extra piercing damage the target takes.',
    'Plague Carrier: Once per turn, it can apply a constitution saving throw DC 8 + Con Bonus to one of its attacks in order to cause effects similar to the Contagion spell. The disease for this creature is (Copy this) [[1t[Plagues]]]. The carrier suffers an effect from this disease of your choosing, but only one.',
    'Poisonous: Once per turn on a specific attack it can cause a DC-Wis/Int (Humanoid) or DC-Con (Non-Humanoid) Constitution saving throw or cause them to take 2d6/4d6/6d6/8d6 poison damage.',
    'Regenerating: This creature gains 5/10/15/20 HP at the start of its turn. Choose a damage type that makes sense; causing this damage type will cause the regeneration to stop. A good example could be Necrotic damage for a priest or Acid damage for a monstrosity.',
    'Replicator: Every turn, there is a 20% chance that it summons a copy of itself. If it does this, it cannot do this again. Additionally, when it does this, both halve their max HP and split the remaining HP between the two.',
    'Resilient: Choose two saving throws for it to have proficiency in, and two damage types for it to resist.',
    'Robber: Once per turn when they hit you, they can cause a DC-Str/Dex Strength saving throw or attempt to disarm you of an object you are holding on failure.',
    "Rustic Curse: At the start of this creature's turn, all enemies within 10ft of this creature must make a DC-Con/Cha Wisdom saving throw or this monster gains resistance to their damage. This effect ends at the end of the target's next turn.", 
    'Sanguine: Once per turn on one specific attack, it can choose to regain half the damage dealt as HP.',
    'Savage: Gains "Savage Attacks" (half orc) and "Savage Attacker" (feat). Savage Attacks: When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit. Savage Attacker: Once per turn when you roll damage for a melee weapon attack, you can reroll the weapons damage dice and use either total.',
    "Shady: Gains proficiency or expertise in Stealth and the Skulker feat. Skulker: You can try to hide when you are lightly obscured from the creature from which you are hiding. When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position. Dim light doesn't impose disadvantage on your Wisdom (Perception) checks relying on sight.", 
    'Sticky: Once per turn, this creature can cause a DC-Wis/Int (Humanoid) or Con (Monster) Strength saving throw or cause a target to become stuck, causing them to be restrained and glued in place. This effect can be ended by spending an action to make a Strength (Athletics) check against the DC in order to break free.',
    'Storm Warden: Gains +2 AC against ranged attacks, and can choose to spend a reaction to cause a Dexterity saving throw DC-Mental (Humanoid) or Con (Monster), causing 1d8/2d8/3d8/4d8 lightning damage, half damage on save.',
    'Sunlit: The area in a 15ft radius around the target is always unobscured and bright light. Everyone has advantage on perception checks to find hidden creatures in this aura, and creatures in this aura have disadvantage on stealth checks. Deals an additional 2/4/6/8 radiant damage in bright light.',
    'Tainted: All of its attacks deal an extra 1d4/2d4/3d4/4d4 necrotic damage.',
    'Terrifying: Can spend its bonus/action to cause all creatures within 20ft of it to make a Wisdom saving throw DC-Cha/Str (Humanoid) or Con/Str/Dex (Monster) for one minute. The creature can re-make the saving throw at the end of their turn. Recharge 5-6.',
    'Thick Skin: Gain resistance to physical damage.',
    "Thief: Can spend a bonus action to attempt to steal an item from a creature that they are not holding, but can be wearing. They gain proficiency or expertise in Stealth and Sleight of Hand and can make a Sleight of Hand check from stealth against the target's passive perception.", 
    'Thorn Armor: When this enemy is struck in melee, they deal 1d4/2d4/3d4/4d4 piercing damage to the attacker automatically. When they roll a 4 on the thorns, they gain resistance to the incoming damage that caused this.',
    "Toxic: At the start of this creature's turn, everyone within 10ft of the creature must make a DC-Con Constitution saving throw or take 1d8/2d8/3d8/4d8 poison damage.", 
    'Toxic Spores: Can spend its action to cause everyone within 30ft to make a DC-Con Constitution saving throw or take 1d8/2d8/3d8/4d8 poison damage, or half damage on fail.',
    'Tracker: Has the Alert feat, proficiency or expertise in Perception, and can spend a bonus action in order to search for hidden targets.',
    'Undying: When this target is reduced to 0 HP, it returns to 25% HP and gains resistance to physical damage.',
    'Vampiric: Once per turn on one specific attack, it deals an additional 1d6/2d6/3d6/4d6 necrotic damage. When this attack hits, it heals for the necrotic damage dealt.',
    'Massive: Its size increases by 1 step, and your hit dice increases in size by 1 step as well. If it already has a d12 hit dice, it instead gains 2 extra hit points per level.',
    'Area Attacker: One of its attacks targets a 5ft radius area or a 15ft arc in front of it instead of one target.',
    'Legendary: They gain a legendary action. They can only use it to attack once or move without causing opportunity attacks.',
    "Cavalry: This creature has a mount of CR/4 that they ride on top of. Their mount also has its own modifiers, but may not have minions of its own. The creature gains the Mounted Combatant feat. Mounted Combatant feat: You are a dangerous foe to face while mounted. While you are mounted and aren't incapacitated, you gain the following benefits:You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount.You can force an attack targeted at your mount to target you instead.If your mount is subjected to an effect that allows it to make Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.", 
    'Constructed: If the elite is already a Construct, reroll this trait. Otherwise, they are comprised entirely of metal and are an automaton. They gain immunity to poison damage and the poisoned condition, their creature type becomes Construct and their AC increases by 2.',
    "Undead: If the elite is already an Undead, reroll this trait. Otherwise, they are an undead creature. They gain immunity to the poisoned condition, resistance to poison and necrotic damage. They gain one of two traits in addition: [[1d2]] 1: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. If you do, you reduce yourself to a pile of bones, render yourself prone, and are considered to be under a similar effect to the feign death spell. While subject to this condition, you are unable to move or take actions other than using an action to end this effect. Once you use this trait, you can't use it again until you finish a long rest. 2: If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie drops to 1 hit point instead.", 
    'Heavily Armored: Gains Splintmail [17] / Platemail [18] / +1 Platemail [19] / +2 Platemail [20]. If their armor is already better, they instead gain the Armored trait.',
    'Heavily Armed: If they are wielding a simple weapon, they are instead wielding a martial weapon of equivalent size. (CR 5+) Their weapon becomes a +1/+2/+3 Weapon. If they are already using a martial weapon, reroll this trait.',
    'Otherworldly: When you attack this target, they can use their reaction to create an aethereal tentacle to attack you back. This aetherial tentacle uses their highest mental score to hit, and deals 1d6/3d6/5d6/7d6 plus their modifier force damage on a hit.',
    'Adventurer: The monster gains 1/2/3/4 levels in a regular D&D class. The hit dice from their class is added onto their health. They gain starting equipment.',
    "Aquatic: You gain the ability to breathe underwater and a swim speed equal to 1.5x your movement speed. You can cast 'Create Water' once per long rest.", 
    'Corrupting: As a bonus action, can turn a Corpse into a Corrupted Corpse. Enemies who end their turn within 5/5/10/10ft of a Corrupted Corpse must make a DC-Mental Charisma saving throw or take 1d6/3d6/5d6/7d6 necrotic damage. Corrupted corpses stop being corrupted when the monster with this tag dies.',
    'Lore Keeper: Your Intelligence increases by 6. Choose up to 3 cantrips or 1st level/2nd level/3rd level/4th level spells. They can cast each of these once per day. They use Intelligence to cast.',
    'Molten: At the start of its turn, everyone within 5/5/10/10ft of it must make a Constitution saving throw DC Constitution or take 1d6/2d6/3d6/4d6 fire damage. When someone hits you, they take fire damage equal to your CR.',
    'Moonlit: Sheds 10ft of dim light around it. Deals an additional 1d6/2d6/3d6/4d6 radiant damage on one of its attacks in dim light.',
    'Spiteful: When this creature takes damage, it can use its reaction to make an attack against the target that damaged it.',
    'Venomous: Once per turn, it can apply an additional 1d4/2d4/3d4/4d4 poison damage on an attack. When someone takes this poison damage, they have disadvantage on their next Constitution saving throw within 1 minute.',
    "Custodian: Can use its reaction to redirect one attack or effect that would harm an allied creature within 30ft of it to itself. If it's a saving throw it has advantage on the roll; if it's an attack, it resists the damage. It cannot redirect an effect that would also effect it, like a Fireball.", 
    'Unstable: When this creature takes damage, it causes a thunderous explosion. Everyone within 5/5/10/10ft of the target must make a DC Con Constitution saving throw or take 1d4/3d4/5d4/7d4 thunder damage.',
    "Half-Dragon: You gain a blindsight of 10ft, a darkvision of 60ft, resistance to your draconic heritage damage type, and a breath weapon. As an action, everyone within a 15/30/60/90ft cone or 30/60/90/120ft line 5ft wide must make a DC Con Dexterity saving throw or take 4d8/8d8/12d8/16d8 damage of your element. Recharge (5-6). Roll the draconic heritage - (choose or roll a d10): 1–2, acid (black [line] or copper [line]); 3–4, cold (silver [cone] or white [cone]); 5–7, fire (brass [line], gold [cone], or red [cone]); 8-9, lightning (blue [line] or bronze [line]); 10, poison (green [Cone]). Reroll if you aren't: Humanoid, Monstrosity, Beast, Giant", 
    "Avenger: For every allied monster that dies in this creature's presence, they add 1 to their AC and 1/2/3/4 to their damage, HP, and max HP, to a maximum of 5 stacks.", 
    'Desecrator: As an action with a recharge of 5-6, the creature can summon a pool of void energy with a 5ft radius. This pool is difficult terrain, and anyone who starts their turn in the pool or enters the pool for the first time on their turn must make a Constitution saving throw DC Mental (Humanoid) or Constitution or take 2d6/4d6/6d6/8d6 necrotic damage, half damage on pass.',
    'Fast: The monster gains 10/20/30/40ft of movement speed.',
    'Frozen: As an action with a recharge of 5-6, the creature can summon a superchilled ice crystal. When the crystal first appears, anyone within 5ft of the crystal must make a DC Mental (Humanoid) or Constiution Constitution saving throw or take 1d8/2d8/3d8/4d8 cold damage, half damage on pass. In 3/2/1/1 turns, the crystal will explode. Everyone within 10ft of the crystal when that happens must make a Strength saving throw with the same DC as earlier, becoming restrained and taking 2d6/4d6/6d6/8d6 cold damage on fail. ',
    'Illusionist: As a reaction ability with a recharge of 5-6, the monster can cast Mirror Image when an attack targets them.',
    'Magmatic: When the monster starts its turn on a tile, that tile becomes molten. Anyone who steps onto that tile automatically takes 2d6/4d6/6d6/8d6 fire damage. The molten effect dissipates at the start of their next turn. A molten monster is resistant/resistant/immune/immune to fire damage and cannot be affected by other molten tiles.',
    'Combustible: When this creature dies, it explodes, causing a DC Con Dexterity saving throw that deals 2d8/4d8/6d8/8d8 fire damage in a 10/15/20/25ft radius around itself, or half damage on a failure.',
    'Psionic: They gain +4 Intelligence, to a minimum of 12/14/16/18 and gain a Mind Blast AOE with Recharge 6/5-6/5-6/4-6. The Mind Blast deals 2d6/5d6/8d6/11d6 Psychic damage in a 10ft/20ft/30ft/40ft cone and stuns the target on a failure more than 5.',
    'Hoarder: The creature has access to four randomly-selected consumable items of common/uncommon/rare/very rare rarity. If they use them, are killed with an AOE, or use a free action to empty their bag, they are lost.',
    'Item User: The creature has access to a randomly-selected magic item of common/uncommon/rare/very rare rarity. There is a 50% chance the item is dropped.',
    'Magic Resistance: The creature has advantage on saving throws against magical spells and effects. If they already had this ability, they gain resistance to magical spells and effects. If they already had this ability, they have a 10/15/20/25% chance to reflect the spell back at the caster.',
    'Reflective: The creature has a 15/20/25/30% chance to reflect a spell back at the caster. The spellcaster uses their own saving throw DC or attack roll against themselves.'
]

randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
print("This is the seed: ", seed)
randomizer.seed(seed)

option = 0
while(option != -1):
    print("===========================================================")
    print("Choose how many traits to generate: ", end="")
    option = int(input())
    print("===========================================================")
    alreadyRolled = []
    for x in range(0, option):
        trait = randomizer.randrange(1, eliteTable.__len__())
        while(trait in alreadyRolled):
            trait = randomizer.randrange(1, eliteTable.__len__())
        alreadyRolled.append(trait)
        trait = eliteTable[trait]
        print(trait)
        if(x != option-1):
            print("")