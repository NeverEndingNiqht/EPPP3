"""
Datum: 06-03-2024
Programmeur: Joost van Assenbergh
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import distance_calculator as distance
import tax_calculator as tax
import circle_calculator as circle
import square_calculator as square
import pythagoras_calculator as pythagoras

import tkinter as tk
from tkinter import ttk

# Start the main event loop
class RekentoolApp:
    def __init__(self):
        self.window = tk.Tk()  # Define the "window" variable
        self.window.title("Rekentool")
        self.window.geometry("300x200")

        # Create a notebook widget to hold the screens
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create the screens
        self.distance_screen = distance.DistanceScreen(self.notebook)
        self.tax_screen = tax.TaxScreen(self.notebook)
        self.circle_screen = circle.CircleScreen(self.notebook)
        self.square_screen = square.SquareScreen(self.notebook)
        self.pythagoras_screen = pythagoras.PythagorasScreen(self.notebook)

        # Add the screens to the notebook
        self.notebook.add(self.distance_screen, text="Afstand")
        self.notebook.add(self.tax_screen, text="BTW")
        self.notebook.add(self.circle_screen, text="Cirkel")
        self.notebook.add(self._screen, text="Vierkant")
        self.notebook.add(self.pythagoras_screen, text="Pythagoras")

    def run(self):
        # Start the main event loop
        self.window.mainloop()

# Create an instance of the RekentoolApp class
window = RekentoolApp()
window.run()