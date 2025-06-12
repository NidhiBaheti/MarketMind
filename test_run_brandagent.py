from agents.brand_agent import BrandAgent
import time

def test_endurastride_campaigns(rounds=5):
    brand = BrandAgent(name="EnduraStride")

    for i in range(rounds):
        print(f"\n🧢 [Campaign {i+1}] USP Focus: {brand.profile['usps'][0]}")
        caption = brand.generate_campaign()
        print(f"📣 Generated Caption: {caption}")

        # Optional: cycle USP manually to test prompt variety
        if i % 2 == 1:
            brand.cycle_usp()

        time.sleep(1)  # Add delay to avoid huggingface rate limits (if needed)

    print("\n📊 Final Summary:", brand.summary())

if __name__ == "__main__":
    test_endurastride_campaigns()