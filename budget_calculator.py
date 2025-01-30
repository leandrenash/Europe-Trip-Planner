from typing import Dict, Tuple

class BudgetCalculator:
    @staticmethod
    def calculate_total_budget(
        base_cost: float,
        days: int,
        companions: int,
        season_multiplier: float = 1.0
    ) -> Tuple[float, Dict[str, float]]:
        """
        Calculate total budget and cost breakdown
        Returns: (total_cost, cost_breakdown)
        """
        # Base daily cost per person
        daily_cost = base_cost * season_multiplier
        
        # Calculate components
        accommodation_cost = daily_cost * 0.4  # 40% for accommodation
        transport_cost = daily_cost * 0.3      # 30% for transport
        food_cost = daily_cost * 0.2           # 20% for food
        activities_cost = daily_cost * 0.1     # 10% for activities
        
        # Calculate total
        total_cost = daily_cost * days * companions
        
        # Create cost breakdown
        cost_breakdown = {
            "Accommodation": accommodation_cost * days * companions,
            "Transport": transport_cost * days * companions,
            "Food": food_cost * days * companions,
            "Activities": activities_cost * days * companions
        }
        
        return total_cost, cost_breakdown

    @staticmethod
    def get_season_multiplier(season: str) -> float:
        """Get cost multiplier based on season"""
        multipliers = {
            'Summer': 1.2,  # Peak season
            'Winter': 0.8,  # Off season
            'Spring': 1.0,  # Shoulder season
            'Fall': 1.0     # Shoulder season
        }
        return multipliers.get(season, 1.0)
