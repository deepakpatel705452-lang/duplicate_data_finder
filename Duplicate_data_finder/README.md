# Duplicate Data Finder (PS No. 26)

## Project overview
Duplicate Data Finder is a Python 3 console program that reads one entry per line from a text file, identifies repeated entries, displays the total and unique item counts, and writes the unique entries to `unique.txt`.

## Features
- Reads text data from a user-provided file (default: `data.txt`).
- **Option 1 – Exact match:** compares entries exactly as written.
- **Option 2 – Ignore case and extra spaces:** treats uppercase/lowercase and repeated spaces as equivalent.
- Displays how many times each duplicate occurs.
- Saves one copy of each unique entry in `unique.txt`.
- Handles missing files, empty files, and invalid menu choices.

## Concepts used
Python 3, lists, sets/dictionaries (via `dict`), loops, functions, `Counter`, file handling, and exception handling (`try-except`).

## Files
- `duplicate_data_finder.py` – main program.
- `data.txt` – sample input file.
- `unique.txt` – output file created after a successful run.
- `test_cases_passed.pdf` – test-case report.

## How to run
1. Install Python 3.
2. Keep `duplicate_data_finder.py` and `data.txt` in the same folder.
3. Open a terminal in that folder.
4. Run:
   ```bash
   python duplicate_data_finder.py
   ```
5. Press Enter to use `data.txt`, then choose `1` or `2`.

## Sample input (`data.txt`)
```text
apple
banana
banana
apple
orange
banana
```

## Expected result for option 1
- Total items: 6
- Unique items: 3
- Duplicates: apple (3 times), banana (2 times)
- Unique entries are saved to `unique.txt`.

## Note
The program ignores blank-only lines. In exact-match mode, leading/trailing spaces are retained as part of an entry; in option 2, spaces are normalized for comparison and output.
