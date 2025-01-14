import random
import os

# Define the file for storing past pairings
PAIRINGS_FILE = "pairings.txt"

# Load past pairings from file
def load_past_pairings():
    past_pairings = set()
    try:
        with open(PAIRINGS_FILE, "r") as f:
            for line in f:
                pair = tuple(sorted(line.strip().split(",")))
                past_pairings.add(pair)
    except:
        print("could not find pairings file")
    return past_pairings

# Save new pairings to file
def save_new_pairings(new_pairings):
    with open(PAIRINGS_FILE, "a") as f:
        f.write("\n")
        for pair in new_pairings:
            f.write(f"{pair[0]},{pair[1]}\n")

# Pair names with specified custom pairs and avoid past pairings
def pair_names(names, custom_pairs=None, unpaired_name=None):
    past_pairings = load_past_pairings()
    new_pairings = set()  # Using set to prevent duplicates
    unpaired = None

    # Convert custom_pairs to a set of sorted tuples
    if custom_pairs:
        custom_pairs = {tuple(sorted(pair)) for pair in custom_pairs}
        new_pairings.update(custom_pairs)
        past_pairings.update(custom_pairs)  # Temporarily add to avoid conflicts

    # Filter out names already paired in custom pairs
    paired_names = {name for pair in new_pairings for name in pair}
    remaining_names = [name for name in names if name not in paired_names]

    # If unpaired_name is specified, remove it temporarily from the remaining names if the count is odd
    if unpaired_name and unpaired_name in remaining_names and len(remaining_names) % 2 != 0:
        remaining_names.remove(unpaired_name)
        unpaired = unpaired_name  # Pre-set the unpaired person

    # Shuffle remaining names for random pairing
    random.shuffle(remaining_names)

    # Create pairs from remaining names
    i = 0
    while i < len(remaining_names) - 1:
        pair = tuple(sorted([remaining_names[i], remaining_names[i + 1]]))
        if pair not in past_pairings:
            new_pairings.add(pair)
            past_pairings.add(pair)  # Temporarily add to avoid conflicts
            i += 2
        else:
            # Handle conflict by reshuffling remaining names
            remaining_names[i + 1], remaining_names[-1] = remaining_names[-1], remaining_names[i + 1]
            random.shuffle(remaining_names[i+1:])

    # If no unpaired_name specified and there's an odd number of names, assign the last name as unpaired
    if not unpaired and i == len(remaining_names) - 1:
        unpaired = remaining_names[i]

    # Save only the new pairings to the file
    save_new_pairings(new_pairings)
    
    return list(new_pairings), unpaired

# Example usage
names = ["Marcus Rim", "Jamie Lee", "Shana Lee", "Timmy S", "Haley Park", "Kelsey Miu", 
         "Aaron Wong", "Amy Jung", "Aaron Liu", "Nia Yick", "Millou LaForte",
         "Samantha Hua", "Trevor Hyun", "Joel Lim", "Alvin He", "Carol He", 
         "Molly Youn", "David Oh", "Yusung Hwang", "Ashley Tran", "Sam Hahn", "Daniel Han"]
custom_pairs = [("Amy Jung", "Alvin He"), ("Marcus Rim", "Millou LaForte")]
new_pairings, unpaired = pair_names(names, custom_pairs, unpaired_name="")
print("New Pairings:", new_pairings)
if unpaired:
    print("Unpaired:", unpaired)