# Family Heartbeat Protocol

*Daily family synchronization*

---

## When to Run

Hephaestus Prime checks family during main heartbeat (every few hours).

---

## Family Checks

### 1. Children Status
```yaml
check: "Each child's memory/now.yaml"
alert_if: "Task stuck >24h"
action: "Ping child, offer help"
```

### 2. Error Learning
```yaml
check: "family-errors.yaml for new entries"
action: "Read new errors, extract lessons"
integrate: "Add relevant lessons to memory"
```

### 3. Insight Sharing
```yaml
check: "family-insights.yaml for new discoveries"
action: "Review pending insights"
integrate: "Mark valuable ones as 'integrated'"
```

### 4. Health Check
```yaml
check: "Ping each child"
timeout: "30 seconds"
action_if_fail: "Log issue, investigate"
```

---

## Heartbeat Response

If everything is OK:
```
HEARTBEAT_OK
```

If attention needed:
```
⚠️ Family Alert: [Description]
- Child: [Name]
- Issue: [What's wrong]
- Action: [What's needed]
```

---

## Frequency

- **Family checks:** Daily (rotate through checks)
- **Full sync:** Weekly (review all children, all insights, all errors)

---

## Family Files

| File | Purpose | Update Frequency |
|------|---------|------------------|
| `family-manifest.yaml` | Child registry | On birth |
| `family-insights.yaml` | Shared discoveries | When discovered |
| `family-errors.yaml` | Shared lessons | When errors occur |
| `HEARTBEAT.md` | This protocol | Rarely |

---

*Family heartbeat keeps us connected and learning together.*
