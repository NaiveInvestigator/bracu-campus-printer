# bracu-campus-printer

A lightweight Python utility for sending PDF files directly to BRAC University campus printers over the network using the LPD protocol.

## Usage

Download the latest script to the current directory:

```bash
wget -O print.py "https://raw.githubusercontent.com/NaiveInvestigator/bracu-campus-printer/refs/heads/main/print.py"
```

Edit the script to add your student id in `print.py`, then print a PDF:

```bash
python3 print.py path/to/file.pdf
```

In case if it doesnt work, change the hostname to another lab pc.

## Requirements

* Python 3
* `wget`
* Network access to the BRAC University printer
* A PDF file to print
