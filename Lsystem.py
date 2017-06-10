from Turtle import *


class Lsystem:
    def __init__(self, variable, rules, axioms):
        self.variable = variable
        self.rules = rules
        self.axioms = axioms
        self.turtle = Turtle()

    def draw(self, depth, fileName):
        expandedVariable = self.variable
        for i in range(depth):
            for rule in self.rules:
                expandedVariable = expandedVariable.replace(rule, self.rules[rule])
                
        for axiom in expandedVariable:
            if axiom in self.axioms:
                exec("self.turtle." + self.axioms[axiom])
        self.turtle.draw(fileName)
