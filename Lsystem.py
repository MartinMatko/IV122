from Turtle import *


class Lsystem:
    def __init__(self, variable, rules, axioms):
        self.variable = variable
        self.rules = rules
        self.axioms = axioms
        self.expanded = self.variable
        self.turtle = Turtle()

    def expand(self, depth):
        for i in range(depth):
            for rule in self.rules:
                self.expanded = self.expanded.replace(rule, self.rules[rule])

    def draw(self, depth, fileName):
        self.expand(depth)
        for i in self.expanded:
            if i in self.axioms:
                exec("self.turtle." + self.axioms[i])
        self.turtle.draw(fileName)
