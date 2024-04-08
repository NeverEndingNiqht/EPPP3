"""
Datum: 06-03-2024
Programmeur: Joost van Assenbergh
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from math import pi
from tkinter import ttk

class CircleScreen(tk.Frame):
    """
    A class representing the CircleScreen widget.
    """

    def __init__(self, parent) -> None:
        """
        Initializes the CircleScreen class.
        :param parent: The parent widget.
        :return: None
        """

        super().__init__(parent)
        
        # Create the widgets for the Cirkel screen
        self.label: ttk.Label = ttk.Label(self, text="Cirkel Rekentool")
        self.label.pack(pady=10)
        
        self.radius_label: ttk.Label = ttk.Label(self, text="Straal:")
        self.radius_label.pack()
        
        self.radius_entry: ttk.Label = ttk.Entry(self)
        self.radius_entry.pack()
        
        self.calculate_button: ttk.Label = ttk.Button(self, text="Bereken", command=self.calculate_area)
        self.calculate_button.pack(pady=10)
        
        self.result_label: ttk.Label = ttk.Label(self, text="")
        self.result_label.pack()
        
    def calculate_area(self) -> None:
        """
        Calculates the area of a circle based on the entered radius.
        :return: None
        """
        
        # Get the radius from the entry widget
        radius_length: float = float(self.radius_entry.get())
        
        # Calculate the area of the square
        area: float = pi * radius_length**2
        
        # Display the result
        self.result_label.config(text=f"Area: {area:.2f}")