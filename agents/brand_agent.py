import random

class BrandAgent:
    def __init__(self, name, strategy="neutral"):
        self.name = name
        self.strategy = strategy
        self.history = []  # List of (campaign_text, engagement_score)

    def generate_campaign(self):
        """
        Generate a basic marketing campaign message.
        Stub LLM generation with strategy-based templates.
        """
        base_messages = {
            "neutral": [
                "Experience unmatched comfort with our new sports shoes!",
                "Step into the future of running.",
                "The perfect blend of style and performance."
            ],
            "emotional": [
                "Every step tells your story. Make it count.",
                "You deserve more than ordinary—wear what empowers you.",
                "Chase your dreams, one step at a time."
            ],
            "discount": [
                "Flash Sale: 30% off all sneakers this weekend!",
                "Buy 1 Get 1 Free—only for 48 hours!",
                "Limited offer: Style that saves you money."
            ]
        }

        message = random.choice(base_messages.get(self.strategy, base_messages["neutral"]))
        return message

    def receive_feedback(self, score):
        """
        Update agent's internal history and evolve strategy.
        score: float (simulated feedback like engagement rate or sentiment)
        """
        if self.history:
            last_campaign = self.history[-1][0]
        else:
            last_campaign = None

        self.history.append((last_campaign, score))

        # Simple evolution rule: switch strategy if avg score < threshold
        if len(self.history) >= 3:
            avg_score = sum(s for _, s in self.history[-3:]) / 3
            if avg_score < 0.5:
                self._mutate_strategy()

    def _mutate_strategy(self):
        """
        Naively switch to a different campaign tone.
        """
        options = ["neutral", "emotional", "discount"]
        options.remove(self.strategy)
        self.strategy = random.choice(options)
        print(f"[{self.name}] Strategy evolved to: {self.strategy}")

    def summary(self):
        return {
            "name": self.name,
            "strategy": self.strategy,
            "campaigns_run": len(self.history)
        }