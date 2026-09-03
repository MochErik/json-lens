# 🔍 JSON-Lens (`json-lens`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![JSON Tool](https://img.shields.io/badge/Format-JSON%20Flatten%20%26%20Diff-blue.svg)](https://github.com/MochErik/json-lens)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-orange.svg)](https://github.com/MochErik/json-lens)

> **Instant JSON Formatter, Flattener & Diff Comparator CLI.** Pretty-print JSON files, flatten deeply nested object trees into dot-notation paths, and calculate key-level delta diffs between two JSON configs.

---

## 🚀 Quick Install

```bash
pip install json-lens
```

---

## 🖥️ Usage

### 1. Flatten Nested JSON
```bash
json-lens flatten appsettings.json
# Output:
# user.profile.name = Erik
# database.pool.max = 20
```

### 2. Compare Diff Between 2 JSON Configs
```bash
json-lens diff config.v1.json config.v2.json
```

---

## 📜 License

MIT License © 2026 [Moch. Erik Irriansyah](https://github.com/MochErik)
