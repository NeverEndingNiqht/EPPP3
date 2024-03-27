"""
Datum: 24-03-2024
Programmeur: Luca ten Have
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from tkinter import ttk

class DistanceScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create and configure the widgets for the Afstand screen
        self.label = ttk.Label(self, text="Afstand Rekentool")
        self.label.pack()

        # Add more widgets and functionality as needed
        
        self.distance_label = ttk.Label(self, text="Afstand (in km):")
        self.distance_entry = ttk.Entry(self)
        self.distance_label.pack()
        self.distance_entry.pack()

        self.speed_label = ttk.Label(self, text="Snelheid (in km/h):")
        self.speed_entry = ttk.Entry(self)
        self.speed_label.pack()
        self.speed_entry.pack()

        self.calculate_button = ttk.Button(self, text="Bereken", command=self.calculate_time)
        self.calculate_button.pack()

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()

        # Pack the widgets
        self.pack()

    def calculate_time(self):
        distance = float(self.distance_entry.get())
        speed = float(self.speed_entry.get())
        time = distance / speed
        self.result_label.config(text=f"Je bent {time:.2f} uur onderweg.")
