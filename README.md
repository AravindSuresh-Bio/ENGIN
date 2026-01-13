# Bio-Firewall: Real-Time Genomic Decontamination System

**Status:** Proof of Concept (PoC) | **Version:** 1.0.0  
**Architecture:** Client-Server (Edge Computing)

## 🧬 Project Overview
The **Bio-Firewall** is an edge-computing solution designed to filter genomic sequencing data in real-time. It acts as an intermediary "safety net" between a DNA sequencer and the cloud/storage network.

By utilizing a negative filtering algorithm, the system automatically detects and discards "Host" DNA (e.g., Human background) while preserving "Pathogen" DNA (e.g., Virus, Bacteria) and novel variants. This reduces data storage requirements by **95%** and protects patient privacy by keeping sensitive genomic data offline.

## 🚀 Key Features
* **Real-Time Stream Processing:** Filters data packets instantaneously as they are generated, rather than post-processing huge files.
* **Negative Filtering Logic:** Saves ONLY data that does *not* match the known Host Genome. Catches known pathogens and unknown "Disease X" candidates.
* **Edge-Native:** Designed to run on local hardware (Laptop/Server) connected directly to the sequencer via low-latency links (USB/Ethernet).
* **Privacy Preserving:** Host DNA is discarded locally; it never touches the internet.

## 🛠️ Simulation Architecture
Since access to physical Illumina/Nanopore sequencers is restricted, this repository contains a **"Digital Twin" simulation**:

| Component | Simulation Substitute | Role |
| :--- | :--- | :--- |
| **Sequencer** | **Android Device (Termux)** | Generates and streams raw FASTQ reads. |
| **Connection** | **USB Tethering (RNDIS)** | Simulates the high-speed, hard-wired link used in labs. |
| **Edge Server** | **Windows Workstation (Python)** | Receives the stream, filters against a Blocklist, and saves the target data. |

### Biological Proxies Used
To model a clinical infection scenario efficiently:
* **Host (Blocklist):** *E. coli* reads (Proxy for Human Genome).
* **Target (Save):** *Staphylococcus* reads (Proxy for Pathogen).
* **Noise:** Synthetic random DNA (Proxy for environmental contaminants/Pollen).

## 📂 Repository Structure
```text
Bio-Firewall-PoC/
├── edge_server/
│   ├── bioshield_filter.py       # Main Server Script (The Firewall)
│   ├── host_db_loader.py         # Database logic
│   └── captured_data/            # Output folder for purified DNA
│
├── simulated_sequencer/
│   ├── sequencer.py              # Client Script (The DNA Machine)
│   └── generate_sample.py        # Generates the mixed "Patient Sample" file
│
└── docs/
    └── methodology.txt           # Detailed explanation of the logic

⚡ How to Run the Demo
Step 1: Prepare the "Edge Server" (Laptop)
 * Navigate to the edge_server folder.
 * Ensure you have a reference file (e.g., SRR...fastq) to act as the Host Database.
 * Run the firewall:
   python bioshield_filter.py

   Wait for the message: [READY] Blocklist Active...
Step 2: Prepare the "Sequencer" (Phone/Client)
 * Navigate to the simulated_sequencer folder.
 * Generate a fresh sample file:
   python generate_sample.py

 * Start the sequence stream (ensure IP matches your laptop):
   python sequencer.py

Step 3: View Results
 * Watch the live dashboard on the Laptop terminal.
 * When complete, check captured_foreign_dna.fasta in the output folder.
 * Expected Result: File size reduced by ~95%, containing only Pathogen/Foreign reads.
⚠️ Disclaimer
This software is a Prototype.
The code provided here is a Python-based implementation for demonstration and educational purposes. It utilizes single-threaded logic for readability.
 * Production Implementation: A commercial-grade version of this architecture would utilize C++ / Rust and FPGA Acceleration to handle the 100,000+ reads/second output of clinical sequencers.
 * Bio-Safety: This tool is for data compression and research; it is not a certified diagnostic device.
Created by Aravind Suresh
