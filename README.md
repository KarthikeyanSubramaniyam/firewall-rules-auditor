# Firewall Rules Auditor

Portable, read-only review of exported firewall rules. It identifies internet-wide access, unrestricted administrative ports, and undocumented rules. It never connects to or changes a firewall.

```powershell
python auditor.py examples/rules.json
```

Created 2026-10-02. Validate findings with the platform owner before changing production policy.
