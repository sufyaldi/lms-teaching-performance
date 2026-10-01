import csv
from collections import defaultdict

TOKEN_MAP = {
    'MAT': 1,
    'ASN': 2,
    'QZ': 3,
    'FRM': 4,
    'GRD': 5,
    'ANC': 6
}

def load_and_tokenize_sequences(events_path, lps_path):
    """
    Loads anonymized temporal events and maps them into lecturer sequence trajectories.
    """
    lecturer_events = defaultdict(list)
    
    with open(events_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lec_id = row['lecturer_id']
            token_code = row['token_code']
            token_id = TOKEN_MAP.get(token_code, 0)
            week = int(row['week_offset'])
            lecturer_events[lec_id].append((week, token_id))
            
    # Sort events by week offset for each lecturer
    sequences = {}
    for lec_id, events in lecturer_events.items():
        events.sort(key=lambda x: x[0])
        sequences[lec_id] = [e[1] for e in events]
        
    # Load targets
    targets = {}
    with open(lps_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lec_id = row['lecturer_id']
            targets[lec_id] = float(row['total_lps'])
            
    return sequences, targets

if __name__ == '__main__':
    seqs, tgt = load_and_tokenize_sequences('../data/sample_events.csv', '../data/lecturer_performance_anonymized.csv')
    print(f"Sample script verified: Loaded {len(seqs)} lecturer trajectories.")
