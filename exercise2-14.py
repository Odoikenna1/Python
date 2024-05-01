heart_rate_beats_per_minute = 220
current_year = int(input("What is the current year? "))
birth_year = int(input("What is the birth year? "))
age_in_years = current_year - birth_year

print(f"Your expected maximum heart rate is { heart_rate_beats_per_minute - age_in_years}")