"""
This program generates passages that are generated in mad-lib format
Author: GA
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "The Mad Libs game is starting now!"

name = raw_input("Please enter a name: ")
adj1 = raw_input("Please enter an adjective: ")
adj2 = raw_input("Please enter another adjective: ")
adj3 = raw_input("Please enter one last adjective: ")

verb = raw_input("Now enter a verb: ")

noun1 = raw_input("Please type a noun: ")
noun2 = raw_input("Another noun, please: ")

animal = raw_input("Please name... an animal: ")
food = raw_input("Some food: ")
fruit = raw_input("A fruit: ")
sh = raw_input("A superhero: ")
country = raw_input("A country: ")
dessert = raw_input("A dessert: ")
year = raw_input("A year: ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, sh, name, country, name, dessert, name, year, noun2)


















