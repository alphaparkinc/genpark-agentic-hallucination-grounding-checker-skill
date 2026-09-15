import json, sys
from client import AgenticHallucinationGroundingCheckerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "hallucination-grounding-checker", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "verify_grounding_claims", "description": "Verifies factual grounding ratio and detects hallucinations against reference context."}]}}
    elif method == "tools/call":
        client = AgenticHallucinationGroundingCheckerClient()
        res = client.verify_grounding_claims()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AgenticHallucinationGroundingCheckerClient()
        print(json.dumps(client.verify_grounding_claims(), indent=2))
