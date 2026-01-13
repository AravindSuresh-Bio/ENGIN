import socket
import time
import os

# --- CONFIGURATION ---
TARGET_IP = "10.247.100.195" # <--- YOUR LAPTOP IP
PORT = 9999
RAW_FILE = "raw_patient_sample.txt"
# ---------------------

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if not os.path.exists(RAW_FILE):
    print(f"ERROR: {RAW_FILE} not found. Run generate_sample.py first!")
    exit()

print(f">>> SEQUENCER CONNECTED TO: {TARGET_IP}")
print(f">>> READING FROM: {RAW_FILE}")
print(">>> STREAMING STARTED...")
time.sleep(2)

# Read the file line by line
with open(RAW_FILE, "r") as f:
    reads = f.readlines()
    total = len(reads)
    
    for i, line in enumerate(reads):
        dna = line.strip()
        if dna: # Only send if not empty
            sock.sendto(dna.encode(), (TARGET_IP, PORT))
        
        # Progress Bar
        if i % 500 == 0:
            pct = (i / total) * 100
            print(f"\rSeq Progress: {pct:.1f}% ({i}/{total})", end="")
            
        time.sleep(0.001) # Very fast

print("\n\n>>> RUN COMPLETE. SAMPLE FINISHED.")

