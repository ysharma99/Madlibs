from sample_madlibs import dog , fairytale, vampires 
import random

#three stories that are a randomly generated and picked 
if __name__ == "__main__":
    m = random.choice([dog,fairytale,vampires])
    m.madlib()