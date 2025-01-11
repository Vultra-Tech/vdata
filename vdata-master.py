import argparse
import os
import json

def save_vdata_file(notes, date, code=None, data=None, file_path="example.vdata"):
    """
    Save data to a custom 'vdata' file.
    """
    with open(file_path, 'w') as f:
        f.write("# This is a vdata file, please use the vdata program to edit or run\n")
        f.write(f"Notes: {notes}\n")
        f.write(f"Date: {date}\n")
        if code:
            f.write(f"Code (Optional): {code}\n")
        if data:
            f.write(f"Data (Optional): {data}\n")
    print(f"Vdata file saved to {file_path}")

def read_vdata_file(file_path):
    """
    Read and parse a custom 'vdata' file.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None

    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    vdata = {}
    for line in lines:
        if line.startswith("#"):  # Skip comments
            continue
        key, _, value = line.partition(": ")
        key = key.strip()
        value = value.strip()
        if value:  # Only include lines with values
            vdata[key] = value

    print(json.dumps(vdata, indent=4))
    return vdata

def main():
    parser = argparse.ArgumentParser(description="Manage vdata files via CLI")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands: save, read")

    # Subparser for the 'save' command
    save_parser = subparsers.add_parser("save", help="Save a vdata file")
    save_parser.add_argument("--file", required=True, help="Path to save the vdata file")
    save_parser.add_argument("--notes", required=True, help="Notes for the vdata file")
    save_parser.add_argument("--date", required=True, help="Date for the vdata file (format: YYYY-MM-DD HH:MM:SS)")
    save_parser.add_argument("--code", help="Optional code snippet")
    save_parser.add_argument("--data", help="Optional JSON data")

    # Subparser for the 'read' command
    read_parser = subparsers.add_parser("read", help="Read a vdata file")
    read_parser.add_argument("--file", required=True, help="Path of the vdata file to read")

    args = parser.parse_args()

    if args.command == "save":
        save_vdata_file(
            notes=args.notes,
            date=args.date,
            code=args.code,
            data=args.data,
            file_path=args.file
        )
    elif args.command == "read":
        read_vdata_file(file_path=args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
