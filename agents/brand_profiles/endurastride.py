# agents/profiles/endurastride_profile.py

def get_profile():
    return {
        "name": "EnduraStride",
        "vision": (
            "To empower everyday athletes with footwear that blends rugged performance, "
            "modern style, and affordability—elevating both workouts and daily hustle."
        ),
        "mission": (
            "Make high-quality sports shoes accessible to every fitness enthusiast "
            "through durability, design, and direct-to-consumer pricing."
        ),
        "core_values": {
            "Durability": "Reinforced stitching, abrasion-resistant outsoles, resilient cushioning.",
            "Aesthetic Appeal": "Sleek silhouettes and on-trend colorways from emerging designers.",
            "Affordability": "Streamlined supply chain and direct-to-consumer pricing.",
            "Sustainability": "Recycled materials and a repair-reuse program to reduce waste."
        },
        "usps": [
            "Triple-Guard Durability System",
            "Modular Design Accents",
            "Direct-to-Consumer Value"
        ],
        "target_audience": [
            "Urban Runners & Gym-Goers (18–35)",
            "Weekend Warriors & Casual Athletes (25–50)",
            "Budget-Conscious Shoppers"
        ],
        "tone": "Energetic, encouraging, transparent, trend-savvy but unpretentious",
        "tagline": "Engineered for Life. Styled for You. Priced for All.",
        "origin_story": (
            "Founded by lifelong runners frustrated with shoes that wore out too quickly, "
            "EnduraStride began in a garage. Prototypes were hand-stitched and field-tested "
            "by local athletes. Now scaled through advanced manufacturing, it stays true "
            "to its grassroots ethos."
        ),
        "visual_language": {
            "Logo": "Stylized footprint with a lightning bolt + shield.",
            "Colors": ["Stone Gray", "Forest Green", "Electric Orange", "Deep Teal"],
            "Typography": "Bold, geometric sans-serif fonts symbolizing strength and modernity."
        },
        "prompt_template": """You are a senior brand copywriter for {brand_name}, a sports-shoe brand known for:
- Rugged performance
- Contemporary style
- Wallet-friendly pricing

Your task is to write an Instagram caption (125–150 characters) that:
- Hooks urban runners (18–35)
- Highlights this USP: {usp}
- Uses a motivating, coach-like tone
- Includes 1 emoji, 1 call-to-action, and 2–3 hashtags (must include #EnduraStride)

Format:
\"<hook> <USP mention> <emoji> <CTA> <hashtags>\"

Respond only with the caption text.
"""
    }