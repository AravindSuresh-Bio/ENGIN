import random
import os

# --- CONFIGURATION ---
HOST_SOURCE = "host_large.txt"        # Your big E. coli file
VIRUS_SOURCE = "sequence.fasta.txt"   # Your Staph/Covid file
OUTPUT_FILE = "raw_patient_sample.txt" # The final mixed file

HOST_COUNT = 20000    # Huge amount of Host
VIRUS_COUNT = 500     # Small amount of Virus
POLLEN_COUNT = 500    # Small amount of Junk
# ---------------------

print(f"--- GENERATING REALISTIC RAW SAMPLE ---")
mixed_reads = []

# 1. LOAD HOST (E. COLI)
if os.path.exists(HOST_SOURCE):
    print(f"Extracting {HOST_COUNT} Host reads...")
    with open(HOST_SOURCE, "r") as f:
        lines = f.readlines()
        added = 0
        # FASTQ parsing (every 4th line is sequence)
        for i in range(1, len(lines), 4):
            if added >= HOST_COUNT: break
            seq = lines[i].strip()
            if len(seq) > 20 and "N" not in seq:
                mixed_reads.append(seq)
                added += 1
else:
    print("ERROR: generate host_large.txt first!")
    exit()

# 2. LOAD VIRUS (STAPH)
if os.path.exists(VIRUS_SOURCE):
    print(f"Extracting {VIRUS_COUNT} Virus reads...")
    with open(VIRUS_SOURCE, "r") as f:
        full_genome = "".join([line.strip() for line in f if not line.startswith(">")])
        # Chop into pieces
        for i in range(0, len(full_genome), 150):
            if len(mixed_reads) >= HOST_COUNT + VIRUS_COUNT: break
            chunk = full_genome[i:i+150]
            if len(chunk) > 50:
                mixed_reads.append(chunk)

# 3. GENERATE POLLEN (RANDOM DNA)
print(f"Simulating {POLLEN_COUNT} Pollen/Junk reads...")
bases = ['A', 'T', 'C', 'G']
for _ in range(POLLEN_COUNT):
    # Create a random 100-letter string
    pollen_seq = "".join(random.choice(bases) for _ in range(100))
    mixed_reads.append(pollen_seq)

# 4. SHUFFLE EVERYTHING
print("Shuffling the dataset (Simulating sequencer chaos)...")
random.shuffle(mixed_reads)

# 5. SAVE TO FILE
print(f"Saving to {OUTPUT_FILE}...")
with open(OUTPUT_FILE, "w") as f:
    for seq in mixed_reads:
        f.write(seq + "\n")

print(f"DONE. Created '{OUTPUT_FILE}' with {len(mixed_reads)} total reads.")

