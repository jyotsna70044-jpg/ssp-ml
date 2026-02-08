Training Data Distribution
        ↓
        PSI / KS / JS
        ↓
Production Data Distribution
        ↓
Drift Score
        ↓
 ┌───────────────┐
 │ Drift Gate    │
 └──────┬────────┘
        ↓
 Promote / Block


| PSI     | Action  |
| ------- | ------- |
| < 0.1   | Safe    |
| 0.1–0.2 | Warn    |
| > 0.2   | Block ❌ |
