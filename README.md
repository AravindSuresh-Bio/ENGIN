# ENGIN-V: Edge-Native Genomic Information Normalizer
**Version:** 1.0.0-Beta
**Lead Developer:** Aravind Suresh (AMRSB)
**Core Logic:** Python / C++ Stream Processing



## 🧬 Executive Summary
**ENGIN-V** is an edge-computing utility designed to filter genomic sequencing data in real-time. By acting as a "Bio-Firewall" between the DNA sequencer and the storage network, it solves the critical issue of data redundancy.

The system utilizes a **Negative Selection Algorithm** to perform real-time host-subtraction, automatically discarding "Normal" Human reads while preserving high-value pathogens and variants. This results in **>90% storage reduction** and cleaner datasets for downstream analysis.

---

## 🚀 Core Features

### 1. Real-Time Filtration (The ENGIN)
Unlike standard tools that process static files, ENGIN-V intercepts the FASTQ stream at the source (Simulated via USB/Network interface).
* **Logic:** Deep Packet Inspection (DPI) for genomic reads.
* **Mechanism:** Checks incoming reads against a local "Host Reference" (Blocklist).
* **Result:** Matches are dropped instantly. Non-matches (Pathogens/Mutations) are passed to storage.

### 2. Data Minimization
Designed to meet **GDPR Article 5** requirements by ensuring that sensitive, non-diagnostic human DNA is never stored on the cloud.

---

## 🛠️ Technical Architecture (PoC Simulation)
Since physical access to Illumina sequencers is restricted, this repository uses a "Digital Twin" architecture:

| Component | Simulation Substitute | Role |
| :--- | :--- | :--- |
| **Sequencer** | Android Device (Termux) | Generates and streams raw FASTQ reads. |
| **Connection** | USB Tethering | Simulates the high-speed hardware link. |
| **Edge Node** | Workstation (Python) | Runs the filtration algorithm and saves output. |

---

## 📂 Repository Structure
```text
ENGIN-V/
├── core_logic/
│   ├── engin_filter.py      # Main filtration script
│   └── host_loader.py       # Reference database handler
│
├── simulation/
│   ├── sequencer_sim.py     # Generates synthetic read streams
│   └── sample_gen.py        # Creates mixed Human/Pathogen samples
│
└── docs/
    └── BENCHMARKS.md        # Storage savings log
