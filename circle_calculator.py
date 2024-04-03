"""
Datum: 06-03-2024
Programmeur: Joost van Assenbergh
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from math import pi
from tkinter import ttk

class CircleScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create the widgets for the Cirkel screen
        self.label = ttk.Label(self, text="Cirkel Rekentool")
        self.label.pack(pady=10)
        
        self.radius_label = ttk.Label(self, text="Straal:")
        self.radius_label.pack()
        
        self.radius_entry = ttk.Entry(self)
        self.radius_entry.pack()
        
        self.calculate_button = ttk.Button(self, text="Bereken", command=self.calculate_area)
        self.calculate_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()
        
    def calculate_area(self):
        # Get the radius from the entry widget
        radius_length = float(self.radius_entry.get())
        
        # Calculate the area of the square
        area = pi * radius_length**2
        
        # Display the result
        self.result_label.config(text=f"Area: {area:.2f}")