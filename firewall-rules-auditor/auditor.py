"""Audit a portable firewall rule JSON export. No rules are changed."""
import argparse, json

def audit(rules: list[dict]) -> list[dict]:
    findings=[]
    for index, rule in enumerate(rules, 1):
        action=str(rule.get("action", "")).lower(); source=str(rule.get("source", "")); ports=str(rule.get("ports", ""))
        if action == "allow" and (source in {"0.0.0.0/0", "*", "any"} or "any" in source.lower()) and (ports in {"*", "any", "0-65535"}):
            findings.append({"rule":"FRA001","severity":"high","index":index,"message":"Any source can reach all ports."})
        if action == "allow" and ports in {"22", "3389"} and source in {"0.0.0.0/0", "*", "any"}:
            findings.append({"rule":"FRA002","severity":"high","index":index,"message":"Administrative access is open to every source."})
        if not rule.get("description"):
            findings.append({"rule":"FRA003","severity":"low","index":index,"message":"Rule has no owner or purpose description."})
    return findings

def main():
    p=argparse.ArgumentParser(description="Review exported firewall rules without applying changes.");p.add_argument("rules_json");a=p.parse_args()
    with open(a.rules_json, encoding="utf-8") as h: rules=json.load(h)
    findings=audit(rules.get("rules", rules));print(json.dumps({"findings":findings,"finding_count":len(findings)},indent=2));raise SystemExit(1 if findings else 0)
if __name__ == "__main__": main()
