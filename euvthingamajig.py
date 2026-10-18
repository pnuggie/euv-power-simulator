import matplotlib.pyplot as poop

# questions
while True:
    try:
        euvpower = float(input("how many watts should the EUV power be? realistically around 600–1000W but you can choose whatever: "))
        break
    except ValueError:
        print("buddy, that is text. can you multiply text? (i am ignoring crazy things like algebra.)")

while True:
    try:
        reflectivity = float(input("what % is the reflectivity of each mirror? realistically they'd be different, but this is a simplified version: "))
        if 0 <= reflectivity <= 100:
            break
        print("that would not work. can you choose a number between 0 and 100?")
    except ValueError:
        print("buddy, that is text. can you multiply text? (i am ignoring crazy things like algebra.)")

while True:
    try:
        noofmirrors = int(input("how many mirrors should there be? "))
        if noofmirrors >= 0:
            break
        print("i dont believe thats possible...try again.")
    except ValueError:
        print("im glad youve discovered how to make fractions of a mirror. sadly, we cannot use fractions of a mirror. try again")

# now its graphing time!

# fixed: was []
noofmirrorslist = [0] # records power before any mirrors have absorbed their bit of the light
euvpowerlist = [euvpower] # to start with og power (below)

currentpower = euvpower

# calculate the power after each mirror/the maths section
for mirror in range(noofmirrors):
    currentpower = currentpower * (reflectivity / 100)

    noofmirrorslist.append(mirror + 1) 
    euvpowerlist.append(currentpower) 

# get final answer
result = euvpowerlist[-1] 

print(f"{result:.6f} watts is the total EUV output. yay!")

# create the graph
poop.plot(noofmirrorslist, euvpowerlist, marker="p")
poop.xlabel("number of mirrors")
poop.ylabel("remaining EUV power (W)")
poop.title("overall euv powerloss through mirrors")
poop.grid(False)
poop.text( 
    0.10, 0.95, 
    f"{result:.6f} watts is the total EUV output after everything. yay!",
    transform=poop.gca().transAxes,
    verticalalignment="top"
)

poop.show()
