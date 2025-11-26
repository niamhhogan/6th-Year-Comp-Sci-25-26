import random
import matplotlib.pyplot as plt

print("Simple agent-based population model")
print("Each person is an individual agent.")
print("Each year, every person might die, emigrate, or have a baby.\n")

# --- Inputs ---

start_pop = int(input("Starting population (number of people)? "))
num_years = int(input("How many years do you want to model? "))

# Probabilities as percentages
death_percent = float(input("Chance of death per person per year (in %)? "))
birth_percent = float(input("Chance of having a baby per person per year (in %)? "))
emigrate_percent = float(input("Chance of emigrating per person per year (in %)? "))

death_prob = death_percent / 100
birth_prob = birth_percent / 100
emigrate_prob = emigrate_percent / 100

# --- Set up agents and tracking lists ---

# Represent each person as a simple '1'
population = [1] * start_pop

year_list = [0]
pop_list = [len(population)]

print("\nYear 0: population =", len(population))

# --- Main simulation loop ---

for year in range(1, num_years + 1):
    new_population = []

    for person in population:
        # Person might die
        if random.random() < death_prob:
            continue  # person removed (dies)

        # Person might emigrate
        if random.random() < emigrate_prob:
            continue  # person removed (emigrates)

        # If they are still here, keep them
        new_population.append(1)

        # Person might have a baby
        if random.random() < birth_prob:
            new_population.append(1)  # add a new baby agent

    # Update population for next year
    population = new_population

    # Record stats
    year_list.append(year)
    pop_list.append(len(population))

    print("Year", year, ": population =", len(population))

# --- Summary ---

print("\nSimulation complete.")
print("Starting population:", start_pop)
print("Final population after", num_years, "years:", len(population))

# --- Graphing ---

plt.plot(year_list, pop_list, marker='o')
plt.title("Agent-based population model")
plt.xlabel("Year")
plt.ylabel("Population (number of people)")
plt.grid(True)
plt.show()
