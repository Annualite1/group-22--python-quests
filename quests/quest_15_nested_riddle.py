direction = input("Enter the direction you are going, Left/Right: ").lower()
if direction == "left":
	can_swim = input ("Can you swim?, choose Yes or No: ").lower()
	if can_swim == "yes": print ("You made the right choices, you found the treasure!")
	else: print ("You chose that you can not swim, you lost the treasure")
else: print ("Ooops, You chose a wrong direction, you lost") 

