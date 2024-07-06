import random
characters = ["princess", "dragon", "knight", "wizard", "king"]
settings = ["castle", "forest", "mountain", "village", "cave"]
plots = ["quest", "battle", "puzzle", "romance", "mystery"]
happened = ["made a lot of friends","finds an apple", "found a secret key", "solved a mistery", "wrote a book"]
print('Once up on a time'+random.choice(settings)+","+'there was a'+random.choice(characters)+"."+'The'+random.choice(characters)+'was on a '+random.choice(plots)+"."+'The'+random.choice(characters)+" "+random.choice(happened))