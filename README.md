# ENGIN: Edge-Native Genomic Inspection Node
**Version:** 1.0.0-Beta  
**Lead Architect:** Aravind Suresh (AMRSB)  
**Architecture:** Python / C++ Stream Processing  

## 🧬 Project Overview
**ENGIN** (Edge-Native Genomic Inspection Node) is a specialized real-time filtration protocol for high-throughput DNA sequencing pipelines. Acting as a "Bio-Firewall," it sits directly between the sequencer and the storage infrastructure to perform **Deep Packet Inspection** on biological data streams.

**The Problem:**
Clinical sequencing generates massive amounts of non-informative "Host" data (e.g., 99% Human background DNA in an infection sample), which clogs network bandwidth and incurs huge cloud storage costs.

**The Solution:**
ENGIN utilizes a **Negative Selection Algorithm** to intercept raw FASTQ reads at the source (the Edge). It automatically identifies and discards known Host reads while preserving Pathogen and Variant data. This results in **>90% Data Minimization** before the data ever touches the disk, ensuring faster downstream analysis and inherent GDPR compliance.

---

## 🚀 Key Capabilities

### 1. Real-Time "Bio-Firewall"
Unlike standard bioinformatics tools that process static files *after* sequencing, ENGIN processes the live data stream.
* **Input:** Raw FASTQ packets via USB/Network.
* **Logic:** K-mer based negative selection against a local Host Reference.
* **Output:** Purified pathogen/variant stream only.

### 2. Radical Data Minimization
By discarding the "Normal" background noise, ENGIN reduces storage requirements by orders of magnitude.
* **Benchmark:** >90% reduction in file size for metagenomic samples.
* **Cost Impact:** Directly reduces AWS S3 / Azure Blob storage costs for clinical labs.

### 3. GDPR Compliance by Design
Sensitive human genetic data is filtered and discarded at the hardware edge. It never leaves the local device, ensuring patient privacy is mathematically preserved.

---

## ☁️ Cloud Validation Strategy
Before deploying to physical hardware, ENGIN utilizes **Azure Cloud** for high-stress validation and benchmarking:

* **Virtual Edge Simulation (Digital Twins):** We utilize **Azure Virtual Machines** configured with constrained resources (RAM/CPU limits) to mimic the hardware limitations of physical edge devices (e.g., Raspberry Pi / Jetson). This allows us to benchmark the ENGIN C++ logic against "Digital Twins" of our target hardware.
* **Massive Dataset Benchmarking:** Real genomic datasets are Terabytes in size. We use **Azure Blob Storage** to host massive synthetic FASTQ streams and "replay" them against our algorithm to measure throughput speed and packet loss in a controlled, high-bandwidth environment.

## 🛠️ Simulation Architecture (Digital Twin)
Since physical access to high-throughput sequencers (e.g., Illumina NovaSeq) is restricted, this repository utilizes a **Client-Server Simulation** to demonstrate the protocol:

| Component | Simulation Substitute | Role |
| :--- | :--- | :--- |
| **The Sequencer** | Android (Termux) / Client Script | Generates and streams synthetic FASTQ reads via TCP/IP. |
| **The Connection** | Localhost / USB Tethering | Simulates the high-speed hardware bus (e.g., PCIe/USB 3.0). |
| **The Edge Node** | Workstation (ENGIN Core) | Receives packets, performs filtration, and writes the minimized file. |

---

## ⚡ Quick Start (Demo)

**1. Generate Synthetic Data:**
Create a mixed sample (Human + Pathogen) for testing.
```bash
python3 simulation/sample_gen.py

2. Initialize the ENGIN Filter:
Start the server to listen for the sequencer stream.
python3 core_logic/engin_filter.py

3. Start the Sequencer Stream:
Simulate the DNA machine sending data.
python3 simulation/sequencer_sim.py

4. Verify Results:
Check the output/ directory. You will see the filtered file size is ~90% smaller than the raw input, containing only the target non-host reads.
⚠️ Disclaimer
Prototype Status: This software is a functional Proof-of-Concept (PoC) written in Python for architectural demonstration. Production deployment for clinical use would require porting the core filtration logic to C++ or Rust for hardware acceleration.
