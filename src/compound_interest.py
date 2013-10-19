# FV = PV (1+rate)periods

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    return present_value * (1+rate_per_period) ** periods
    


print future_value(1000, .02, 365, 3) #1061.83480113
print future_value(500, .04, 10, 10) #745.317442824