print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Onwards Towards The Treasure!! Arrrgh~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Welcome to Bones, The Island Where The Greatest Treasure Lies ,"THE ONE PIECE"')
choice = input("Press Enter To Begin")

print('You Land At The Shore Of The Island, After Sailing The Grand Line')
print('What Is The Fisrt Thing You Would Do ?')
choice = input('1.Search for Resourses 2.Search for Crewmates 3.Search for the Treasure')
if choice == "1":
    print("You Find Abundance Of Fruits & Drinkable Water")
    counter = 3
    while counter > 0:
        choice = input("1.Rest ? 2.Setout to Find the treasure")
        if choice == "1":
            counter = counter - 1
            if counter == 0:
                print("Game Over, You Used Up All The Resources & Died Without Finding The Treasure")
                exit()
        else:
            print("You Find Yourself Looking At The Cave Opening")
            break
    print("What Do You Want To Do ?")
    choice = input("1.Go In, 2.Look Around for survivors")
    if choice == "1":
        print('''
           ,aodObo,
        ,AMMMMP~~~~
     ,MMMMMMMMA.
   ,M;'     `YV'
  AM' ,OMA,
 AM|   `~VMM,.      .,ama,____,amma,..
 MML      )MMMD   .AMMMMMMMMMMMMMMMMMMD.
 VMMM    .AMMY'  ,AMMMMMMMMMMMMMMMMMMMMD
 `VMM, AMMMV'  ,AMMMMMMMMMMMMMMMMMMMMMMM,                ,
  VMMMmMMV'  ,AMY~~''  'MMMMMMMMMMMM' '~~             ,aMM
  `YMMMM'   AMM'        `VMMMMMMMMP'_              A,aMMMM
   AMMM'    VMMA. YVmmmMMMMMMMMMMML MmmmY          MMMMMMM
  ,AMMA   _,HMMMMmdMMMMMMMMMMMMMMMML`VMV'         ,MMMMMMM
  AMMMA _'MMMMMMMMMMMMMMMMMMMMMMMMMMA `'          MMMMMMMM
 ,AMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMa      ,,,   `MMMMMMM
 AMMMMMMMMM'~`YMMMMMMMMMMMMMMMMMMMMMMA    ,AMMV    MMMMMMM
 VMV MMMMMV   `YMMMMMMMMMMMMMMMMMMMMMY   `VMMY'  adMMMMMMM
 `V  MMMM'      `YMMMMMMMV.~~~~~~~~~,aado,`V''   MMMMMMMMM
    aMMMMmv       `YMMMMMMMm,    ,/AMMMMMA,      YMMMMMMMM
    VMMMMM,,v       YMMMMMMMMMo oMMMMMMMMM'    a, YMMMMMMM
    `YMMMMMY'       `YMMMMMMMY' `YMMMMMMMY     MMmMMMMMMMM
     AMMMMM  ,        ~~~~~,aooooa,~~~~~~      MMMMMMMMMMM
       YMMMb,d'         dMMMMMMMMMMMMMD,   a,, AMMMMMMMMMM
        YMMMMM, A       YMMMMMMMMMMMMMY   ,MMMMMMMMMMMMMMM
       AMMMMMMMMM        `~~~~'  `~~~~'   AMMMMMMMMMMMMMMM
       `VMMMMMM'  ,A,                  ,,AMMMMMMMMMMMMMMMM
     ,AMMMMMMMMMMMMMMA,       ,aAMMMMMMMMMMMMMMMMMMMMMMMMM
   ,AMMMMMMMMMMMMMMMMMMA,    AMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 ,AMMMMMMMMMMMMMMMMMMMMMA   AMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
AMMMMMMMMMMMMMMMMMMMMMMMMAaAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM''')
        print("Game Over, You Got Eaten By A lion")
        exit()
    else:
        print("You Find An Local Tribe Village")
        choice = input("1.Approach the Village")
        print("The TribalPeople Look At You At Awe")
        print("? reffO oT evaH uoY oD tahW")
        choice = input("Did You Understand ? (y/n)")
        if choice == 'y' :
            choice = input("secruoseR llA mehT gniviG yB tsurT niaG.2 , secruoseR emoS mehT gniviG yB tsurT niaG.1")
            if choice == "1" or counter < 2:
                print("Tribal People Show You the One Piece But Since Your Offering Was Not Enough They Cooked You !! GAME OVER")
                print('''
                               _.(-)._
                            .'         '.
                            /             \
                            |'-...___...-'|
                             \    '='    /
                              `'._____.'`
                               /   |   \
                              /.--'|'--.\
                            []/'-.__|__.-'\[]
                                    |
                                    [] ''')
                exit()
            elif choice == "2" and counter >= 2:
                print("You Gain Their Trust And They Give You The Treasure!!!")
                print("CONGRATULATIONS YOU WIN THE 'One Piece'")
                print('''
                                         ____
                        /\  __\_
                       /  \/ \___\
                       \     /___/
                    /\_/     \    \
                   /          \____\
               ___/\       _  /    /
              / \/  \     /_\/____/
              \     /     \___\
              /     \_/\  /   /
             /          \/___/
             \  _       /   /
              \/_|     /___/
                 /     \___\
                 \  /\_/___/
                  \/___/
                
''')
        else:
            print("You Got Stabbed, 'poP poP rrrrrkS ,maF sdnE gnorW eht nI ruoY'")
            print("GAMEOVER")
            exit()
elif choice == "2":
    print("You Kept Walking Until You Found A Sight Of Life, But Due To Starvation & DeHydration, You Died")
    print("GAME OVER")
    print('''
                                               .""--.._
                                           []      `'--.._
                                           ||__           `'-,
                                         `)||_ ```'--..       \
                     _                    /|//}        ``--._  |
                  .'` `'.                /////}              `\/
                 /  .""".\              //{///
                /  /_  _`\\            // `||
                | |(_)(_)||          _//   ||
                | |  /\  )|        _///\   ||
                | |L====J |       / |/ |   ||
               /  /'-..-' /    .'`  \  |   ||
              /   |  :: | |_.-`      |  \  ||
             /|   `\-::.| |          \   | ||
           /` `|   /    | |          |   / ||
         |`    \   |    / /          \  |  ||
        |       `\_|    |/      ,.__. \ |  ||
        /                     /`    `\ ||  ||
       |           .         /        \||  ||
       |                     |         |/  ||
       /         /           |         (   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \ `-._       |           /              ||
    \ ,//`\    /`           |              ||
     ///\  \  |             \              ||
    |||| ) |__/             |              ||
    |||| `.(                |              ||
    `\\` /`                 /              ||
       /`                   /              ||
      /                     |              ||
     |                      \              ||
    /                        |             ||
  /`                          \            ||
/`                            |            ||
`-.___,-.      .-.        ___,'            ||
         `---'`   `'----'`
''')
    exit()
else:
    print("As You Get Towards The Inside Of the Cave, The Volcana Irupts Killing Everthing On The Island")
    print("Game Over")
    print('''
                          ooO
                     ooOOOo
                   oOOOOOOoooo
                 ooOOOooo  oooo
                /vvv\
               /V V V\ 
              /V  V  V\          
             /     V   \          AAAAH!  RUN FOR YOUR LIVES!
            /      VV   \               /
 ____      /        VVV    \   	  o          o
 /\      /        VVVV     \     /-   o     /-
/  \   /           VVVVVVV   \  /\  -/-    /\
                    VVVVVVVVVVVVV   /\
''')
    exit()

print('Working')