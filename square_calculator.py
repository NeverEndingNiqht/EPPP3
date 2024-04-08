"""
20-03-2024
Programmeur: Lucas de Jongh
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from tkinter import ttk

class SquareScreen(tk.Frame):
    """
    A class representing the SquareScreen widget.
    """
    
    def __init__(self, parent) -> None:
        """
        Initializes the SquareScreen class.
        :param parent: The parent widget.
        :return: None
        """

        super().__init__(parent)
        
        # Maak de widgets voor het Vierkant scherm
        self.label: ttk.Label = ttk.Label(self, text="Vierkant Rekentool")
        self.label.pack(pady=10)
        
        self.side_label: ttk.Label = ttk.Label(self, text="Lengte zijde:")
        self.side_label.pack()
        
        self.side_entry: ttk.Label = ttk.Entry(self)
        self.side_entry.pack()
        
        self.calculate_button: ttk.Label = ttk.Button(self, text="Bereken", command=self.calculate_area)
        self.calculate_button.pack(pady=10)
        
        self.result_label: ttk.Label = ttk.Label(self, text="")
        self.result_label.pack()
        
    def calculate_area(self) -> None:
        """
        Haalt de lengte van de zijde op uit het invoerveld en berekent het oppervlak van het vierkant.
        :return: None
        """

        # Haal de lengte van de zijde op uit het invoerveld
        side_length: float = float(self.side_entry.get())
        
        # Bereken het oppervlak van het vierkant
        area: float = side_length ** 2
        
        # Toon het resultaat
        self.result_label.config(text=f"Area: {area}")