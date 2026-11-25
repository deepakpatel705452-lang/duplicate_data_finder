"""
Duplicate Data Finder
PS No. 26
Reads entries from data.txt, counts duplicates, and saves unique entries.
"""

from collections import Counter
from pathlib import Path


def normalize(entry):
    """Normalize text for case-insensitive comparison and extra-space removal."""
    return " ".join(entry.split()).casefold()


def read_entries(filename):
    """Read non-empty lines from a text file."""
    path = Path(filename)
    with path.open("r", encoding="utf-8") as file:
        return [line.rstrip("\r\n") for line in file if line.strip()]


def analyze_entries(entries, ignore_case=False):
    """Return total count, unique entries, and duplicate counts."""
    if ignore_case:
        # Keep the first original spelling for each normalized entry.
        display_names = {}
        keys = []
        for entry in entries:
            key = normalize(entry)
            if key not in display_names:
                display_names[key] = " ".join(entry.split())
            keys.append(key)
        counts = Counter(keys)
        unique_entries = [display_names[key] for key in display_names]
        duplicates = [
            (display_names[key], count)
            for key, count in counts.items()
            if count > 1
        ]
        unique_count = len(display_names)
    else:
        counts = Counter(entries)
        unique_entries = list(dict.fromkeys(entries))
        duplicates = [(entry, count) for entry, count in counts.items() if count > 1]
        unique_count = len(counts)

    return len(entries), unique_count, duplicates, unique_entries


def save_unique_entries(unique_entries, output_file="unique.txt"):
    """Write unique entries to the output file."""
    with open(output_file, "w", encoding="utf-8") as file:
        for entry in unique_entries:
            file.write(entry + "\n")


def main():
    print("=" * 45)
    print("          DUPLICATE DATA FINDER")
    print("=" * 45)
    filename = input("Enter input file name [data.txt]: ").strip() or "data.txt"

    print("\nChoose comparison mode:")
    print("1. Exact match")
    print("2. Ignore case and extra spaces")

    choice = input("Enter your choice (1 or 2): ").strip()
    if choice not in ("1", "2"):
        print("Invalid choice. Please run the program again and select 1 or 2.")
        return

    try:
        entries = read_entries(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return
    except OSError as error:
        print(f"Unable to read the file: {error}")
        return

    if not entries:
        print("File is empty. Nothing to check.")
        return

    ignore_case = choice == "2"
    total, unique_count, duplicates, unique_entries = analyze_entries(
        entries, ignore_case=ignore_case
    )

    print("\n---------- RESULT ----------")
    print(f"Total items: {total}")
    print(f"Unique items: {unique_count}")

    if duplicates:
        print("Duplicates:")
        for entry, count in duplicates:
            print(f"  {entry} ({count} times)")
    else:
        print("No duplicates found.")

    try:
        save_unique_entries(unique_entries)
        print("Unique list saved to unique.txt")
    except OSError as error:
        print(f"Unable to save unique.txt: {error}")


if __name__ == "__main__":
    main()
