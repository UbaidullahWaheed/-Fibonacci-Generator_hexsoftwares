# ⟨F⟩ Fibonacci Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Internship](https://img.shields.io/badge/Hex%20Softwares-Internship-red?style=for-the-badge)

A **premium dark-themed desktop application** built with Python and Tkinter that provides a complete suite of Fibonacci sequence tools — all in one elegant GUI.

---

## 🖼️ Features

| Tab | Description |
|-----|-------------|
| 🔢 **Generate Series** | Generate the first N Fibonacci numbers with live stat pills (count, sum, largest, even count) |
| 🔍 **Check Number** | Check if any number is a Fibonacci number; shows nearest lower & upper Fibonacci |
| 📍 **Nth Term** | Find the exact Fibonacci number at any position (0-indexed) |
| 📊 **Statistics** | Full breakdown — sum, average, golden ratio, even/odd numbers |
| 🔄 **Reverse Series** | Display the Fibonacci series in descending order |
| 📈 **Visualizer** | Animated color bar chart of the series (up to 30 terms) |
| ℹ️ **About** | App information and project details |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x (Tkinter is included by default)

### Run the App
```bash
git clone https://github.com/YOUR_USERNAME/HexSoftwares_Fibonacci_Generator.git
cd HexSoftwares_Fibonacci_Generator
python fibonacci_generator.py
```

---

## 🧮 How It Works

The Fibonacci sequence is defined by the recurrence relation:

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)   for n > 1
```

Result: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...`

### Checking if a number is Fibonacci
A number **N** is a Fibonacci number if and only if one or both of **(5N² + 4)** or **(5N² − 4)** is a perfect square.

### Golden Ratio
As N grows, the ratio of consecutive Fibonacci numbers approaches the **Golden Ratio φ ≈ 1.6180339887...**

---

## 📁 Project Structure

```
HexSoftwares_Fibonacci_Generator/
│
├── fibonacci_generator.py   # Main application
└── README.md                # Project documentation
```

---

## 🛠️ Built With

- **Python 3** — Core language
- **Tkinter** — GUI framework (built-in)
- **Math** — Perfect square checks (built-in)

> ✅ Zero external dependencies — runs out of the box!

---

## 📸 App Preview

```
┌─────────────────────────────────────────────────────┐
│  ⟨F⟩  FIBONACCI GENERATOR    Hex Softwares Internship│
├──────────────┬──────────────────────────────────────┤
│ 🔢 Generate  │   Enter how many numbers to generate  │
│ 🔍 Check     │   ┌──────────────┐  [ Generate ]      │
│ 📍 Nth Term  │   │  e.g. 15     │                    │
│ 📊 Statistics│   └──────────────┘                    │
│ 🔄 Reverse   │   Count: 15  Sum: 986  Largest: 610   │
│ 📈 Visualizer│                                        │
│ ℹ️  About    │   [0]  0                               │
│              │   [1]  1    ...                        │
└──────────────┴──────────────────────────────────────┘
```

---

## 👨‍💻 Author
Ubaidullah Waheed

Developed as **Task 1** of the **Hex Softwares Python Programming Internship**.

- 🌐 [Hex Softwares](https://www.hexsoftwares.tech)
- 📧 info@hexsoftwares.tech
- 💼 [LinkedIn — Hex Softwares](https://linkedin.com/company/hex-softwares)

---

## 📄 License

This project is licensed under the **MIT License**.
