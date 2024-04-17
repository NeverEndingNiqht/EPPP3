"""
20-03-2024
Lucas de Jongh
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from tkinter import ttk

class SquareScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Maak de widgets voor het Vierkant scherm
        self.label = ttk.Label(self, text="Vierkant Rekentool")
        self.label.pack(pady=10)
        
        self.side_label = ttk.Label(self, text="Lengte zijde in vierkante meter:")
        self.side_label.pack()
        

        self.entry_frame = tk.Frame(self)
        self.entry_frame.pack(pady=10)

        self.side_entry = ttk.Entry(self.entry_frame)
        self.side_entry.pack(side=tk.LEFT)

        self.unit_label = ttk.Label(self.entry_frame, text="m")
        self.unit_label.pack(side=tk.LEFT)


        self.calculate_button = ttk.Button(self, text="Bereken", command=self.calculate_area)
        self.calculate_button.pack(pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()
        
    def calculate_area(self):
        # Haal de lengte van de zijde op uit het invoerveld
        side_length = float(self.side_entry.get())
        
        # Bereken het oppervlak van het vierkant
        area = side_length ** 2
        
        # Toon het resultaat
        self.result_label.config(text=f"Area: {area} m²" )
