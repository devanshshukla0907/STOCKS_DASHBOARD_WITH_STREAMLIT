# Stock Analysis Dashboard

This project is a Streamlit-based application for analyzing stock data. It provides a comprehensive stock dashboard, including pricing data, fundamental data, top news, and technical analysis using various indicators.

## Features

- **Stock Dashboard**: View the adjusted closing price of the selected stock over a specified date range.
- **Pricing Data**: Analyze returns, annual return, standard deviation, and risk-adjusted return.
- **Fundamental Data**: Display the balance sheet, income statement, and cash flow statement using Alpha Vantage API.
- **Top News**: Fetch and display the latest news articles related to the selected stock with sentiment analysis.
- **Technical Analysis**: Apply technical indicators to the stock data and visualize the results.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/devanshshukla0907/stock-analysis-dashboard.git
    cd stock-analysis-dashboard
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

## Dependencies

- `streamlit`
- `pandas`
- `numpy`
- `yfinance`
- `plotly`
- `alpha_vantage`
- `stocknews`
- `pandas_ta`

## Project Structure

- `app.py`: Main application file containing the Streamlit code.
- `README.md`: Project documentation.
- `requirements.txt`: List of required Python packages.

## How to Use

1. **Stock Dashboard**:
   - Enter the stock ticker in the sidebar.
   - Select the start and end dates.
   - View the adjusted closing price chart.

2. **Pricing Data**:
   - Check the pricing data and various metrics like annual return and standard deviation.

3. **Fundamental Data**:
   - View the balance sheet, income statement, and cash flow statement of the selected stock.

4. **Top News**:
   - Read the latest news articles related to the selected stock with sentiment analysis.

5. **Technical Analysis**:
   - Select a technical indicator from the dropdown menu.
   - View the chart with the selected indicator applied to the stock data.

## API Keys

This project requires an API key from Alpha Vantage to fetch fundamental data. Obtain your API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and replace the placeholder in the code with your key:

```python
key = 'YOUR_ALPHA_VANTAGE_API_KEY'
```





## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
Streamlit   

Alpha Vantage   

Yahoo Finance   

Plotly   


## Contributing
Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any questions or suggestions, please contact devanshshukla0907@gmail.com.
