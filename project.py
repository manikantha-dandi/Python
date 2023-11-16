import pandas as pd
import matplotlib.pyplot as plt

def main():
    olympic_data = load_data()
    
    display_data_head(olympic_data)
    # Plotting using Matplotlib
    # Call your analysis functions
    line_plot_participation_over_years(olympic_data)
    bar_plot_total_medals_by_country(olympic_data)
    comparison_of_medals_across_years(olympic_data)
    bar_plot_medals_distribution_in_year(olympic_data, 2020)
    scatter_plot_rank_vs_total_medals(olympic_data)
    stacked_bar_plot_total_medals_distribution(olympic_data)
    # Adding more functions
    plot_medals_over_years(olympic_data)
    print("Top 4 countries performed well in 2008 are :")
    print(get_top_countries(olympic_data, 2008, 4))
    pie_chart_category_wise_medals_all_years(olympic_data, 'India')
    

def load_data():
    # Load your dataset
    # Assuming the dataset is stored in a CSV file named 'olympic_statistics_modified.csv'
    # You may need to adjust the file name/path accordingly
    return pd.read_csv('F:\\python_pro\\olympic_statistics_modified.csv')

def display_data_head(dataframe):
    print(dataframe.head())



def bar_plot_medals_distribution_in_year(dataframe, selected_year):
    selected_year_data = dataframe[dataframe['Year'] == selected_year]

    if 'Country' in selected_year_data.columns:
        medals_data = selected_year_data[['Country', 'Gold', 'Silver', 'Bronze']]
        medals_data.plot(x='Country', kind='bar', stacked=True, figsize=(12, 6))
        plt.title(f'Medals Distribution in {int(selected_year)}')
        plt.xlabel('Country')
        plt.ylabel('Number of Medals')
        plt.legend(title='Medal Type')
        plt.show()
    else:
        print(f"The 'Country' column is not present. Medals Distribution plot skipped.")

def scatter_plot_rank_vs_total_medals(dataframe):
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe['Rank'], dataframe['Total Medals'], c='blue', alpha=0.7)
    plt.title('Scatter Plot: Rank vs Total Medals')
    plt.xlabel('Rank')
    plt.ylabel('Total Medals')
    plt.grid(True)
    plt.show()

def stacked_bar_plot_total_medals_distribution(dataframe):
    medals_data_all_years = dataframe.groupby('Country')[['Gold', 'Silver', 'Bronze']].sum()

    medals_data_all_years.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title('Total Medals Distribution for All Years (Each Country as a Group)')
    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.legend(title='Medal Type')
    plt.show()

def comparison_of_medals_across_years(dataframe):
    medals_by_type = dataframe.groupby('Year')[['Gold', 'Silver', 'Bronze']].sum()

    medals_by_type.plot(kind='line', figsize=(12, 6))
    plt.title('Comparison of Gold, Silver, and Bronze Medals Across Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Medals')
    plt.legend(title='Medal Type')
    plt.grid(True)
    plt.show()

def bar_plot_total_medals_by_country(dataframe):
    total_medals_by_country = dataframe.groupby('Country')['Total Medals'].sum()

    total_medals_by_country.plot(kind='bar', figsize=(12, 6))
    plt.title('Total Medals by Country')
    plt.xlabel('Country')
    plt.ylabel('Total Medals')
    plt.show()

def plot_medals_over_years(data):
    # plot function
    plt.figure(figsize=(10, 6))
    for medal_type in ['Gold', 'Silver', 'Bronze']:
        plt.plot(data['Year'], data[medal_type], label=medal_type)

    plt.title(f'Medals Over Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Medals')
    plt.legend()
    plt.grid(True)
    plt.show()

def get_top_countries(data, year, n):
    # function to get top N countries in a specific year
    year_data = data[data['Year'] == year]
    top_countries = year_data.nlargest(n, 'Total Medals').reset_index(drop=True)
    
    # Convert float columns to integers
    top_countries['Year'] = top_countries['Year'].astype(int)
    top_countries['Total Athletics'] = top_countries['Total Athletics'].astype(int)
    top_countries['Gold'] = top_countries['Gold'].astype(int)
    top_countries['Silver'] = top_countries['Silver'].astype(int)
    top_countries['Bronze'] = top_countries['Bronze'].astype(int)
    top_countries['Total Medals'] = top_countries['Total Medals'].astype(int)
    top_countries['Rank'] = top_countries['Rank'].astype(int)

    return top_countries


def line_plot_participation_over_years(dataframe):
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe['Year'], dataframe['Total Athletics'], marker='o')
    plt.title('Year-wise Participation')
    plt.xlabel('Year')
    plt.ylabel('Total Athletics')
    plt.grid(True)
    plt.show()

def pie_chart_category_wise_medals_all_years(dataframe, country):
    country_data = dataframe[dataframe['Country'] == country]
    if not country_data.empty:
        medals_data = country_data.groupby('Year')[['Gold', 'Silver', 'Bronze']].sum()

        labels = ['Gold', 'Silver', 'Bronze']
        plt.figure(figsize=(10, 6))
        plt.pie(medals_data.sum(axis=0), labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(f'{country} Medals Distribution Across All Years')
        plt.show()
    else:
        print(f"No data available for {country}.")



if __name__ == "__main__":
    main()
