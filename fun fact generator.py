import random

def get_fun_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Octopuses have three hearts and blue blood.",
        "A group of flamingos is called a 'flamboyance.'",
        "Wombat poop is cube-shaped. This unique shape prevents it from rolling away and helps mark their territory.",
        "Bananas are berries, but strawberries aren't.",
        "There are more stars in the universe than grains of sand on all the Earth's beaches.",
        "A day on Venus is longer than a year on Venus. Venus rotates very slowly on its axis, taking about 243 Earth days to complete one rotation, while it only takes about 225 Earth days to orbit the Sun.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "Humans share about 60% of their DNA with bananas.",
        "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of iron in the heat."
    ]
    
    return random.choice(facts)

if __name__ == "__main__":
    print("Here's a fun fact for you:")
    print(get_fun_fact())
