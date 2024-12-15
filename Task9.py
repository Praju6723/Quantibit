from statistics import mean, median, mode, StatisticsError

def calculate_stats(data):
    
    if not data:
        return "Data is empty, cannot calculate stats"
    
    mean_value = mean(data)
    
    median_value = median(data)
    
    try:
        mode_value = mode(data)  
    except StatisticsError:
        mode_value = "No unique mode" 
    
    return mean_value, median_value, mode_value


data = [1, 2, 2, 3, 4]

mean_value, median_value, mode_value = calculate_stats(data)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
