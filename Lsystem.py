from Turtle import *


class Lsystem:
    def __init__(self, variable, rules, axioms):
        self.variable = variable
        self.rules = rules
        self.axioms = axioms
        self.turtle = Turtle()

    def draw(self, depth, fileName):
        expanded = self.variable
        for i in range(depth):
            for rule in self.rules:
                expanded = expanded.replace(rule, self.rules[rule])
                
        for i in expanded:
            if i in self.axioms:
                exec("self.turtle." + self.axioms[i])
        self.turtle.draw(fileName)
