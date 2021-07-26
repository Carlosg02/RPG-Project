#ROLE_PLAYING_Game
#features/ideas to implement
  #fighting game where you fight/battle others.
    # implementing a fight system where the users have an initial health pool and an experience points can be gained
    #as you level up you can increase hp or increase your own dmg.
        #-player moves and the amount of hitpoints can be stored in a  list
        #variable needed for player
#Introduction of our game and using strings 
import random
from replit import audio as s
welcomeString = """ 
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

███╗░░░███╗██╗░░░██╗██╗░░░░░████████╗██╗██████╗░██╗███╗░░░███╗███████╗███╗░░██╗░██████╗██╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░
████╗░████║██║░░░██║██║░░░░░╚══██╔══╝██║██╔══██╗██║████╗░████║██╔════╝████╗░██║██╔════╝██║██╔══██╗████╗░██║██╔══██╗██║░░░░░
██╔████╔██║██║░░░██║██║░░░░░░░░██║░░░██║██║░░██║██║██╔████╔██║█████╗░░██╔██╗██║╚█████╗░██║██║░░██║██╔██╗██║███████║██║░░░░░
██║╚██╔╝██║██║░░░██║██║░░░░░░░░██║░░░██║██║░░██║██║██║╚██╔╝██║██╔══╝░░██║╚████║░╚═══██╗██║██║░░██║██║╚████║██╔══██║██║░░░░░
██║░╚═╝░██║╚██████╔╝███████╗░░░██║░░░██║██████╔╝██║██║░╚═╝░██║███████╗██║░╚███║██████╔╝██║╚█████╔╝██║░╚███║██║░░██║███████╗
╚═╝░░░░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝

███████╗██╗░██████╗░██╗░░██╗████████╗███████╗██████╗░  ░██████╗████████╗██████╗░███████╗███████╗████████╗
██╔════╝██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝██╔══██╗  ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝
█████╗░░██║██║░░██╗░███████║░░░██║░░░█████╗░░██████╔╝  ╚█████╗░░░░██║░░░██████╔╝█████╗░░█████╗░░░░░██║░░░
██╔══╝░░██║██║░░╚██╗██╔══██║░░░██║░░░██╔══╝░░██╔══██╗  ░╚═══██╗░░░██║░░░██╔══██╗██╔══╝░░██╔══╝░░░░░██║░░░
██║░░░░░██║╚██████╔╝██║░░██║░░░██║░░░███████╗██║░░██║  ██████╔╝░░░██║░░░██║░░██║███████╗███████╗░░░██║░░░
╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░   """
print(welcomeString)
print("\n+++++++++++++WELCOME TO MULTIDIMENSIONAL FIGHTER STREET+++++++++++++")
print("$$$$$$$ Rated: M for money $$$$$$$\n")
print("\n")

#global variables
playerName =  input("Enter your name to play: ")

#move1 is index 0, rando move is index 1-2, heals is index 3
player = [25, 15, 35, 22,playerName] 
playerHealth = 200
currentLevel = 0
currentXP = 0

# required xp to level up
requiredXP = 50

# foe GLOBAL variables
foeHealth =  0 

# to add a foe make sure to follow the list format below and add thier name to the foes list
dragon = [200,250, 20, 10, 35, 15,"Dragon"] #health index:0, 1 , move1 index:2, move2 index:3 and 4(randomizing move), heals index 5.    
wizard = [150,200, 10, 15, 25, 30,"Wizard"] #health, move1, move2 (randomizing move), heals    
firebird = [150,200, 20, 10, 25, 20,"Firebird"] #health, move1, move2 (randomizing move), heals    
mermaid = [60,120, 10, 5, 35, 50,"Mermaid"] #health, move1, move2 (randomizing move), heals    
alien = [100,190, 15, 20, 30, 20,"Alien"] #health, move1, move2 (randomizing move), heals    
# all foes
foes =  [dragon, wizard, firebird, mermaid, alien]  

