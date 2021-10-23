class Characters:
    def __init__(self, race, name, age, emptiness):
        if race == "gnome":
            self.intelligence = 0  # Основные характеристики
            self.strength = 0  # Основные характеристики
            self.agility = 0  # Основные характеристики
            self.resistance = 0  # Основная характеристика
            # -----------------------------------------------Доп. Характеристики
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.mobility = 0
            # ---------------------------------------------- Характеристики, изменяемая только внешними факторами
            self.height = 0
            self.weight = 0
            self.age = age
            self.muscles = 0
            self.emptiness = emptiness + (age // 100)
            self.voidDef = 0
            self.statusRes = 0
            # -----------------------------------------Характеристики, изменяемаые основными хар. + внешними факторами
            self.learningSkill = 0 + self.intelligence * 0.1
            self.physDefence = 0
            self.magicDefence = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0 + self.resistance * 0.33
            self.fireDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.energyDef = 0 + self.allElemDef
            self.attackSpeed = 0 + self.agility * 0.1
            # -------------------------------------------------Незименяемые характеристики
            self.race = race
            self.name = name
            self.evilNature = 0
            # --------------------------------------------Характеристики, изменяемые только основными характеристиками
            self.aggression = 0 * (self.intelligence // 100)
            print("Hi, imgnome")
        if race == "high-elf":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0

            print("Hi, imhigh-elf")
        if race == "dark-elf":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0

            print("Hi, imdark-elf")
        if race == "human":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imhuman")
        if race == "beastlike":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imbeastlike")
        if race == "undead":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imundead")
        if race == "beast":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imbeast")
        if race == "birdlike":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imbirdlike")
        if race == "coldblooder":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imcoldblooder")
        if race == "highhuman":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imhighhuman")
        if race == "orc":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imorc")
        if race == "troll":
            self.intelligence = 0
            self.strength = 0
            self.agility = 0
            self.health = 0 + self.strength * 0.25
            self.energy = 0 + self.intelligence * 0.4
            self.attackSpeed = 0 + self.agility * 0.1
            self.learningSkill = 0 + self.intelligence * 0.1
            self.height = 0
            self.weight = 0
            self.mobility = 0
            self.physDefence = 0
            self.magicDefence = 0
            self.race = race
            self.name = name
            self.age = age
            self.emptiness = emptiness
            self.evilNature = 0
            self.aggression = 0
            self.lifeLeak = 0
            self.muscles = 0
            self.initiative = 0
            self.morale = 0
            self.allElemDef = 0
            self.fireDef = 0 + self.allElemDef
            self.voidDef = 0
            self.energyDef = 0 + self.allElemDef
            self.coldDef = 0 + self.allElemDef
            self.statusRes = 0


            print("Hi, imtroll")