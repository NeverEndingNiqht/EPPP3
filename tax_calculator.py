"""
Datum: 13-03-2024
Programmeur: Floris Barendsen
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from tkinter import ttk

class TaxScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create and configure the widgets
        self.label = ttk.Label(self, text="BTW Rekentool")
        self.label.pack(pady=10)
        
        self.entry = ttk.Entry(self)
        self.entry.pack(pady=5)
        
        self.button = ttk.Button(self, text="Bereken", command=self.calculate_btw)
        self.button.pack(pady=5)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
        
    def calculate_btw(self):
        try:
            amount = float(self.entry.get())
            btw_amount = amount * 0.21
            total_amount = amount + btw_amount
            self.result_label.configure(text=f"BTW: {btw_amount:.2f}, Totaal: {total_amount:.2f}")
        except ValueError:
            self.result_label.configure(text="Ongeldige invoer.")