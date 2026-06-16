import matplotlib.pyplot as plt
players = ["Ronaldo","Messi","Mbappe","Haaland","Neymar.jr"]
goals = [5,7,6,4,8]

plt.bar(players,goals)
plt.title("Fifa Goals")
plt.xlabel("players")
plt.ylabel("Players")
plt.show()
matches = [1,2,3,4,5]
goals = [2,1,3,0,4]

plt.plot(matches.goals)
plt.show()

plt.pie([40,35,25],lable = ["messi","mane","neil"])
plt.show()