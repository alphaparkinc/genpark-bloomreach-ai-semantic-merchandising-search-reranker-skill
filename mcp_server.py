#!/usr/bin/env python3
import json
import sys
from client import BloomreachAISemanticMerchandisingReranker

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        reranker = BloomreachAISemanticMerchandisingReranker()
        catalog = [
            {"id": "p1", "title": "White Runner Trainers", "category": "Footwear", "price": 120.0, "margin_rate": 0.45, "stock": 15, "tags": ["sneakers", "running"]},
            {"id": "p2", "title": "Vintage Leather Boots", "category": "Footwear", "price": 250.0, "margin_rate": 0.30, "stock": 0, "tags": ["boots", "leather"]},
            {"id": "p3", "title": "Everyday Cotton Tee", "category": "Apparel", "price": 35.0, "margin_rate": 0.50, "stock": 50, "tags": ["t-shirt", "basic"]}
        ]
        res = reranker.rerank_catalog("comfortable sneakers", catalog, {"boost_categories": ["Footwear"]})
        assert res["results_count"] == 3
        assert res["top_products"][0]["id"] == "p1"
        print(f"[TEST PASS] Bloomreach Reranker Passed! Top Pick: {res['top_products'][0]['title']}")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-bloomreach-reranker", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "rerank_catalog", "description": "Bloomreach semantic e-commerce search and merchandising reranker"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                reranker = BloomreachAISemanticMerchandisingReranker()
                out = reranker.rerank_catalog(args.get("query", ""), args.get("catalog_items", []), args.get("merchandising_rules", {}))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
