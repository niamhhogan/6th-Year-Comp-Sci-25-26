import matplotlib.pyplot as plt
import random

print("📈 YouTube Views Prediction Model")
print("This program estimates how a video will gain views over time based on growth factors and chance of going viral.")

# User inputs
initial_views = int(input("Enter initial views on Day 0: "))
base_growth_rate = float(input("Enter average daily growth rate as a % (e.g. 15 for 15%): "))
engagement_level = input("What is the viewer engagement? (low / medium / high): ").lower()
chance_of_virality = int(input("Enter chance of going viral (0 to 100%): "))
days = int(input("How many days do you want to model? "))

# Engagement multiplier
engagement_effect = {
    "low": 1.0,
    "medium": 1.2,
    "high": 1.5
}

growth_multiplier = engagement_effect.get(engagement_level, 1.0)

# Tracking data
view_counts = [initial_views]
day_labels = [0]

viral_triggered = False

for day in range(1, days + 1):
    previous_views = view_counts[-1]

    # Viral boost (one-time)
    if not viral_triggered and random.randint(1, 100) <= chance_of_virality:
        print(f"🔥 Video went viral on Day {day}!")
        growth_rate = base_growth_rate * 3  # viral spike
        viral_triggered = True
    else:
        growth_rate = base_growth_rate

    # Apply growth and engagement multiplier
    new_views = previous_views * (1 + (growth_rate / 100) * growth_multiplier)

    # Add slight randomness to simulate real-world variation
    new_views *= random.uniform(0.95, 1.05)

    view_counts.append(int(new_views))
    day_labels.append(day)

    print(f"Day {day}: {int(new_views)} views")

# Plot
plt.plot(day_labels, view_counts, marker='o')
plt.title("Projected YouTube Video Views Over Time")
plt.xlabel("Day")
plt.ylabel("Views")
plt.grid(True)
plt.show()
