"""
20-03-2024
Programmeur: Lucas de Jongh
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from tkinter import ttk

class SquareScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create the widgets for the Vierkant screen
        self.label = ttk.Label(self, text="Vierkant Rekentool")
        self.label.pack(pady=10)
        
        self.side_label = ttk.Label(self, text="Lengte zijde:")
        self.side_label.pack()
        
        self.side_entry = ttk.Entry(self)
        self.side_entry.pack()
        
        self.calculate_button = ttk.Button(self, text="Bereken", command=self.calculate_area)
        self.calculate_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()
        
    def calculate_area(self):
        # Get the side length from the entry widget
        side_length = float(self.side_entry.get())
        
        # Calculate the area of the square
        area = side_length ** 2
        
        # Display the result
        self.result_label.config(text=f"Area: {area}")