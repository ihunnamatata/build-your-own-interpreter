# 🧮 Build Your Own Interpreter (Math Expression Evaluator)

This project demonstrates a minimal interpreter built in Python. It tokenizes, parses, and evaluates arithmetic expressions using a recursive structure — laying the groundwork for domain-specific languages used in simulation, modeling, and health informatics.

---

## 📌 What It Can Do

- Parses expressions like:
  ```
  (2 + 3) * (4 + 1)
  ```
- Handles:
  - Parentheses
  - `+`, `-`, `*`, `/` operators
- Recursively evaluates expressions using an AST (abstract syntax tree)

---

## 🧠 Healthcare System Use Case

In simulation and EHR systems, clinicians and modelers often define dynamic expressions like:

```text
risk_score = (age * 0.03) + (systolic_bp / 2)
perfusion = pressure * flowrate
```

This interpreter is the foundation for:
- 🧠 FEM scripting interfaces
- 💻 Medical decision logic engines
- 📋 Expression evaluators in digital twin dashboards

---

## 🚀 How to Run

```bash
cd src/
python main.py
```

Then try:
```text
(2 + 3) * (4 + 1)
(10 / 2) + 8
```

---

## 🗂️ Structure

- `main.py` – Recursive interpreter (tokenizer, parser, evaluator)
- `assets/` – Diagram placeholder (AST or flowchart)
- `NOTES.md` – Add your own examples or learning thoughts

---

## 👩🏾‍⚕️ Author

**Ihunna Amugo**  
DDS Candidate | MHA | MS | REHS | PhD(c) Computational Engineering  
GitHub: [@ihunnamatata](https://github.com/ihunnamatata)
