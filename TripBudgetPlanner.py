class TripBudgetPlanner:
    def __init__(self):
        # Predefined data for average daily cost at different destinations.
        # This is a simple example, you can extend it with more destinations and data.
        self.destinations_data = {
            'Paris': 150,
            'New York': 200,
            'Tokyo': 120,
            'Bangkok': 70,
            'London': 180
        }

    def get_cost_per_day(self, destination):
        """Get the average cost per day for the given destination."""
        return self.destinations_data.get(destination, None)

    def calculate_budget(self, destination, budget, days):
        """Calculate whether the user has enough budget for the destination."""
        cost_per_day = self.get_cost_per_day(destination)
        
        if cost_per_day is None:
            return f"Sorry, we don't have data for {destination}. Please try another destination."
        
        total_cost = cost_per_day * days
        difference = budget - total_cost
        
        if difference > 0:
            return (f"Your budget is sufficient! Total cost for {days} days in {destination} is ${total_cost}. "
                    f"You have ${difference} extra.")
        elif difference < 0:
            return (f"Your budget is insufficient. Total cost for {days} days in {destination} is ${total_cost}. "
                    f"You need ${-difference} more.")
        else:
            return f"Your budget is exactly enough! Total cost for {days} days in {destination} is ${total_cost}."


def main():
    trip_planner = TripBudgetPlanner()
    
    # User input for destination, budget and days of stay
    destination = input("Enter your destination: ").strip()
    budget = float(input("Enter your budget: ").strip())
    days = int(input("Enter the number of days you plan to stay: ").strip())
    
    result = trip_planner.calculate_budget(destination, budget, days)
    print(result)


if __name__ == "__main__":
    main()
