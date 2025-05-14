def predict_congestion(vehicle_count, time_of_day):
    if vehicle_count > 80 and time_of_day in ['morning', 'evening']:
        return "High"
    elif vehicle_count > 50:
        return "Moderate"
    else:
        return "Low"
