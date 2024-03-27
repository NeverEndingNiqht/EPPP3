"""
Datum: 26-03-2024
Programmeur: Wouter Jorna
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from math import sqrt
from tkinter import ttk

class PythagorasScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create and configure the widgets for the Pythagoras screen
        self.label = ttk.Label(self, text="Pythagoras Rekentool")
        self.label.pack()

        # Add more widgets and functionality as needed
        
        self.side_a_label = ttk.Label(self, text="Lengte zijde A:")
        self.side_a_entry = ttk.Entry(self)
        self.side_a_label.pack()
        self.side_a_entry.pack()

        self.side_b_label = ttk.Label(self, text="Lengte zijde B:")
        self.side_b_entry = ttk.Entry(self)
        self.side_b_label.pack()
        self.side_b_entry.pack()

        self.calculate_button = ttk.Button(self, text="Bereken", command=self.calculate_side_c)
        self.calculate_button.pack()

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()

        # Pack the widgets
        self.pack()

    def calculate_side_c(self):
        side_a = float(self.side_a_entry.get())
        side_b = float(self.side_b_entry.get())
        side_c = sqrt(side_a**2 + side_b**2)
        self.result_label.config(text=f"De lengte van zijde C is {side_c:.2f}.")