# bracu-campus-printer

A lightweight Python utility for sending PDF files directly to BRAC University campus printers over the network using the LPD protocol.

## Usage

Download the latest script to the current directory:

```bash
wget -O print.py "YOUR_SCRIPT_URL"
```

Edit the printer and job parameters in `print.py`, then print a PDF:

```bash
python3 print.py path/to/file.pdf
```

## Configuration

The editable LPD parameters are defined as variables in the script:

```python
queue = "..."
username = "..."
job_name = "..."
control_file_name = "..."
data_file_name = "..."
```

Only the actual editable values need to be changed. The fixed LPD protocol prefixes and suffixes are hardcoded in the script.

## Requirements

* Python 3
* `wget`
* Network access to the BRAC University printer
* A PDF file to print

## How It Works

The script:

1. Connects to the configured printer over TCP.
2. Establishes an LPD print session.
3. Sends the print job's control information.
4. Transfers the PDF file as the print data.
5. Closes the connection after submitting the job.

