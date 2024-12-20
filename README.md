# Automatic File Sorter

A Python script to automatically sort files into folders based on their file extensions. This script dynamically detects file extensions in a given directory and organizes files into corresponding folders.

## Features

- Automatically detects file extensions in the directory.
- Creates folders dynamically for each unique file extension.
- Moves files into their respective folders.
- Fully dynamic and adaptable to new file extensions.

## Prerequisites

- Python 3.x
- The `os` and `shutil` libraries (these are built-in Python libraries, no additional installation is needed).

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/anilamrute/automatic-file-sorter.git
   ```

2. Navigate to the project directory:
   ```bash
   cd automatic-file-sorter
   ```

3. Edit the `path` variable in the script to point to the directory you want to organize:
   ```python
   path = r"D:/Your/Directory/Path/"
   ```

4. Run the script:
   ```bash
   python file_sorter.py
   ```

## Folder Structure

The script will create folders in the specified directory for each file type:
- `.txt` files → `text files`
- `.csv` files → `csv files`
- `.jpg`, `.png`, `.jpeg` files → `images files`
- `.xls`, `.xlsx` files → `excel files`
- And more based on the extensions found in the directory.

## Example Output

For a directory with the following files:
```
report.xlsx
image1.jpg
notes.txt
data.csv
```

The script will create the following structure:
```
D:/Your/Directory/Path/
├── csv files/
│   └── data.csv
├── excel files/
│   └── report.xlsx
├── images files/
│   └── image1.jpg
├── text files/
│   └── notes.txt
```

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request.