# functions
def playGame():

    global player, playerHealth, currentLevel, currentXP, requiredXP, start

    # display current stats
    print(f'{playerName}, these are your current stats HP: {playerHealth}hp. upperCut: {player[0]}dmg. thunderbolt throw (varies): {player[1]}-{player[2]}dmg. self-heal: {player[3]}hp')
    print("\nLevel up as you play to increase your moves/health. battle others and gain 50XP!")

    print("your evil foes: ")
    #print out all foes in list
    for i in range(len(foes)):
        print(f'{foes[i][-1]}')
      
    print("\n")
    print("************************************************************************************\n")
    
    # pick the foe based on foe list and return their moves list and randomized health
    fightFoe, foeHealth = pickFoe(foes)

    # randomizing naration but use the name of selected hero
    tellStory(playerName, fightFoe)
    
    # start the battle and return reset health and also any gained xp. return winning music to pause.  
    playerHealth, currentXP, winM = battle(player,fightFoe, foeHealth,start)
    #player,fightFoe,playerHealth, foeHealth,currentXP
    
    levelCheck(player)
    
    winM.paused = True
    winM.volume = .05

    print(f'player obj test: {player}')
    
    return winM

# randomizing the foes with randomized health 
def pickFoe(foeList):
    
    currFoe = foeList[random.randint(0,4)]
    
    foeHealth = currFoe[random.randint(0,1)]
      
    return currFoe, foeHealth




def battle(playerMoves, foeMoves, foeCurrHealth, start):
    
    global playerHealth, currentXP

    print("\nLet the fight begin!")

    healthStart = playerHealth

    # print(f'{foeMoves[-1]}\'s health: {foeCurrHealth}')
    # print(f'your health: {playerHealth}')

    while foeCurrHealth >= 0 and playerHealth >= 0:
        

        print(f'\n{foeMoves[-1]}\'s health: {foeCurrHealth}')
        print(f'your health: {playerHealth}')

        print(f"\nayooo? 1. upperCut ({player[0]} damage) 2. thunderbolt throw ({player[1]}-{player[2]} damage)  3. heals ({player[3]} hp.)")
        usrSel = input("make a selection (1-3 only or you lose you chance to attack): ")

        if usrSel == "1":
            
            print(f'\n-=-=-=**{playerMoves[-1]} upperCuts {foeMoves[-1]}-')
            
            foeCurrHealth -= playerMoves[0]
            
            print(f'{foeMoves[-1]} new health -({playerMoves[0]}hp): {foeCurrHealth}')
        elif usrSel == "2":
            
            print(f'\n-=-=-=**{playerMoves[-1]} throws a thunder bolt at {foeMoves[-1]}-')
            
            randomAttack = random.randint(playerMoves[1],playerMoves[2])
            
            foeCurrHealth -= randomAttack
            
            print(f'{foeMoves[-1]} new health -({randomAttack}hp): {foeCurrHealth}')
        elif usrSel == "3":
            
            print("\n-=-=-=**Healing...")
            
            playerHealth += playerMoves[3]    
            
            print(f'your health +({playerMoves[3]}hp): {playerHealth}')
        elif usrSel == "00100":
            print("ahhhhhhhhh I see you want to see what it's like to cheat")
            for i in range(4):
                playerMoves[i] = 250

            playerHealth = -1   
            
        else:
            
            print("incorrect selection")
            
            continue     


        foeSel  = random.randint(1,3)

        
        if foeSel == 1:

            print(f'-=-=-=**{foeMoves[-1]} attacks {playerMoves[-1]}-')
            
            playerHealth -= foeMoves[2]
            
            print(f'you lost health (-{foeMoves[2]}hp): {playerHealth}')
        
        elif foeSel == 2:
            
            print(f'-=-=-=**{foeMoves[-1]} rando attacks {playerMoves[-1]}-')
            
            randomAttack = random.randint(foeMoves[3],foeMoves[4])
            
            playerHealth -= randomAttack
            
            print(f'you lost health (-{randomAttack}hp): {playerHealth}')
        
        elif foeSel == 3:
            
            print("-=-=-=**Foe Healing...")
            
            foeCurrHealth += foeMoves[5]    
            
            print(f'foe health +({foeMoves[5]}hp): {foeCurrHealth}')
   
    
    if foeCurrHealth <= 0:
        start.paused = True

        m = s.play_file('music.mp3')
        # m = s.play_file('music.mp3')
        m.volume = .09 
        
        print("\n======VICTORY!! +++50xp points!======")
        currentXP += 50
        
        print("...health is now reset..")
        playerHealth = healthStart

        input("continue?")
    elif playerHealth <= 0:
        start.paused = True

        m = s.play_file("L.mp3")
        m.volume = .09


        print("\nYou've been defeated! ( no XP gained :( )")
        print("You'll get em next time")
        
        
        print("...health is now reset..")
        playerHealth = healthStart

        input("continue?")
    else:
        print("\nmathmatical miracle...TIE")    

    return (playerHealth, currentXP,m)          


