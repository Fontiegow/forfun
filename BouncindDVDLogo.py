import sys, time , random

try : 
    import bext

except ImportError :
    print("This program requires the Bext module which you can install by running 'pip3 install bext'")
    sys.exit("bext is not installed")

WIDTH , HEIGHT = bext.size()

WIDTH -= 1

NUMBER_OF_LOGOS = 5 
PAUSE_AMOUNT = 0.2 

COLORS =['red','green','blue','yellow','magenta','cyan','white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = [UP_RIGHT , UP_LEFT , DOWN_RIGHT , DOWN_LEFT]

COLOR = 'color'
DIR = 'direction'
X = 'x'
Y = 'y'

def main() :
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGOS) : 
        logos.append({COLOR : random.choice(COLORS) ,
                        X : random.randint(0,WIDTH - 4) ,
                        Y : random.randint(0,HEIGHT - 4),
                     DIR : random.choice(DIRECTIONS)})
        
        if logos[-1][X] % 2 == 1 :    # make sure x is even so it will hit the corner. 
            logos[-1][X] -= 1

    cornerBounces = 0 
    while True :
        for logo in logos :
            bext.goto(logo[X] , logo[Y])
            print('  ' , end=' ')
            
            originalDirection = logo[DIR] 
            
            if logo[X] == 0 and logo[Y] == 0 :
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT -1  :
                logo[DIR] = UP_RIGHT
                cornerBounces += 1 
            elif logo[X] == WIDTH - 3 and logo[Y] == 0 :
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1 :
                logo[DIR] = UP_LEFT 
                cornerBounces += 1    

            # see if the logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT :
                logo[DIR] == UP_RIGHT 
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT :
                logo[DIR] = DOWN_RIGHT 

            # see if the logo bounces off the right edge (WIDHT -3 BECAUSE DVD is 3 leters wide)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT :        
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT :
                logo[DIR] = DOWN_LEFT 

            # see if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT :
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT :
                logo[DIR] = DOWN_RIGHT

            #see if the logo bounces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT :
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT :
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection :
                logo[COLOR] = random.choice(COLORS) 

            # Move the logo
            # X moves by 2 because Characters are twice as tall as they are wide.  
            if logo[DIR] == UP_RIGHT :
                logo[X] += 2 
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT :
                logo[X] -= 2 
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT :
                logo[X] += 2 
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT :  
                logo[X] -= 2 
                logo[Y] += 1

        # Display Number of Corner Bounces
        bext.goto(5 , 0)
        bext.fg('white')
        print('Corner Bounces: ' , cornerBounces , end='') 

        # Draw logos at their locations 
        for logo in logos :
            bext.goto(logo[X] , logo[Y])
            bext.fg(logo[COLOR])
            print('DVD' , end='')
        
        bext.goto(0, 0)

        sys.stdout.flush() # Required to make the output show up immediately. and for bext-using programs.
        time.sleep(PAUSE_AMOUNT) 

if __name__ == '__main__' :
    try :
        main()
    except KeyboardInterrupt : 
        print()
        print('Bouncing Logo by Farid Nahaie (Inspired by Al Sweigart)') 
        sys.exit()  
