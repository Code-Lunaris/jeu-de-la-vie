from cellule import cellule
from tkinter import Canvas

class celluleUI():
    
    def __init__(self, cell, can):

        self.cellule = cell

        self.masterCan = can

        self.celSize = self.masterCan.celSize

        self.colors = ["white", "black"]

        self.cellColor = self.colors[self.cellule.state]

        x = self.masterCan.celSize*self.cellule.posLine
        y = self.masterCan.celSize*self.cellule.posColonne
    
        self.rec = self.can.create_rectangle(x, y, x+sell.celSize, y+self.celSize, fill = self.cellColor)
        