def levelCheck(player):
  #Once the user has gained xp their level will be checked
  global currentLevel
  global currentXP
  global requiredXP
  
  #If they havent reached the required XP then nothing will happen
  if currentXP < requiredXP:
    pass
  elif currentXP == requiredXP or currentXP > requiredXP: #The level up process will happen once their current XP equals or passes the required XP
    currentLevel += 1 #They will level up by 1 level
    print(f'\n⊱ ────── Congrats you are now level {currentLevel}────── ⊰')
    
    levelUp(player) #The levelup function will run allowing them to upgrade their stats
   
    if currentXP > requiredXP: # if they end up with more currentxp then required then they will have the extra xp added to their next level progression.
      currentXP = currentXP - requiredXP
    else:
      currentXP = 0 #if they have the exact xp then they will reset back to 0 once they level up 
    # removed for demo purposes  
    # requiredXP += 100


def levelUp(player):
    #if the player levels up prompt to pick move to add power.
    # health index 0, move index 1, rando move index 2-3, heals, 4
    global playerHealth
    choiceSelected = False

    
    while choiceSelected == False:
      lv_choice = input("\n⊱ ────── Would you like to:\n (1) Increase max health by 25\n (2)Increase your damage by 5\n (3) Increase your healing amount by 10 \n Input selection here: ")
      if lv_choice == '1':  #This will level up their health 
       playerHealth += 25
       choiceSelected = True
       return player, playerHealth
      
      elif lv_choice == '2':  #This will level up their attack damage
        player[0] += 5
        player[1] += 5
        player[2] += 5
        choiceSelected = True
        return player, playerHealth

      elif lv_choice == '3': #This will level up their healing ability
        player[3] += 10
        choiceSelected = True
        return player, playerHealth
        
      else:
        print("Please enter in a valid number")
        continue
             
def tellStory(usrName,currentFoe):
#randomizes the setting and links back to who you are fighting
    foeName = currentFoe[-1]
    
    adj = ["foul smelling", "angry", "repulsive", "massive", "nasty", "colossal", "angry", "ferocious"]
    place = ["castle", "beach", "town", "forest", "jugnle", "ocean", "city", "boat" ]

    adj1 =  adj[random.randint(0,len(adj)-1)]

    place1 = place[random.randint(0,len(place)-1)]

    print(f'\n⊱ ────── The {adj1} {foeName} showed up out of nowhere as {usrName} was heading to the {place1} , get ready to fight! ────── ⊰')

    return
  
#### Actual Game / Story #####

print("⊱ ────── NOTE: Characters may stay alive for up to negative 50 hitpoints before dying if they heal on their turn")

while True:
    
    #  play background audio    
    start = s.play_file("start.mp3")
    start.volume = .05
    start.set_loop = 0 
    
    pause = playGame()
    pause.paused = True    

