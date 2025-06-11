# Quansheng-DM32UV-Chirp-to-DM32-channel-list-
This is a Python script to import CSV  Channel lists from Chirp into the Baofeng DM-32Uv CPS software

So you got your shiny new Baofeng DM-32uv radio , and you want to import your channels from Chirp software instead of writing each one of the channels , this script would let you convert your Chirp CSV channel File into a CSV file thats usable with the import feature of the DM32 CPS software.


CHIRP to DM32UV CSV Converter
=============================

This tool converts a CHIRP-format CSV file (e.g., from UV-K5 or similar radios)
into a CSV format compatible with the DM-32UV radio programming software.

Features
--------

- Parses and converts CHIRP CSV files to DM32UV format.
- Automatically calculates TX frequency using Duplex and Offset.
- Maps CHIRP fields into the correct DM32UV format and order.
- Sets the CTCSS Decode tone using CHIRP's rToneFreq field.
- Forces CTCSS Encode to 'None' to avoid transmission without matching tone.
- Fixes a known issue in the DM32UV software where encode/decode are interpreted in reverse.
  - Encode is set to 'None' (disabled).
  - Decode is set based on CHIRP's rToneFreq.
- Sets all other necessary DM32UV fields to safe, usable defaults (e.g., High power, 12.5KHz bandwidth, etc.).
- Supports analog (FM/NFM) and digital channels.

How to Use
----------

1. Make sure you have Python 3 installed.
2. Place this script (chirp_to_dm32uv.py) in the same folder as your CHIRP CSV file (e.g., Quansheng_UV-K5_20250306.csv).
3. Open a command prompt and navigate to the script folder:
   > cd path\to\folder
4. Run the script:
   > python chirp_to_dm32uv.py
5. The output file will be created as:
   CHIRP_to_DM32UV_fixed.csv

Notes
-----

- TX Frequency is derived from RX + Offset (taking Duplex direction into account).
- All CTCSS Encode values are set to 'None' deliberately, to ensure compatibility with DM32UV software.
- CTCSS Decode values are imported from CHIRP (rToneFreq).
- Non-FM modes are marked as Digital.

Output
------

A new file will be saved in the same folder:
CHIRP_to_DM32UV_fixed.csv

You can open this file with Excel, LibreOffice, or directly import it into your DM-32UV software.
