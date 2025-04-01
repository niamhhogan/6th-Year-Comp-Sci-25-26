import matplotlib.pyplot as plt

print("This program simulates virus spread in a population.")
print("You'll enter starting values for infected people, infection and recovery rates, and simulate how the virus spreads over time.")

# User inputs
population = int(input("Enter total population: "))
initial_infected = int(input("Enter the number of people initially infected: "))
infection_rate = float(input("Enter infection rate per day (e.g. 0.2 for 20%): "))
recovery_rate = float(input("Enter recovery rate per day (e.g. 0.1 for 10%): "))
days = int(input("Enter the number of days to simulate: "))

# Lists to store daily values
infected = [initial_infected]
recovered = [0]
susceptible = [population - initial_infected]

# Simulate day by day
for day in range(days):
    new_infections = min(susceptible[day], infected[day] * infection_rate)
    new_recoveries = infected[day] * recovery_rate

    infected_today = infected[day] + new_infections - new_recoveries
    recovered_today = recovered[day] + new_recoveries
    susceptible_today = population - infected_today - recovered_today

    infected.append(infected_today)
    recovered.append(recovered_today)
    susceptible.append(susceptible_today)

    print(f"Day {day + 1}: Infected = {round(infected_today)}, Recovered = {round(recovered_today)}, Susceptible = {round(susceptible_today)}")

# Plotting the results
days_list = [i for i in range(days + 1)]
plt.plot(days_list, infected, label="Infected")
plt.plot(days_list, recovered, label="Recovered")
plt.plot(days_list, susceptible, label="Susceptible")
plt.xlabel("Days")
plt.ylabel("People")
plt.title("Virus Spread Model")
plt.legend()
plt.grid(True)
plt.show()
