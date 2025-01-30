import streamlit as st
import pandas as pd
from data_processor import DataProcessor
from visualizations import (
    create_cost_comparison_chart,
    create_accommodation_comparison,
    create_cost_breakdown_pie,
    create_seasonal_trend
)
from budget_calculator import BudgetCalculator

# Page configuration
st.set_page_config(
    page_title="Europe Travel Budget Planner",
    page_icon="🌍",
    layout="wide"
)

# Initialize session state
if 'data_processor' not in st.session_state:
    st.session_state.data_processor = DataProcessor('attached_assets/Tourist_Travel_Europe.csv')

# Title and introduction
st.title("🌍 Europe Travel Budget Planner")
st.write("""
Plan your European adventure with our data-driven budget calculator! 
Enter your travel preferences below to get personalized cost estimates and insights.
""")

# Create sidebar for inputs
with st.sidebar:
    st.header("Travel Preferences")
    
    # Country and city selection
    country = st.selectbox(
        "Select Country",
        st.session_state.data_processor.get_unique_countries()
    )
    
    cities = st.session_state.data_processor.get_cities_for_country(country)
    city = st.selectbox("Select City", cities)
    
    # Travel details
    days = st.number_input("Number of Days", min_value=1, max_value=30, value=7)
    companions = st.number_input("Number of Travelers", min_value=1, max_value=10, value=2)
    
    # Accommodation preference
    accommodation = st.selectbox(
        "Preferred Accommodation",
        st.session_state.data_processor.get_accommodation_types()
    )
    
    # Season selection
    season = st.selectbox(
        "Travel Season",
        ["Spring", "Summer", "Fall", "Winter"]
    )

# Main content area
col1, col2 = st.columns(2)

with col1:
    # Calculate and display cost estimates
    costs = st.session_state.data_processor.calculate_average_costs(
        country, city, accommodation
    )
    
    if costs['avg_cost_per_day'] > 0:
        season_multiplier = BudgetCalculator.get_season_multiplier(season)
        total_budget, cost_breakdown = BudgetCalculator.calculate_total_budget(
            costs['avg_cost_per_day'],
            days,
            companions,
            season_multiplier
        )
        
        st.header("Estimated Budget")
        st.metric(
            "Total Budget",
            f"€{total_budget:,.2f}",
            f"€{total_budget/days/companions:,.2f} per person/day"
        )
        
        # Cost breakdown visualization
        st.plotly_chart(
            create_cost_breakdown_pie(cost_breakdown),
            use_container_width=True
        )
    else:
        st.error("No data available for the selected combination. Please try different options.")

with col2:
    # Transport mode comparison
    transport_costs = st.session_state.data_processor.get_transport_mode_costs(country, city)
    st.plotly_chart(
        create_cost_comparison_chart(transport_costs),
        use_container_width=True
    )
    
    # Accommodation comparison
    accommodation_costs = st.session_state.data_processor.get_accommodation_costs(country, city)
    st.plotly_chart(
        create_accommodation_comparison(accommodation_costs),
        use_container_width=True
    )

# Seasonal trends
st.header("Seasonal Cost Trends")
st.plotly_chart(
    create_seasonal_trend(st.session_state.data_processor.df, country, city),
    use_container_width=True
)

# Travel tips and insights
st.header("💡 Travel Tips")
tips_col1, tips_col2 = st.columns(2)

with tips_col1:
    st.subheader("Save on Transportation")
    cheapest_transport = min(transport_costs.items(), key=lambda x: x[1])
    st.write(f"✓ Consider traveling by {cheapest_transport[0]} to save money")
    st.write("✓ Book transportation in advance for better rates")
    st.write("✓ Look for rail passes if planning multiple city visits")

with tips_col2:
    st.subheader("Accommodation Savings")
    cheapest_accommodation = min(accommodation_costs.items(), key=lambda x: x[1])
    st.write(f"✓ {cheapest_accommodation[0]} offers the best value in {city}")
    st.write("✓ Book accommodations outside the city center")
    st.write("✓ Consider longer stays for potential discounts")

# Footer
st.markdown("---")
st.markdown("""
<small>Data-driven insights based on real travel expenses. Prices may vary based on current market conditions.</small>
""", unsafe_allow_html=True)
