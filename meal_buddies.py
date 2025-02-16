import random

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
    except FileNotFoundError:
        print("Pairings file not found. Starting fresh.")
    return past_pairings

# Save new pairings to file
def save_new_pairings(new_pairings):
    with open(PAIRINGS_FILE, "a") as f:
        for pair in new_pairings:
            f.write(f"{pair[0]},{pair[1]}\n")
        f.write("\n")

# Pair names with specified custom pairs and avoid past pairings
def pair_names(names, custom_pairs=None, unpaired_name=None):
    past_pairings = load_past_pairings()
    custom_pairs = {tuple(sorted(pair)) for pair in (custom_pairs or [])}
    max_retries = 10  # Limit the number of retries to avoid infinite loops
    retry_count = 0

    unpaired = unpaired_name
    if unpaired_name:
        names.pop(names.index(unpaired_name))


    while retry_count < max_retries:
        retry_count += 1
        print(f"Attempt {retry_count} at pairing names...")
        random.shuffle(names)  # Shuffle names for a fresh start
        new_pairings = set(custom_pairs)  # Include custom pairs from the start
        remaining_names = [name for name in names if name not in {n for pair in custom_pairs for n in pair}]

        # Attempt to create pairs
        while len(remaining_names) > 1:
            name1 = remaining_names.pop(0)
            pair_found = False

            for i, name2 in enumerate(remaining_names):
                pair = tuple(sorted([name1, name2]))
                if pair not in past_pairings:
                    new_pairings.add(pair)
                    past_pairings.add(pair)
                    remaining_names.pop(i)
                    pair_found = True
                    break

            if not pair_found:
                print(f"Conflict detected for {name1}. Restarting...")
                break  # Restart the entire pairing process

        # Handle the final unpaired person if restart didn't occur
        if len(remaining_names) == 1:
            unpaired = remaining_names.pop()
        
        # Check for success
        if len(remaining_names) == 0:
            save_new_pairings(new_pairings)
            return list(new_pairings), unpaired

    raise Exception(f"Failed to pair names after {max_retries} attempts. Consider adjusting constraints.")

# Example usage
names = ["Marcus Rim", "Timmy S", "Haley Park", "Kelsey Miu", 
         "Aaron Wong", "Amy Jung", "Aaron Liu", "Millou LaForte", 
         "Samantha Hua", "Trevor Hyun", "Joel Lim", "Alvin He", "Carol He", 
         "Molly Youn", "Yusung Hwang", "Ashley Tran", "Sam Hahn", "Daniel Han", 
         "Minjoo Yang", "Christine Kim", "Dylan Kim", "Noah Ong"]
# custom_pairs = [("Amy Jung", "Ashley Tran"), ("Marcus Rim", "Alvin He")]
custom_pairs = []

new_pairings, unpaired = pair_names(names, custom_pairs, unpaired_name=None)
print("New Pairings:", new_pairings)
if unpaired:
    print("Unpaired:", unpaired)
