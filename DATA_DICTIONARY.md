Country Name
Type: text
Unit: none
Definition: Country name as written by WDI.
Caveats: Egypt is written "Egypt, Arab Rep." and contains a comma. Use Country Code as the key.

Country Code
Type: text
Unit: none
Definition: Three-letter World Bank country code.
Caveats: none
Year
Type: integer
Unit: calendar year
Definition: Year of observation, 2000 to 2022.
Caveats: The raw file goes to 2024, but 2023 and 2024 were dropped because health expenditure and skilled births are empty in those years.

Mortality rate
Type: number
Unit: per 1,000 live birthsDefinition: Probability that a newborn baby will die before reaching age five, given the age-specific mortality rates of that year.
Source: UN Inter-agency Group for Child Mortality Estimation (UN IGME).
Missing: 0 of 506 rows.
Caveats: Modelled estimate, not a survey count. The series is smooth, so years within a country are strongly related.

GDP per capita PPP
Type: number
Unit: constant 2021 international dollars
Definition: Gross domestic product per person, converted with purchasing power parities and expressed in constant prices.
Source: WDI.
Missing: 0 of 506 rows.
Caveats: The reference year (2021) can change in later WDI releases and revise old values. Yemen was removed because all 25 years were missing.

Current health expenditure
Type: number
Unit: % of GDP
Definition: Current health expenditure as a percentage of GDP, including healthcare goods and services consumed during the year.
Source: World Bank WDI.
Missing: 2 of 506 rows 
Caveats: Does not include capital health expenditure such as buildings, machinery, IT and stocks of vaccines. Empty for all countries in 2024.

Basic sanitation services
Type: number
Unit: % of population
Definition: People using at least basic sanitation services.
Source: World Bank WDI.
Missing: 0 of 506 rows.
Caveats: none

Basic drinking water services
Type: number
Unit: % of population
Definition: People using at least basic drinking water services.
Source: World Bank WDI.
Missing: 0 of 506 rows.
Caveats: none recorded.

Measles immunization
Type: number
Unit: % of children ages 12-23 months
Definition: Share of children aged 12 to 23 months who received measles immunization.
Source: World Bank WDI.
Missing: 0 of 506 rows.
Caveats: none recorded.

Fertility rate
Type: number
Unit: births per woman
Definition: Total fertility rate.
Source: World Bank WDI.
Missing: 0 of 506 rows.
Caveats: none recorded.

Births attended by skilled health staff
Type: number
Unit: % of total births
Definition: Share of births attended by skilled health staff.
Source: World Bank WDI.
Missing: 293 of 506 rows (57.9%).
Caveats: Most missing variable, and the gaps are clustered in some countries. 19 cells in the raw file are exactly 100.0, which looks like a natural ceiling. Empty for all countries in 2023 and 2024.

Primary completion rate, female
Type: number
Unit: % of relevant age group
Definition: Number of new entrants in the last grade of primary education, regardless of age, divided by the population at the entrance age for that grade.
Source: World Bank WDI.
Missing: 182 of 506 rows (36.0%).
Caveats: Gaps are clustered in some countries (for example Afghanistan and Kenya). Values above 100 are allowed by the definition and were not capped (maximum 124.4 in the raw file). The rate is an upper estimate of true completion because final-year dropouts are not adjusted for.

Urban population
Type: number
Unit: % of total population
Definition: Share of the population living in urban areas.
Source: World Bank WDI.
Missing: 0 of 506 rows.
Caveats: none recorded.

Population, total
Type: number
Unit: number of people
Definition: Total population.
Source: World Bank WDI.
Missing: 0 of 506 rows.
Caveats: none recorded.

Life expectancy at birth
Type: number
Unit: years
Definition: Life expectancy at birth, total.
Source: World Bank WDI.
Missing: 0 of 506 rows.
Caveats: Closely related to under-5 mortality, so it overlaps with the outcome and should not be used as a predictor without care.

Female labour force participation
Type: number
Unit: % of female population ages 15+
Definition: Female labour force participation rate (modeled ILO estimate).
Source: World Bank WDI
Missing: 0 of 506 rows.
Caveats: Modeled estimate, not a direct count.
