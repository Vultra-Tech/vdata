# This code is in archive, meaning it no longer gets supported, though it may be back in cycle soon. Currently it lacks behind, and is in version 1.0.
# If you need something like this, please sign up for our beta tester program for an application, or contribute to this project by adding on to this.



print("This code is deprecated. It is not good practice to use it as it lacks features and may be incompatible with later versions.")
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
