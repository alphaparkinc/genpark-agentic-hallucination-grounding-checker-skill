import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgenticHallucinationGroundingCheckerClient

def main():
    client = AgenticHallucinationGroundingCheckerClient()
    res = client.verify_grounding_claims()
    print("=== Agentic Hallucination Grounding Checker Output ===")
    print(f"Grounding Ratio: {res['grounding_ratio']*100}% ({res['grounded_claims_count']}/{res['total_claims_evaluated']} Claims Grounded)")
    print(f"Hallucination Free: {res['hallucination_free_verdict']} (Confidence: {res['confidence_score']})")
    print("\nClaim Attribution Breakdown:")
    for c in res['evaluated_claims']:
        print(f"  - [{'GROUNDED' if c['grounded'] else 'HALLUCINATED'}] {c['claim']}")

if __name__ == '__main__':
    main()
