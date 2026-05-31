# ENGIN — Edge-Native Genomic Inspection Node

Experimental prototype exploring streamed genomic read filtration and edge-oriented FASTQ preprocessing workflows.

---

## 🧬 Overview

ENGIN (Edge-Native Genomic Inspection Node) is an exploratory computational biology project investigating whether genomic reads can be filtered during streaming rather than after complete dataset generation.

The project simulates a simplified edge-processing workflow where incoming FASTQ-style reads are compared against a local reference dataset to separate known "host" sequences from potentially relevant non-host reads.

The repository currently contains early proof-of-concept implementations written primarily in Python.

---

## 🎯 Project Goals

This project was created to explore concepts involving:

* Streamed genomic data processing
* Host-versus-foreign read filtering
* Edge-oriented biological workflows
* Lightweight genomic preprocessing
* Real-time sequence handling concepts
* Systems-oriented bioinformatics experimentation

Rather than functioning as a production bioinformatics tool, ENGIN is intended as an experimental architecture and learning-oriented systems project.

---

## ⚙️ Current Prototype Architecture

The current implementation simulates a simplified sequencing pipeline using socket-based communication between a synthetic read generator and a filtering node.

### Components

| Component             | Role                                        |
| --------------------- | ------------------------------------------- |
| `generate_sample.py`  | Creates synthetic sequence samples          |
| `sequencer.py`        | Simulates streamed read transmission        |
| `bioshield_server.py` | Receives reads and performs filtering logic |

---

## 🔬 Current Filtering Logic

The prototype currently uses direct sequence matching against a local host reference dataset.

Simplified workflow:

1. Incoming reads are streamed through UDP sockets
2. Reads are compared against a locally loaded host database
3. Matching reads are discarded
4. Non-matching reads are written to an output FASTA file

This implementation is intentionally simplified and primarily designed to explore workflow architecture rather than optimized biological accuracy or production-scale throughput.

---

## 🧪 Experimental Nature

This repository represents an exploratory proof-of-concept project.

The current implementation:

* Uses simplified filtering logic
* Simulates sequencing workflows
* Is not clinically validated
* Is not intended for production or diagnostic use
* Does not represent optimized genomic classification methods

Future versions may explore:

* K-mer-based filtering
* Bloom filters
* Faster indexing structures
* Rust/C++ implementations
* Distributed processing
* Cryptographic verification systems

---

## 🚀 Running the Demo

### 1. Generate Synthetic Data

```bash
python generate_sample.py
```

### 2. Start the Filtering Node

```bash
python bioshield_server.py
```

### 3. Start the Stream Simulator

```bash
python sequencer.py
```

---

## 🧠 Technical Interests Behind This Project

ENGIN was primarily developed as an exploratory systems-biology and computational infrastructure project investigating intersections between:

* Bioinformatics workflows
* Stream processing
* Edge computing concepts
* Sequence filtration architectures
* Biological information systems

---

## ⚠️ Disclaimer

This project is an experimental educational and exploratory prototype created for systems-oriented computational biology experimentation.

It should not be used for:

* clinical diagnostics
* medical decision-making
* production genomic analysis
* validated pathogen detection workflows

---

## 👤 Author

Aravind Suresh
Biotechnology Graduate & Computational Biology Student

Associate Member, Royal Society of Biology (AMRSB)
