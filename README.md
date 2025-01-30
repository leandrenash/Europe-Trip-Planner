# 🌍 Europe Travel Budget Planner

A data-driven web application that helps travelers plan their European adventures by providing accurate budget estimates based on real travel data.

![Europe Travel Budget Planner](generated-icon.png)

## 🎯 Features

- **Smart Budget Calculator**
  - Estimates total trip cost based on historical data
  - Breaks down expenses by category (accommodation, transport, food, activities)
  - Adjusts estimates based on season and travel preferences

- **Interactive Visualizations**
  - Cost comparison across different transportation modes
  - Accommodation price analysis
  - Seasonal price trends
  - Expense breakdown pie charts

- **Travel Insights**
  - Cost-saving recommendations
  - Best time to visit suggestions
  - Transportation mode comparisons
  - Accommodation type analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/europe-travel-budget-planner.git
cd europe-travel-budget-planner
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

The application will be available at `http://localhost:5000`.

## 📊 Data Structure

The application uses a comprehensive travel dataset (`Tourist_Travel_Europe.csv`) with the following key fields:

- `Country_Visited`: European country
- `City_Visited`: Specific city
- `Mode_of_Travel`: Transportation method
- `Travel_Duration_Days`: Length of stay
- `Number_of_Companions`: Group size
- `Total_Travel_Cost`: Total trip cost
- `Accommodation_Type`: Type of lodging
- `Season_of_Visit`: Travel season

## 🛠️ Technology Stack

- **Backend Framework**: Python with Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Data Source**: Real travel expense dataset

## 📖 Usage Guide

1. Select your desired destination country and city from the sidebar
2. Enter your travel details:
   - Number of days
   - Number of travelers
   - Preferred accommodation type
   - Travel season
3. View the generated budget estimate and cost breakdown
4. Explore different visualizations for deeper insights
5. Check travel tips for cost-saving opportunities

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Travel data sourced from real European travel expenses
- Built with Streamlit's amazing framework
- Inspired by the need for data-driven travel planning

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/europe-travel-budget-planner](https://github.com/yourusername/europe-travel-budget-planner)
