import random
from reptile import Reptile

class BreedingSystem:
    """Handles the breeding mechanics for reptiles."""
    
    def __init__(self):
        # This could be further enhanced with more machine learning logic later
        pass

    def breed(self, female, male):
        """Simulates breeding between two reptiles, producing a clutch of eggs"""

        # Ensure both are valid mates (opposite sex)
        if female.sex == male.sex:
            return "Cannot breed reptiles of the same sex."
        
        clutch_size = random.randint(1, 13) # Random clutch size (1-13)
        offspring = []
        
        for _ in range(clutch_size):
            offspring.append(self.create_offspring(female, male))

        return offspring
    
    def create_offspring(self, female, male):
        """Creates a single offspring with combined genetic traits."""
        offspring_name = f"{female.name} x {male.name} Offspring"

        # Combine morphs (random chance of inheriting from either parent)
        offspring_morphs = self.combine_genes(female.morphs, male.morphs)

        # Combine hets (recessive traits)
        offspring_hets = self.combine_genes(female.morphs, male.morphs)

        # Random Chance of inheriting a dominant morph from each parent
        if random.random() < 0.5:
            offspring_morphs.append(female.morphs[random.randint(0, len(female.morphs) - 1)])

        if random.random() < 0.5:
            offspring_morphs.append(male.morphs[random.randint(0, len(male.morphs) - 1)])

        # Create offspring Reptile object
        offspring = Reptile(
            name=offspring_name,
            sex=random.choice(["Male", "Female"]),
            morphs=offspring_morphs,
            hets=offspring_hets
        )

        return offspring
    
    def combine_genes(self, parent1_genes, parent2_genes):
        """Combines genes from 2 parents (dominant morphs and recessive hets)."""
        combined_genes = list(set(parent1_genes + parent2_genes)) # Unique genes from both parents
        return combined_genes
    
    def calculate_hatchling_value(self, offspring):
        """Calculates the market value of the hatchling based on it's genes."""
        return offspring.calculate_value()
    
    def predict_clutch_outcome(self, female, male):
        """Uses basic machine learning model (future implementation) to predict clutch outcome probabilities."""
        # For now we can simulate a very basic prediction based on gene inheritance
        predicted_morphs = self.combine_genes(female.morphs, male.morphs)
        predicted_value = self.calculate_hatchling_value(offspring=Reptile(female.name + " x " + male.name, "Female", predicted_morphs, [] ))

        # This could be replaced with machine learning models that take genetic probabilities into account
        return {"predicted_morphs": predicted_morphs, "predicted_value": predicted_value}
    
    def display_clutch(self, offspring):
        """Helper function to display the results of a clutch."""
        return [str(child) for child in offspring]
