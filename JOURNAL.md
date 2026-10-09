Before We Looked
We downloaded the WDI Excel file and opened it. We saw that it has data for 2000 to 2024, rows for each country and variable, and some missing values. We did not count anything or compare any values.
1. We predicted Pakistan’s under-5 mortality in 2022 would be higher than both Bangladesh’s and Sri Lanka’s, and the gap with Sri Lanka would be larger than the gap with Bangladesh, because Sri Lanka has a much stronger health system.
2. We predicted that Pakistan's GDP per capita would be lower than India's in most recent years, because the two countries have experienced different patterns of economic growth and income development.
3. We predicted that female primary completion rate would have one of the highest proportions of missing values in the dataset, potentially exceeding 20% of country-year observations, because education indicators may not be reported consistently across all countries and years.

What We Did
We started with a proposal on predicting persistent high poverty. We could not understand how to justify the poverty threshold, so we checked the World Bank poverty data for our countries. We found a lot of missing values and very few data points per country, which would have made a reliable classification model hard to build. Because of this, we dropped that topic and switched to under-5 mortality in Pakistan compared with peer countries, which is an outcome with complete data in WDI.
We set up the GitHub repo, which took several attempts: our first push failed because we had not made a commit yet, and our repo name was different from the one we had typed in the commands. We wrote three predictions and committed them before running any counts, after opening the WDI Excel file only to look at its general layout. Then we copied the raw file into `data/raw`. Our first copy command failed because the file name had brackets and spaces, not underscores.
In Colab we looked at the structure: 2 sheets, 304 rows, footer lines, ".." for missing values, and 13 series for 23 countries. We counted missing values, duplicates, wrong types and out-of-range values, and read the metadata for definitions and licence. We wrote `clean.py`. Our first version produced 11,132 rows instead of the expected 506, because `pivot_table` with `dropna=False` created every combination of country name, code and year. We replaced it with `pivot` and got 506 rows. Then we made four charts.

What Surprised Us
Skilled birth attendance had the most missing values (62.3% in the raw file), which we did not predict, and it was missing for all 23 countries in 2023 and 2024. We checked this by counting missing cells by country and by year. We expected GDP and health expenditure to be fine, and both had 4.3% missing, but for different reasons: GDP is missing only for Yemen (all 25 years), while health expenditure is missing for all countries in 2024 plus Afghanistan in 2000 and 2001.
Female primary completion goes up to 124.4, which looked impossible. We checked the metadata and found that the definition can exceed 100% because of late entrants and repeaters, so we did not change it (53 cells). Skilled births has 19 cells exactly at 100.0, which is a natural ceiling.

What We Revised
Topic:Before, we planned to predict whether a country stays in high poverty, using a poverty-headcount threshold. When we checked the poverty data, we found many missing values and few data points, so we could not defend the threshold or build a model on it. We changed to a continuous outcome, under-5 mortality, which has 0% missing values in our file.
Countries: Before, we had 23 countries. Yemen's GDP is missing for all 25 years and our baseline needs GDP, so we removed it and now have 22 countries.
Timeframe: Before, we planned to use 2000 to 2022. The file goes to 2024, but health expenditure and skilled births are empty in the last years, so we kept 2000 to 2022.
Variables: Before, we had 10 predictors. The file also has life expectancy, skilled births and female primary completion.
Missing values: We assumed missing values might be spread out. The data showed they cluster in specific countries, so we decided not to fill them in.

What We Still Don't Trust
National averages hide differences inside Pakistan.
The peers are very different from Pakistan (Sri Lanka 6.3 vs Pakistan 59.7), and we chose them without a formal criterion, so the gap could change with a different list.