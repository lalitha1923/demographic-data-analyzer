from demographic_data_analyzer import calculate_demographic_data
import test_module

# Run the analysis and print results
if __name__ == "__main__":
    result = calculate_demographic_data()

    print("Race Count:\n", result['race_count'])
    print("Average Age of Men:", result['average_age_men'])
    print("Percentage with Bachelor's Degrees:", result['percentage_bachelors'])
    print("Higher Education Rich (%):", result['higher_education_rich'])
    print("Lower Education Rich (%):", result['lower_education_rich'])
    print("Minimum Work Hours:", result['min_work_hours'])
    print("Rich Percentage Among Min Workers:", result['rich_percentage'])
    print("Highest Earning Country:", result['highest_earning_country'])
    print("Highest Country Rich (%):", result['highest_earning_country_percentage'])
    print("Top Occupation in India for >50K:", result['top_IN_occupation'])