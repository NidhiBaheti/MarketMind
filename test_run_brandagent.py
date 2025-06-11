from agents.brand_agent import BrandAgent
import random

brand = BrandAgent(name="AirFlex", strategy="neutral")

# Simulate 10 campaign rounds
for step in range(10):
    message = brand.generate_campaign()
    print(f"\n[Round {step+1}] Campaign: {message}")

    # Simulated feedback (randomized for testing)
    score = random.uniform(0.3, 1.0)
    print(f"Simulated feedback score: {round(score, 2)}")

    brand.receive_feedback(score)

print("\nFinal Agent Summary:", brand.summary())