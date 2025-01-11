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

def read_vdata_file(file_path):
    """
    Read and parse a custom 'vdata' file.
    """
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

    return vdata
