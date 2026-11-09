# Network & Host Firewall Rule Risk Auditor

<p align="center">
  <img src="https://img.shields.io/badge/Security-Defensive_Auditor-blue?style=flat" alt="Type">
  <img src="https://img.shields.io/badge/Status-Architectural_Showcase-success?style=flat" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
</p>

> 🔒 **Technical Showcase & Architecture Specification**  
> *This repository provides public architectural documentation, system specifications, and implementation summaries. Full production source code, internal test suites, and proprietary algorithms are maintained in a secure private repository.*

---

## 📌 Executive Summary

**Category**: Network Security & Perimeter Defense  
**Tech Stack**: `Python 3.10+ · Network Security · Firewall Auditing · Rule Optimization`  

Defensive auditor analyzing firewall rule tables to flag overly permissive rules, risky administrative port exposures, and shadowed rule entries.

---

## 🎯 The Problem It Solves

Over years of operation, firewall rule bases accumulate thousands of rules. Redundant, shadowed, or overly permissive rules (`ANY` to `ANY`) create unseen holes in perimeter defenses.

---

## ⚙️ How the Engine Works

1. **Rule Base Ingestion & Normalization**: Ingests firewall rule sets from host firewalls, cloud security groups, or enterprise appliances into a normalized table format.
2. **High-Risk Port Detection**: Identifies rules permitting inbound traffic to high-risk administrative or plaintext ports (21 FTP, 23 Telnet, 22 SSH, 3389 RDP, 445 SMB, 1433 MSSQL).
3. **Permissive CIDR Flagging**: Flags rules allowing unrestricted source CIDRs (`0.0.0.0/0`, `::/0`, `/8`, `/16`).
4. **Shadowed & Redundant Rule Detection**: Identifies rules rendered ineffective because a preceding broader rule already matches all candidate traffic.
5. **Optimization & Cleanup Report**: Emits rule pruning recommendations and hardened replacement entries.

---

## 🚀 Key Capabilities

- Flags open ingress to high-risk administrative ports (SSH, RDP, SMB)
- Detects overly broad source network allowances
- Identifies shadowed and obsolete firewall rules
- Outputs prioritized cleanup tables for network administrators

---

## 🏗️ System Data Flow & Architecture

```
+-----------------------------------+
|  Target Input / Configuration    |
|  (JSON Snapshots / Policies)      |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  1. Schema Normalization Engine   |
|  Validates types & formats        |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  2. Core Analytical Pipeline      |
|  Heuristic rule evaluation,       |
|  invariant checks & drift diffs   |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  3. Risk Classification           |
|  Assigns severity: INFO / HIGH    |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  4. Structured Findings & Report  |
|  Root cause, evidence &           |
|  actionable remediation steps     |
+-----------------------------------+
```

---

## 📄 Findings Output Structure

The engine generates structured, machine-parsable JSON reports adhering to this standard audit schema:

```json
{
  "results": [
    {
      "resource": "resource-identifier",
      "severity": "HIGH",
      "check": "CHECK_IDENTIFIER",
      "detail": "Descriptive analysis of the identified security posture issue.",
      "remediation": "Actionable step-by-step guidance to restore compliant state.",
      "evidence": {
        "observed_field": "value",
        "required_policy": "enforced_policy"
      }
    }
  ],
  "count": 1,
  "scope": "Comprehensive defensive security audit"
}
```

---

## 🔒 Source Code & Enterprise Inquiries

To protect proprietary intellectual property and client operational security:
* **Public Repository**: Contains comprehensive architecture specifications, schemas, and design overviews.
* **Private Repository**: Contains the complete production implementation, continuous integration pipelines, and full regression test suites.

For architectural questions or enterprise inquiries, connect via [LinkedIn](https://www.linkedin.com/in/karthikeyansubramaniam04/) or visit the [Portfolio Site](https://karthikeyansubramaniyam.github.io).
