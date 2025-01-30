import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Dict

def create_cost_comparison_chart(transport_costs: Dict[str, float]) -> go.Figure:
    """Create bar chart comparing transport costs"""
    fig = px.bar(
        x=list(transport_costs.keys()),
        y=list(transport_costs.values()),
        title="Average Daily Cost by Transport Mode",
        labels={'x': 'Transport Mode', 'y': 'Average Cost per Day (€)'}
    )
    fig.update_layout(showlegend=False)
    return fig

def create_accommodation_comparison(accommodation_costs: Dict[str, float]) -> go.Figure:
    """Create bar chart comparing accommodation costs"""
    fig = px.bar(
        x=list(accommodation_costs.keys()),
        y=list(accommodation_costs.values()),
        title="Average Daily Cost by Accommodation Type",
        labels={'x': 'Accommodation Type', 'y': 'Average Cost per Day (€)'}
    )
    fig.update_layout(showlegend=False)
    return fig

def create_cost_breakdown_pie(cost_components: Dict[str, float]) -> go.Figure:
    """Create pie chart showing cost breakdown"""
    fig = px.pie(
        values=list(cost_components.values()),
        names=list(cost_components.keys()),
        title="Estimated Cost Breakdown"
    )
    return fig

def create_seasonal_trend(df: pd.DataFrame, country: str, city: str) -> go.Figure:
    """Create line chart showing seasonal cost trends"""
    mask = (df['Country_Visited'] == country) & (df['City_Visited'] == city)
    seasonal_data = df[mask].groupby('Season_of_Visit')['Cost_Per_Person_Day'].mean()
    
    # Ensure seasons are in chronological order
    season_order = ['Winter', 'Spring', 'Summer', 'Fall']
    seasonal_data = seasonal_data.reindex(season_order)
    
    fig = px.line(
        x=seasonal_data.index,
        y=seasonal_data.values,
        title="Average Daily Cost by Season",
        labels={'x': 'Season', 'y': 'Average Cost per Day (€)'}
    )
    return fig
