# market.py
import random
import math

class MarketSystem:
    """
    The MarketSystem class handles AI-driven market trends,
    predicts reptile sales price, and simulates auctions and expos.

    In a full implementation, machine learning models would be integrated
    to forecast market fluctuations and analyze historical data.
    """

    def __init__(self):
        # Base market multiplier (influences all sales prices)
        self.base_trend = 1.0
        # Volatility determines the potential swing per update
        self.volatility = 0.1
        # History of multiplier values (could be used to train ML models)
        self.history = []
        # Initialize the market trend 
        self.update_market_trends()

    def update_market_trends(self):
        """
        Updates current market multiplier.
        
        This method simulates machine learning predictions by applying
        a random change within a defined volatility range. In a real
        system, this would be replaced by predictions from an ML model.
        """
        trend_change = random.uniform(-self.volatility, self.volatility)
        self.base_trend += trend_change 

        # Clamp the multiplier to stay within reasonable limits (e.g., 0.5x to 2.0x)
        self.base_trend = max (0.5, min(self.base_trend, 2.0))
        self.history.append(self.base_trend)
        return self.base_trend
    
    def predict_sale_price(self, reptile):
        """
        Predicts the sale price for a given reptile factoring in current market trends.

        :param reptile: An instance of the Reptile class.
        :return: Final auction price as a float.
        """
        starting_price = reptile.calculate_value()
        current_bid = starting_price
        rounds = random.randint(3, 11) # Number of bidding rounds

        for _ in range(rounds):
            # Each round increases the bid by a percentage of the starting price
            bid_increase = random.uniform(0.05, 1.1) * starting_price
            current_bid += bid_increase * self.base_trend

        return round(current_bid, 2)
    
    def run_expo(self):
        """
        Simulates an expo event that can affect the market.

        Expo outcomes can include:
          - "rare_discovery": Rare morph discoveries temporarily boost market prices.
          - "market_boost": General positive expo causing market drops.
          - "market_drop": A disappointing expo event causing market drops.
          - "none": No significant effect.
        The expo event adjusts the market multiplier accordingly.
        :return: A string message describing the expo event outcome. 
        """
        expo_effect = random.choice(["rare_discovery", "market_boost", "market_drop", "none"])
        if expo_effect == "rare discovery":
            self.base_trend *= 1.2
            effect_message = "Rare morph discovery! Market prices have increased"
        elif expo_effect == "market_boost":
            self.base_trend *= 1.1
            effect_message = "Expo success! General market boost."
        elif expo_effect == "Market drop":
            self.base_trend *= 0.9
            effect_message = "Expo disappointment. Market prices dropped."
        else:
            effect_message = "Expo held with no significant market effect."

        # Clamp the multiplier again to enforce limits
        self.base_trend = max(0.5, min(self.base_trend, 2.0))
        self.history.append(self.base_trend)
        return effect_message
    # Example usage and testing of MarketSystem (for standalone testing)
    if __name__ == "__main__":
        # For demonstration purposes, import a reptile instance from reptile.py
        from reptile import Reptile

        # Create a test reptile (normally created via breeding or shop purchase)
        test_reptile = Reptile(name="TestBallPython", sex="Male", morphs=["Pastel"], hets=["Pied"])

        # Initialize the market system 
        market = MarketSystem()
        print("Initial market trend multiplier:", market.base_trend)

        # Predict sale price based on the current market trend
        predicted_price = market.predict_sale_price(test_reptile)
        print("Predicted sale price for reptile:", predicted_price)

        # Simulate an auction event
        auction_price = market.run_auction(test_reptile)
        print("Auction final price for reptile:", auction_price)

        # Simulate an expo event
        expo_outcome = market.run_expo()
        print("Expo event outcome:", expo_outcome)

        # Update market trends and show the new multiplier
        updated_trend = market.update_market_trends()
        print("Updated markettrend multiplier:", updated_trend)
