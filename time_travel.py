def time_travel(years: list) -> int:
    
    count_years = 0
    
    for i in range(1, len(years)):
        if years[i] == years[i-1]:
            count_years += 0
        elif years[i] > years[i-1]:
            count_years += 1
        else:
            count_years += 2
            
    return count_years