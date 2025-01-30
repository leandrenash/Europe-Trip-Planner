import pandas as pd
import numpy as np
from typing import Dict, List, Tuple

class DataProcessor:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)
        self.process_data()
        
    def process_data(self):
        """Initial data processing and cleaning"""
        # Ensure numeric columns are properly typed
        numeric_cols = ['Travel_Duration_Days', 'Number_of_Companions', 'Total_Travel_Cost']
        self.df[numeric_cols] = self.df[numeric_cols].apply(pd.to_numeric)
        
        # Calculate per person per day cost
        self.df['Cost_Per_Person_Day'] = (
            self.df['Total_Travel_Cost'] / 
            (self.df['Number_of_Companions'] * self.df['Travel_Duration_Days'])
        )

    def get_unique_countries(self) -> List[str]:
        """Get list of unique countries"""
        return sorted(self.df['Country_Visited'].unique())

    def get_cities_for_country(self, country: str) -> List[str]:
        """Get cities for a specific country"""
        return sorted(self.df[self.df['Country_Visited'] == country]['City_Visited'].unique())

    def get_accommodation_types(self) -> List[str]:
        """Get unique accommodation types"""
        return sorted(self.df['Accommodation_Type'].unique())

    def get_travel_modes(self) -> List[str]:
        """Get unique travel modes"""
        return sorted(self.df['Mode_of_Travel'].unique())

    def calculate_average_costs(self, 
                              country: str, 
                              city: str, 
                              accommodation: str) -> Dict[str, float]:
        """Calculate average costs for given parameters"""
        mask = (
            (self.df['Country_Visited'] == country) &
            (self.df['City_Visited'] == city) &
            (self.df['Accommodation_Type'] == accommodation)
        )
        filtered_df = self.df[mask]
        
        if len(filtered_df) == 0:
            return {
                'avg_cost_per_day': 0,
                'min_cost': 0,
                'max_cost': 0,
                'median_cost': 0
            }
            
        return {
            'avg_cost_per_day': filtered_df['Cost_Per_Person_Day'].mean(),
            'min_cost': filtered_df['Cost_Per_Person_Day'].min(),
            'max_cost': filtered_df['Cost_Per_Person_Day'].max(),
            'median_cost': filtered_df['Cost_Per_Person_Day'].median()
        }

    def get_transport_mode_costs(self, 
                               country: str, 
                               city: str) -> Dict[str, float]:
        """Get average costs by transport mode"""
        mask = (
            (self.df['Country_Visited'] == country) &
            (self.df['City_Visited'] == city)
        )
        return self.df[mask].groupby('Mode_of_Travel')['Cost_Per_Person_Day'].mean().to_dict()

    def get_accommodation_costs(self, 
                              country: str, 
                              city: str) -> Dict[str, float]:
        """Get average costs by accommodation type"""
        mask = (
            (self.df['Country_Visited'] == country) &
            (self.df['City_Visited'] == city)
        )
        return self.df[mask].groupby('Accommodation_Type')['Cost_Per_Person_Day'].mean().to_dict()
