#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

player_one = [4, 9, 1, 6, 3, 7, 2, 8, 5, 2]
player_two = [5, 3, 7, 2, 6, 4, 9, 1, 8, 3]

player_one_wins = sum(1 for i in range(10) if player_one[i] > player_two[i])
player_two_wins = sum(1 for i in range(10) if player_two[i] > player_one[i])

print("Player One =", player_one)
print("Player Two =", player_two)
print("Player One won", player_one_wins, "times")
print("Player Two won", player_two_wins, "times")
print("Player One's highest number is", max(player_one), "at index", player_one.index(max(player_one)))
print("Player Two's highest number is", max(player_two), "at index", player_two.index(max(player_two)))
print("Player One's lowest number is", min(player_one), "at index", player_one.index(min(player_one)))
print("Player Two's lowest number is", min(player_two), "at index", player_two.index(min(player_two)))


