# scraper.py

import time
import json

def mock_score_project(description, tags):
    score = 0
    text = description.lower() + " " + " ".join(tags).lower()
    if "carbon" in text:
        score += 30
    if "token" in text or "tokenization" in text:
        score += 25
    if "regenerative" in text:
        score += 20
    if "open" in text or "transparent" in text:
        score += 10
    if "web3" in text:
        score += 5
    return min(score, 100)

sample_projects = [
    {
        "name": "Regen Network",
        "description": "Tokenizing ecological state and building the economic infrastructure to support regenerative land stewardship.",
        "tags": ["ReFi", "Carbon", "Blockchain"]
    },
    {
        "name": "Open Forest Protocol",
        "description": "A scalable, open, and transparent MRV solution to accelerate nature-based carbon projects.",
        "tags": ["Forestry", "Carbon MRV", "Web3"]
    },
    {
        "name": "Toucan Protocol",
        "description": "Building public infrastructure to bring carbon markets on-chain and support a regenerative economy.",
        "tags": ["Carbon Market", "Tokenization", "Public Goods"]
    },
    {
        "name": "KlimaDAO",
        "description": "A protocol to accelerate the price of carbon by creating strong demand through tokenized assets.",
        "tags": ["Carbon", "DeFi", "Climate"]
    },
    {
        "name": "Solid World DAO",
        "description": "Building pre-financing infrastructure for high-integrity carbon projects using Web3 rails.",
        "tags": ["Carbon", "Web3", "DAO"]
    },
    {
        "name": "Flowcarbon",
        "description": "Tokenizing nature-based carbon credits to increase liquidity and transparency in climate finance.",
        "tags": ["Carbon Credits", "Tokenization", "Climate Finance"]
    }
]

def main():
    results = []
    for project in sample_projects:
        print(f"Scoring {project['name']}...")
        score = mock_score_project(project['description'], project['tags'])
        project['investment_score'] = score
        results.append(project)
        time.sleep(0.5)

    with open("scored_projects.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nCompleted scoring. Results saved to scored_projects.json")

if __name__ == "__main__":
    main()
