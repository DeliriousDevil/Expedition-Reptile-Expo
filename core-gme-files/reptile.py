import random
import json

class Reptile:
    """"Represents a ball python with genetic traits, morphs, and market value."""

    def __init__(self, name, sex, morphs, hets=None, price=None):
        """ 
        Initialize a reptile with specific genetics.

        :param name: Name of the reptile
        :param sex: "Male" or "Female"
        :param morphs: List of dominant/incomplete dominant morphs (e.g., ["Pastel", "Yellowbelly"])
        :param hets: List of recessive heterozygous traits (e.g., ["Piebald(Pied)", "Clown", "Axanthic", "VPI"]), default None
        :param price: Market price of the reptile, auto-calculated if None
        """
        self.name = name
        self.sex = sex
        self.morphs = morphs
        self.hets = hets if hets else []
        self.price = price if price else self.calculate_value()

    def gene_count(self):
        """Returns the total number of genes (dominant, co-dominant, visual recessive, and het {recessive trait}, genetic mutations)"""
        return len(self.morphs) + len(self.hets)
    
    def calculate_value(self):
        """
        Determines the market value of the reptile using AI-driven trends.
        Base value is influenced by the number of genes and market demand.
        """
        base_price = 50 # Normal ball python price
        gene_multiplier = 1.5 # Price increase per dominant, co-dominant, and incomplete dominant gene
        het_multiplier = 2 # Price increase per visual recessive gene

        price = base_price
        for morph in self.morphs:
            price *= gene_multiplier
        for het in self.hets:
            price *= het_multiplier

        # Add AI-driven price fluctuation (market trends)
        price_variance = random.uniform (0.9, 1.2) # +/- 10-20% variation
        final_price = round(price * price_variance, 2)
        return max(final_price, 50) # Ensure a minimum base value 
    
    def to_dict(self):
        """Converts reptile object from saved dictionary data."""
        return {
            "name": self.name,
            "sex": self.sex,
            "morphs": self.morphs,
            "hets": self.hets,
            "price": self.price
        }
    
    @classmethod
    def from_dict(cls, data):
        """Converts reptile object to a dictionary for saving."""
        return cls(
            name=data["name"],
            sex=data["sex"],
            morphs=data["morphs"],
            hets=data["hets"],
            price=data["price"]
        )
    
    def __str__(self):
        morphs_str = ", ".join(self.morphs) if self.morphs else "Normal"
        hets_str = f" (Het: {', '.json(self.hets)})" if self.hets else ""
        return f"{self.name} ({self.sex}) - {morphs_str}{hets_str} - ${self.price}"
