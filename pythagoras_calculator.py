"""
Datum: 26-03-2024
Programmeur: Wouter Jorna
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from math import sqrt
from tkinter import ttk

class PythagorasScreen(tk.Frame):
    """
    A class representing the PythagorasScreen widget.
    """

    def __init__(self, parent) -> None:
        """
        Initializes the PythagorasScreen class.
        :param parent: The parent widget.
        :return: None
        """

        super().__init__(parent)
        
        # Create and configure the widgets for the Pythagoras screen
        self.label: ttk.Label = ttk.Label(self, text="Pythagoras Rekentool")
        self.label.pack(pady=10)

        # Add more widgets and functionality as needed
        
        self.side_a_label: ttk.Label = ttk.Label(self, text="Lengte zijde A:")
        self.side_a_entry: ttk.Entry = ttk.Entry(self)
        self.side_a_label.pack()
        self.side_a_entry.pack()

        self.side_b_label: ttk.Label = ttk.Label(self, text="Lengte zijde B:")
        self.side_b_entry: ttk.Entry = ttk.Entry(self)
        self.side_b_label.pack()
        self.side_b_entry.pack()

        self.calculate_button: ttk.Button = ttk.Button(self, text="Bereken", command=self.calculate_side_c)
        self.calculate_button.pack(pady=10)

        self.result_label: ttk.Label = ttk.Label(self, text="")
        self.result_label.pack()

        # Pack the widgets
        self.pack()

    def calculate_side_c(self) -> None:
        """
        Calculates the length of side C based on the lengths of sides A and B, according to the pythagorean theorem.
        :return: None
        """
        
        side_a: float = float(self.side_a_entry.get())
        side_b: float = float(self.side_b_entry.get())
        side_c: float = sqrt(side_a**2 + side_b**2)
        self.result_label.config(text=f"De lengte van zijde C is {side_c:.2f}.")