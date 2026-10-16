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
