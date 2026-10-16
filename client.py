"""
Bloomreach-inspired AI Semantic E-Commerce Search & Merchandising Reranker (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
import re
import math
from typing import Dict, Any, List, Optional

class BloomreachAISemanticMerchandisingReranker:
    SYNONYM_DICT = {
        "sneakers": ["shoes", "trainers", "kicks", "footwear"],
        "dress": ["frock", "gown", "apparel"],
        "hoodie": ["sweatshirt", "pullover", "jacket"],
        "cheap": ["budget", "affordable", "discount"],
        "luxury": ["premium", "designer", "high-end"]
    }

    def __init__(self, engine_name: str = "GenPark-Bloomreach-Discovery-Core"):
        self.engine_name = engine_name

    def expand_query_intent(self, query: str) -> Dict[str, Any]:
        tokens = re.findall(r"\w+", query.lower())
        expanded = set(tokens)
        for t in tokens:
            if t in self.SYNONYM_DICT:
                expanded.update(self.SYNONYM_DICT[t])
                
        price_intent = "NORMAL"
        if any(w in tokens for w in ["cheap", "budget", "discount"]):
            price_intent = "LOW_PRICE"
        elif any(w in tokens for w in ["luxury", "premium", "expensive"]):
            price_intent = "HIGH_PRICE"
            
        return {
            "original_query": query,
            "tokens": tokens,
            "expanded_tokens": list(expanded),
            "price_intent": price_intent
        }

    def compute_product_score(self, item: Dict[str, Any], query_intent: Dict[str, Any], rules: Dict[str, Any]) -> float:
        expanded_tokens = query_intent["expanded_tokens"]
        title_words = set(re.findall(r"\w+", item.get("title", "").lower()))
        tag_words = set(re.findall(r"\w+", " ".join(item.get("tags", [])).lower()))
        all_product_words = title_words | tag_words | {item.get("category", "").lower()}
        
        # 1. Semantic match score
        matches = sum(1 for t in expanded_tokens if t in all_product_words)
        relevance = matches / max(1, len(query_intent["tokens"]))
        
        # 2. Stock availability penalty
        stock = int(item.get("stock", 10))
        stock_factor = 1.0 if stock > 0 else 0.1
        
        # 3. Commercial profitability boost (Margin & Revenue)
        margin = float(item.get("margin_rate", 0.30))
        commercial_boost = 1.0 + (0.5 * margin)
        
        # 4. Merchandising boost & bury rules
        boost_cats = rules.get("boost_categories", [])
        bury_cats = rules.get("bury_categories", [])
        rule_multiplier = 1.0
        if item.get("category") in boost_cats:
            rule_multiplier *= 1.4
        if item.get("category") in bury_cats:
            rule_multiplier *= 0.5
            
        total_score = (relevance * 0.5 + 0.1) * stock_factor * commercial_boost * rule_multiplier
        return round(total_score, 4)

    def rerank_catalog(self, query: str, catalog_items: List[Dict[str, Any]], merchandising_rules: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        rules = merchandising_rules or {}
        query_intent = self.expand_query_intent(query)
        
        ranked_products = []
        for p in catalog_items:
            score = self.compute_product_score(p, query_intent, rules)
            ranked_products.append({**p, "discovery_score": score})
            
        ranked_products.sort(key=lambda x: x["discovery_score"], reverse=True)
        
        return {
            "engine": self.engine_name,
            "query": query,
            "intent_analysis": query_intent,
            "total_candidates": len(catalog_items),
            "results_count": len(ranked_products),
            "top_products": ranked_products[:10],
            "merchandising_verdict": "OPTIMIZED_RELEVANCE_WITH_MARGIN_LIFT"
        }
