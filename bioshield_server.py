import socket
import time
import os
import sys

# --- CONFIGURATION ---
LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 9999
HOST_DB_FILE = "SRR25083113_2.fastq" # Your E. coli file
OUTPUT_FILE = "captured_foreign_dna.fasta" 
# ---------------------

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))
os.system('cls' if os.name == 'nt' else 'clear')

print(f"\n\033[92m[SYSTEM] BIOSHIELD: PURIFICATION MODE | TARGET: FOREIGN DNA\033[0m")

# 1. BUILD THE BLOCKLIST (Host Database)
host_dna_db = set()
count = 0

try:
    print(f"Loading Host Database from {HOST_DB_FILE}...")
    with open(HOST_DB_FILE, "r") as f:
        while True:
            header = f.readline()
            if not header: break 
            sequence = f.readline().strip() 
            f.readline() # Skip +
            f.readline() # Skip Quality
            
            if sequence:
                host_dna_db.add(sequence)
                count += 1
            
            # Increased limit to 100,000 to match your large test
            if count >= 100000: break 
                
    print(f"\033[92m[READY] Blocklist Active ({count} sequences). Listening...\033[0m")

except FileNotFoundError:
    print(f"\n[ERROR] Could not find {HOST_DB_FILE}. Make sure it is in this folder!")
    sys.exit()

# 2. THE PURIFICATION LOOP
total_reads = 0
blocked_host = 0
captured_foreign = 0

print(f"Creating storage file: {os.path.abspath(OUTPUT_FILE)}\n")
start_time = time.time() # START TIMER

# Open file in Write mode
with open(OUTPUT_FILE, "w") as f_out:
    try:
        while True:
            data, addr = sock.recvfrom(4096)
            incoming_dna = data.decode('utf-8').strip()
            total_reads += 1

            if incoming_dna in host_dna_db:
                # HOST -> DISCARD
                blocked_host += 1
            else:
                # FOREIGN -> SAVE
                captured_foreign += 1
                
                # Write to file
                f_out.write(f">Foreign_Read_{captured_foreign}\n")
                f_out.write(f"{incoming_dna}\n")
                
                # --- THE FIX: FORCE DISK WRITE IMMEDIATELY ---
                f_out.flush() 
                os.fsync(f_out.fileno()) 
                # ---------------------------------------------

            # DASHBOARD (Updates every 100 reads)
            if total_reads % 100 == 0:
                elapsed = time.time() - start_time
                print(f"\r\033[96m[STATUS] Time: {elapsed:.1f}s | Processed: {total_reads} | \033[92mSAVED: {captured_foreign}\033[0m ", end="")

    except KeyboardInterrupt:
        end_time = time.time()
        duration = end_time - start_time
        
        # Get final file size
        file_size_kb = os.path.getsize(OUTPUT_FILE) / 1024
        
        print(f"\n\n\033[91m[STOP] Capture Complete.\033[0m")
        print(f"----------------------------------------")
        print(f"Total Time : {duration:.2f} seconds")
        print(f"Total Processed : {total_reads}")
        print(f"Host Discarded : {blocked_host}")
        print(f"Pathogen Saved : {captured_foreign}")
        print(f"Final File Size : {file_size_kb:.2f} KB")
        print(f"File Location : {os.path.abspath(OUTPUT_FILE)}")
        print(f"----------------------------------------")
