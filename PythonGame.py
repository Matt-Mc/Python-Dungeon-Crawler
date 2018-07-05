#Dungeon Crawler
#Matthew McCarty

from random import *
from graphics import *

x = 0
y = 0
difficulty = 0

def Generate(x,y,diff):
        #This creates the game board by making and filling a grid
        grid = []
        sgrid = []
        generate = randint(1,100)

        empty = "X"
        blocked = "+"
        mob = "M"
        player = "O"
        end = "!"
        shop = "S"
        unexplored = "#"


        
        #Generates the gameboard that will be used for comparison to the shown gameboard that the play will navigate
        for i in range(y):
                row = []
                for j in range(x):
                        generate = randint(1,100)
                        if generate >= 55:
                              row.append(empty)
                        elif generate < 55:
                                generate = randint(1,100)
                                if generate > 90:
                                        row.append(blocked)
                                elif generate < 30:
                                        row.append(mob)
                                elif generate == 50:
                                        row.append(shop)
                                elif generate >= 30:
                                          row.append(empty)      
                grid.append(row)


        grid[0][0] = "O"
        grid[x - 1][y - 1] = "!"


        #creates the gameboard shown to player, with tiles covered.
        for i in range(y):
                row = []
                for j in range(x):
                        row.append(unexplored)
                sgrid.append(row)

        sgrid[0][0] = "O"
        sgrid[x - 1][y - 1] = "!"


        for i in range(x-1):
                for j in range(y-1):
                        if(i < x and j < y):
                                if(grid[i][j] == "+" and grid[i][j+1] == "+" or grid[i-1][j] == "+"):
                                        grid[i][j] == "X"
        
        for row in grid:
                print(row)
        print("\n")
        
        for row in sgrid:
                print(row)


                
        main(x,y)
        play(grid,x,y,diff,sgrid)
        





def play(grid,x,y,diff,sgrid):
        xp = 0
        yp = 0
        print("""
		Where would you like to move?
                        use wasd to move
	""")
        flag = True
        while flag:
	#While Statement waits for an acceptable input to procede
        #gets input from player using WASD format and compares grids to check if the play can move to the desired or not
                flag = input("\n")
                if flag == "w":
                        if yp >= 0 or yp <= y:
                                yp -= 1
                                if grid[yp][xp] == "+": 
                                        sgrid[yp][xp] = "+"
                                        yp += 1
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("The way is blocked!")
                                elif grid[yp][xp] == "M":
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp + 1][xp] = "X"
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("A Monster Appeared!")
                                
                                else:
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp + 1][xp] = "X"
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                        else:
                                print ("You can't go that way")
                elif flag == "s":
                        if yp >= 0 or yp < y:
                                yp += 1
                                if grid[yp][xp] == "+":
                                        sgrid[yp][xp] = "+"
                                        yp -= 1
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("The way is blocked!")
                                elif grid[yp][xp] == "M":
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp - 1][xp] = "X"
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("A Monster Appeared!")
                                else:
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp - 1][xp] = "X"
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                        else:
                                print ("You can't go that way")
                elif flag == "d":
                        if xp >= 0 or xp <= x:
                                xp += 1
                                if grid[yp][xp] == "+":
                                        sgrid[yp][xp] = "+"
                                        xp -= 1
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("The way is blocked!")
                                elif grid[yp][xp] == "M":
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp][xp - 1] = "X"
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("A Monster Appeared!")
                                else:
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp][xp - 1] = "X"
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                        else:
                                print ("You can't go that way")
                                
                elif flag == "a":
                        if xp >= 0 or xp <= x:
                                
                                xp -= 1
                                if grid[yp][xp] == "+":
                                        sgrid[yp][xp] = "+"
                                        xp += 1
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("The way is blocked!")
                                elif grid[yp][xp] == "M":
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp][xp + 1] = "X"
                                        update(grid,yp,xp)
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                                        print("A Monster Appeared!")
                                else:
                                        sgrid[yp][xp] = "O"
                                        sgrid[yp][xp + 1] = "X"
                                        print ("\n" * 60)
                                        for row in sgrid:
                                                print(row)
                        else:
                                print ("You can't go that way")
                elif flag == "":
                        print("\n Not a Valid Option, Try Again \n")

        




def Settings():
	print("""
		What Difficulty Would you Like?

		1. Easy
		2. Medium
		3. Hard
	""")

	flag = True
	while flag:
	#While Statement waits for an acceptable input to procede
		flag = input("\n")
		if flag == "1":
			x = 10
			y = 10
			difficulty = 1
			print ("\n" * 60)
			Generate(x,y,difficulty)
		elif flag == "2":
			x = 15
			y = 15
			difficulty = 2
			print ("\n" * 60)
			Generate(x,y,difficulty)
		elif flag == "3":
			x = 20
			y = 20
			difficulty = 3
			print ("\n" * 60)
			Generate(x,y,difficulty)
		elif flag != "" or flag > 3:
			print("\n Not a Valid Option, Try Again \n")





def menu():
	# menu function thats takes input from the user
	print("""
		1. Play New Game
		2. How to Play
		3. Quit
	""")

	flag = True
	while flag:
	#While Statement waits for an acceptable input to procede
		flag = input("What would you like to do?\n")
		if flag == "1":
			Settings()
			flag = False
		elif flag == "2":
			Tutorial()
			flag = False
		elif flag == "3":
			exit()
		elif flag != "" or flag > 3:
			print("\n Not a Valid Option, Try Again \n")



#def update(grid,yp,xp):

        #updates the game window to show the players enviroment
   
        
        
        
  

def main(x,y):
        #creates a new window and creates a new gameboard to be shown to the player
        xp = 0
        yp = 0
        changey = 50
        changex = 50
        total = x*y
        check = 0


        Xsize = (50 * x) + 40
        Ysize = (50 * y) + 40
        
        win = GraphWin("Python Dungeon Crawler",Xsize,Ysize)
        win.setBackground(color_rgb(65,65,65))


        for i in range(y):
                if i == 0:
                        yp += 20
                else:
                         yp += changey 
                xp = 20
                for j in range(x):
                        TLpt = Point(xp,yp)
                        xp += changex 
                        BRpt = Point(xp, yp + 50)
                        rect = Rectangle(TLpt,BRpt)
                        if check == 0:
                                rect.setFill(color_rgb(153,204,0))
                        elif check == total - 1:
                                rect.setFill(color_rgb(128,0,0))
                        else:
                                rect.setFill(color_rgb(0,0,0))
                        
                        rect.draw(win)
                        check += 1

                        

menu()
