Cleaning Log 

Cleaning entries 
1. The Data sheet has 304 rows, but the last rows are not data. Only 299 rows have a Country Code, which equals 23 countries x 13 series. only rows with a Country Code are kept, so 5 rows were removed.
2. All 25 year columns were read as text (object type) because WDI writes ".." for a missing value. replaced them with NaN and converted the columns to numbers 
3. Yemen's GDP per capita is missing for all 25 years, while the other 22 countries have complete GDP-removed Yemen completely, which leaves Pakistan plus 21 peers
4.. The raw file covers 2000 to 2024. Current health expenditure is missing for all 23 countries in 2024, and skilled birth attendance is missing for all 23 countries in 2023 and 2024 so both years are removed 
5. The raw file has one row per country and series, with one column per year-reshaped it so that one row is one country-year with one column per series, giving 506 rows and 16 columns and switched to pivot, which keeps only existing combinations and fails if a country-year appears twice
6. The missing cells are concentrated in some countries: for female completion, Afghanistan and Kenya are missing 20 of 25 years while Cambodia and Uzbekistan are missing 1. Filling or interpolating would invent data exactly where the gaps are-left them as NaN and will decide in the modelling stage which variables to use
7. The maximum is 124.4, and 53 cells in the raw file are above 100, mostly in Indonesia (12), Nepal (9), Bhutan (8) and Viet Nam (5). The metadata says this rate can exceed 100% because the numerator includes late entrants and repeaters while the denominator is only the children at the entrance age. So the values follow the definition and are not errors
8. Skilled birth attendance not dropped, and values at exactly 100 kept (not changed)
9. Country names kept as they are (not changed) 

Missing: found 
Duplicates: not found
Wrong Types: found
Wrong units: not found
Encoding: not found
drift: not checked
