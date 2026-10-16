# genpark-bloomreach-ai-semantic-merchandising-search-reranker-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](https://www.genpark.ai)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

Bloomreach-inspired AI Semantic E-Commerce Search & Merchandising Reranker. Parses customer shopping intent, expands synonyms, applies visual/category boost & bury rules, and balances semantic relevance against gross margin & stock availability.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import BloomreachAISemanticMerchandisingReranker

def main():
    reranker = BloomreachAISemanticMerchandisingReranker()
    catalog = [
        {"id": "p1", "title": "White Runner Trainers", "category": "Footwear", "price": 120.0, "margin_rate": 0.45, "stock": 15, "tags": ["sneakers", "running"]},
        {"id": "p2", "title": "Vintage Leather Boots", "category": "Footwear", "price": 250.0, "margin_rate": 0.30, "stock": 0, "tags": ["boots", "leather"]},
        {"id": "p3", "title": "Merino Wool Pullover", "category": "Apparel", "price": 85.0, "margin_rate": 0.60, "stock": 25, "tags": ["sweater", "hoodie"]}
    ]
    rules = {"boost_categories": ["Footwear"], "bury_categories": ["Apparel"]}
    result = reranker.rerank_catalog("athletic sneakers", catalog, rules)
    print("--- Bloomreach AI Discovery Rerank Output ---")
    print(f"Query: {result['query']} | Intent Tokens: {result['intent_analysis']['expanded_tokens']}")
    for idx, item in enumerate(result['top_products'], 1):
        print(f"{idx}. {item['title']} - Score: {item['discovery_score']} (Stock: {item['stock']}, Margin: {item['margin_rate']})")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
