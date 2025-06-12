from llm.local_inference import LocalLLM

class BrandAgent:
    def __init__(self, profile: dict, llm=None):
        self.name = profile["name"]
        self.profile = profile
        self.llm = llm or LocalLLM()
        self.history = []

    def generate_campaign(self, focus_usp=None):
        usp = focus_usp or self.profile["usps"][0]
        prompt = self.profile["prompt_template"].format(
            brand_name=self.name,
            usp=usp
        )
        caption = self.llm.generate(prompt)
        self.history.append({"caption": caption, "usp": usp})
        return caption

    def cycle_usp(self):
        usps = self.profile["usps"]
        current = self.profile["usps"][0]
        next_index = (usps.index(current) + 1) % len(usps)
        self.profile["usps"][0] = usps[next_index]
        print(f"[{self.name}] USP focus changed to: {usps[next_index]}")

    def summary(self):
        return {
            "brand_name": self.name,
            "tagline": self.profile.get("tagline"),
            "campaigns_run": len(self.history),
            "last_usp": self.history[-1]["usp"] if self.history else None
        }