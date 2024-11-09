def alpha_inserts(countries, country):
    countries.append(country)


countries = ['Australia', 'Cuba', 'Senegal']

alpha_inserts(countries, 'Brazil')

print(', '.join(countries))  # Outputs "Australia, Brazil, Cuba, Senegal"
alpha_inserts(['Brazil'], 'Australia')