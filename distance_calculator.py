"""
Datum: 24-03-2024
Programmeur: Luca ten Have
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from tkinter import ttk

class DistanceScreen(tk.Frame):
    """
    A class representing the DistanceScreen widget.
    """

    def __init__(self, parent) -> None:
        """
        Initializes the DistanceScreen class.
        :param parent: The parent widget.
        :return: None
        """

        super().__init__(parent)
        
        # Create and configure the widgets for the Afstand screen
        self.label: ttk.Label = ttk.Label(self, text="Afstand Rekentool")
        self.label.pack(pady=10)

        # Add more widgets and functionality as needed
        self.distance_label: ttk.Label = ttk.Label(self, text="Afstand (in km):")
        self.distance_entry: ttk.Entry = ttk.Entry(self)
        self.distance_label.pack()
        self.distance_entry.pack()

        self.speed_label: ttk.Label = ttk.Label(self, text="Snelheid (in km/h):")
        self.speed_entry: ttk.Entry = ttk.Entry(self)
        self.speed_label.pack()
        self.speed_entry.pack()

        self.calculate_button: ttk.Button = ttk.Button(self, text="Bereken", command=self.calculate_time)
        self.calculate_button.pack(pady=10)

        self.result_label: ttk.Label = ttk.Label(self, text="")
        self.result_label.pack()

        # Pack the widgets
        self.pack()

    def calculate_time(self) -> None:
        """
        Calculates the time it takes to travel a certain distance at a certain speed.
        :return: None
        """
        
        distance: float = float(self.distance_entry.get())
        speed: float = float(self.speed_entry.get())
        time: float = distance / speed
        self.result_label.config(text=f"Je bent {time:.2f} uur onderweg.")