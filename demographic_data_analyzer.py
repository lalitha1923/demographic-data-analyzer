import pandas as pd

def calculate_demographic_data():
    # Load data
    df = pd.read_csv(r"C:\Users\aliet\Documents\DataScienceProjects\demographic-data-analyzer\adult.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education
    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_edu]['salary'] == '>50K').mean() * 100, 1)

    # 5. Non-advanced education
    lower_education = ~advanced_edu
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. Minimum hours worked
    min_work_hours = df['hours-per-week'].min()

    # 7. Rich among minimum hour workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. Country with highest % of >50K earners
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary = country_salary.fillna(0)
    highest_earning_country = country_salary['>50K'].idxmax()
    highest_earning_country_percentage = round(country_salary['>50K'].max() * 100, 1)

    # 9. Top occupation in India for >50K earners
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }