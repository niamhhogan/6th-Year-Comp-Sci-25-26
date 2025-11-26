"""
Population Projection vs Agent Model
------------------------------------

This program runs TWO different types of population models:

1) Projection model (formula-based)
   - Uses birth, death and migration RATES
   - Calculates the new population with a formula each year
   - Gives the SAME result every time (no randomness)

2) Agent model (individual-based)
   - Treats each 1,000 people as one 'agent'
   - Each agent can die, leave, have a baby or be joined by someone new
   - Uses RANDOM chance, so the result changes each time you run it

Both models use the SAME starting population and SAME rates
so you can compare the difference between them.
"""

import random
import matplotlib.pyplot as plt

print("Population Projection Model vs Agent Model")
print("-------------------------------------------")
print("Two models will run using the same inputs:")
print("1) Projection model (smooth, formula-based)")
print("2) Agent model (random, individual-based)")
print()

# =========================
#        INPUTS
# =========================

start_pop_thousands = int(input("Starting population (in thousands, e.g. 500 for 500,000)? "))
num_years = int(input("How many years do you want to model? "))

print("\nEnter yearly rates (per 1000 people).")
death_rate = float(input("Death rate per 1000 people per year: "))
birth_rate = float(input("Birth rate per 1000 people per year: "))
migration_rate = float(input("Net migration rate per 1000 people per year (positive = more arriving, negative = more leaving): "))

# Rates for the projection model
death_rate_per_thousand = death_rate
birth_rate_per_thousand = birth_rate
migration_rate_per_thousand = migration_rate

# For the agent model, convert these to probabilities.
# Example: 10 per 1000 = 0.01 chance per agent.
death_prob = max(death_rate / 1000, 0)
birth_prob = max(birth_rate / 1000, 0)

# Migration rules:
# Positive migration = extra people arriving
# Negative migration = people leaving
if migration_rate >= 0:
    immigration_prob = migration_rate / 1000
    emigration_prob = 0
else:
    immigration_prob = 0
    emigration_prob = abs(migration_rate) / 1000

# =========================
#      MODEL SETUP
# =========================

years = list(range(num_years + 1))

# ----- Projection model -----
projection_pop = [0] * (num_years + 1)
projection_pop[0] = start_pop_thousands

# ----- Agent model -----
# Each "agent" represents 1,000 people
agents = [1] * start_pop_thousands
agent_pop = [len(agents)]

print("\n=== YEAR 0 ===")
print("Projection model population:", projection_pop[0], "thousand")
print("Agent model population:     ", agent_pop[0], "thousand")

# =========================
#        MAIN LOOP
# =========================

for year in range(1, num_years + 1):

    # ======================================
    # 1) PROJECTION MODEL
    # Formula-based model
    # ======================================
    # This model changes the population using a formula:
    #
    # new_population = old_population
    #                 + births
    #                 - deaths
    #                 + migration
    #
    # It always gives the same answer if inputs stay the same.

    old_pop = projection_pop[year - 1]

    net_rate = (-death_rate_per_thousand +
                 birth_rate_per_thousand +
                 migration_rate_per_thousand)

    new_pop = old_pop + old_pop * (net_rate / 1000)
    projection_pop[year] = new_pop

    # ======================================
    # 2) AGENT MODEL
    # Individual-based model
    # ======================================
    # In this model we treat each 1,000 people as an 'agent'.
    # For each agent we decide:
    # - Do they die?
    # - Do they emigrate?
    # - Do they stay?
    # - Do they have a baby (new agent)?
    # - Does an immigrant arrive (extra agent)?
    #
    # Because these events use RANDOM CHANCE,
    # the population changes differently every time you run the program.

    new_agents = []

    for agent in agents:

        # Chance of death
        if random.random() < death_prob:
            continue

        # Chance of emigration (leaving the country)
        if random.random() < emigration_prob:
            continue

        # Agent survives and stays in the population
        new_agents.append(1)

        # Chance of having a baby
        if random.random() < birth_prob:
            new_agents.append(1)

        # Chance of immigration (new person arriving)
        if random.random() < immigration_prob:
            new_agents.append(1)

    agents = new_agents
    agent_pop.append(len(agents))

    print(f"\n=== YEAR {year} ===")
    print("Projection model:", round(projection_pop[year], 2), "thousand")
    print("Agent model:     ", agent_pop[year], "thousand")

# =========================
#        SUMMARY
# =========================

print("\n==================== SUMMARY ====================")
print("Final projection model population:",
      round(projection_pop[-1], 2), "thousand")
print("Final agent model population:",
      agent_pop[-1], "thousand")
print("Note: The agent model changes every time because it is random.\n")

# =========================
#        GRAPH
# =========================

plt.plot(years, projection_pop, label="Projection model (smooth line)")
plt.plot(years, agent_pop, marker='o', linestyle='--',
         label="Agent model (bumpy line)")

plt.title("Comparison: Projection Model vs Agent Model")
plt.xlabel("Year")
plt.ylabel("Population (thousands)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
