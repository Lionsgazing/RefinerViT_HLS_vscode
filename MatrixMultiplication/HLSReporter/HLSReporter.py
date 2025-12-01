import pandas as pd
import numpy as np
from io import TextIOWrapper
import re
import os



def parse_ascii_table(file: TextIOWrapper, iStop: int = 26):
    rows = []
    i = 0
    for line in file:
        line = line.strip()

        if i >= iStop:
            break

        i += 1
        # Only process rows that start with a table cell "|"
        if not line.startswith("|"):
            continue
        
        # Strip leading/ending "|" and split by "|"
        parts = [col.strip() for col in line.strip("|").split("|")]
        
        # Skip header rows (they contain letters but no numbers or dashes)
        if "Modules" in parts[0] or "Loops" in parts[0]:
            continue
        
        # Skip separator rows
        if re.match(r"[-+]+", line):
            continue
        
        # Save parsed row
        rows.append(parts)
    
    return rows


def split_value_and_percent(s):
    """
    Input examples:
      "1622 (~0%)"
      "22073 (9%)"
      "-"
      "1 (~0%)"
    Returns (value, percent)
    """
    if s == "-" or s.strip() == "":
        return ("-", "-")

    match = re.match(r"(\d+)\s*\((.*?)\)", s)
    if match:
        value, percent = match.groups()
        return value, percent
    else:
        return (s, "-")  # if no percentage exists


def main():

    csvPath = "./AllReports.csv"
    synthesisID: int = 0

    existingDf = None
    if os.path.exists(csvPath):
        existingDf = pd.read_csv(csvPath)

        synthesisID: int = existingDf["SynthesisID"].max() + 1



    with open("../HLS/build/reports/hls_compile.rpt", "r") as file:
        parsed_rows = parse_ascii_table(file)


    # Extract table rows
    #parsed_rows = parse_ascii_table(text)

    # Print as a structured list of dicts
    base_columns  = [
        "Module", "Issue Type", "Slack", "Latency (cycles)", "Latency (ns)",
        "Iteration Latency", "Interval", "Trip Count", "Pipelined",
        "BRAM", "DSP", "FF", "LUT", "URAM"
    ]

    results = []

    for row in parsed_rows:
        entry = dict(zip(base_columns, row))

        # Process the resource columns
        for col in ["BRAM", "DSP", "FF", "LUT", "URAM"]:
            try:
                value, percent = split_value_and_percent(entry[col])
            except:
                continue
            entry[col + "_value"] = value
            entry[col + "_percent"] = percent
            del entry[col]   # remove original combined column

        results.append(entry)

    df = pd.DataFrame(results)
    df.insert(0, "SynthesisID", synthesisID)

    # Concat
    if (type(existingDf) != type(None)):
        dfconcat = pd.concat([df, existingDf], ignore_index=True)
    else:
        dfconcat = df

    dfconcat.to_csv(csvPath)

if __name__ == "__main__":
    main()