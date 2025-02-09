import json
import random
import math

class player:
    def __init__(self, username):
        self.username = username 
        self.money = 700 #starting amount
        self.rep = 0 #reputation starts at 0
        self.level = 1
        self.reptiles = [] #List of owned reptiles
        self.inventory = {} #Items from the breeder shop currently in the players inventory
        self.tournament_rank = None #Holds current Tournament Ranking 

    def buy_item(self, item_name, cost): 
        """buy an item from the shop if the player has enough money."""
        if self.money >= cost:
            self.money -= cost
            self.inventory[item_name] = self.inventory.get(item_name, 0) + 1
            return f"Purchased {item_name}!"
        return "Not enough money!"
    
    def sell_reptil(self, reptile, price):
        """sell a reptile and earn reputation based on how many genes it contained, and how much it sold for!"""
        if reptile in self.reptiles:
            self.reptiles.remove(reptile)
            self.money += price
            self.rep += (price * 2) + (12 * reptile.gene_count()) #Calculation of Reputation formula
            return f"Sold {reptile.name} for ${price}!"
        return "Reptile not found"
    
    def check_level_up(self):
        """Increase level when reputation meets the required threshold."""
        next_level_rep = math.ceil(600 * (1.25 ** (self.level - 1))) #125% imcrease per level
        if self.rep >= next_level_rep and self.level < 30:
            self.level += 1 
            return f"Leveled up to {self.level }!"
        return "Not enough rep to level up."
    
    def save_progress(self):
        """Save player progress to a file."""
        data = {
            "username": self.username,
            "money": self.money,
            "rep": self.rep,
            "reptile": [reptile.to_dict() for reptile in self.reptiles],
            "inventory": self.inventory,
            "tournament_rank": self.tournament_rank
        }
        with open(f"{self.username}_save.json", "w") as f:
            json.dump(data, f)

    def load_progress(self):
        """Load player progress progress from a file."""
        try:
            with open(f"{self.username}_save.json", "r") as f:
                data = json.load(f)
                self.money = data["money"]
                self.rep = data["level"]
                self.inventory = data["inventory"]
                self.tournament_rank = data["tournament_rank"]
                # Reconstruct reptiles from saved data
                from reptile import Reptile
                self.reptiles = [Reptile.from_dict(r) for r in data["reptiles"]]
        except FileNotFoundError:
            return "No save file found. Starting fresh."
