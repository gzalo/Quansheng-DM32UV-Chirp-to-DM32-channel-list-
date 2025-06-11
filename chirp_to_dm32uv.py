import csv

# Input and output file names
input_file = "Quansheng_UV-K5_20250306.csv"
output_file = "CHIRP_to_DM32UV_fixed.csv"

# Default values for DM32UV fields
default_values = {
    "Power": "High",
    "Band Width": "12.5KHz",
    "Scan List": "None",
    "TX Admit": "Allow TX",
    "Emergency System": "None",
    "Squelch Level": "3",
    "APRS Report Type": "Off",
    "Forbid TX": "0",
    "APRS Receive": "0",
    "Forbid Talkaround": "0",
    "Auto Scan": "0",
    "Lone Work": "0",
    "Emergency Indicator": "0",
    "Emergency ACK": "0",
    "Analog APRS PTT Mode": "0",
    "Digital APRS PTT Mode": "0",
    "TX Contact": "None",
    "RX Group List": "None",
    "Color Code": "1",
    "Time Slot": "Slot 1",
    "Encryption": "0",
    "Encryption ID": "None",
    "APRS Report Channel": "1",
    "Direct Dual Mode": "0",
    "Private Confirm": "0",
    "Short Data Confirm": "0",
    "DMR ID": "Radio 1",
    "Scramble": "None",
    "RX Squelch Mode": "Carrier/CTC",
    "Signaling Type": "None",
    "PTT ID": "OFF",
    "VOX Function": "0",
    "PTT ID Display": "0"
}

# Output column order for DM32UV
column_order = [
    "No.", "Channel Name", "Channel Type", "RX Frequency[MHz]", "TX Frequency[MHz]",
    "Power", "Band Width", "Scan List", "TX Admit", "Emergency System", "Squelch Level",
    "APRS Report Type", "Forbid TX", "APRS Receive", "Forbid Talkaround", "Auto Scan",
    "Lone Work", "Emergency Indicator", "Emergency ACK", "Analog APRS PTT Mode",
    "Digital APRS PTT Mode", "TX Contact", "RX Group List", "Color Code", "Time Slot",
    "Encryption", "Encryption ID", "APRS Report Channel", "Direct Dual Mode",
    "Private Confirm", "Short Data Confirm", "DMR ID", "CTC/DCS Encode", "CTC/DCS Decode",
    "Scramble", "RX Squelch Mode", "Signaling Type", "PTT ID", "VOX Function",
    "PTT ID Display"
]

# Read CHIRP CSV and process rows
with open(input_file, newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    output_rows = []

    for i, row in enumerate(reader):
        if not row.get("Name") or not row.get("Frequency"):
            print(f"Skipping incomplete row {i+1}")
            continue

        try:
            rx = float(row["Frequency"])
            offset = float(row.get("Offset", "0") or 0)
            duplex = row.get("Duplex", "").strip()
            if duplex == "+":
                tx = rx + offset
            elif duplex == "-":
                tx = rx - offset
            else:
                tx = rx
        except Exception as e:
            print(f"Skipping row {i+1} due to error: {e}")
            continue

        ctcss_decode = row.get("rToneFreq", "None") or "None"

        new_row = {
            "No.": i + 1,
            "Channel Name": row["Name"],
            "Channel Type": "Anlaog" if row.get("Mode", "").lower() in ["fm", "nfm"] else "Digital",
            "RX Frequency[MHz]": str(rx),
            "TX Frequency[MHz]": str(tx),
            "CTC/DCS Encode": "None",          # Force Encode to None
            "CTC/DCS Decode": ctcss_decode     # Use rToneFreq from CHIRP
        }

        new_row.update(default_values)
        output_rows.append(new_row)

        print(f"Processed: {new_row['Channel Name']} ({rx} MHz)")

# Write output file
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=column_order)
    writer.writeheader()
    writer.writerows(output_rows)

print(f"\n✅ Done! Converted and saved to: {output_file}")
