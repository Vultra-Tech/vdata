# vdata
Vdata is a file type used to store data easily
> ⚠️ **Important:**
> Vdata is currently advancing; You can still download it, just look for an update soon on our github.
# Files
Myfile.vdata is an example of how Vdata works.  
vdata.py is the file you would need to easily intergrate vdata into your program or other thing.  
vdata-master is what you use to read and write to Vdata files.
# Usage
To use vdata-master you would need the following commands:  
Here is an example to write to a vdata file:  

  
python vdata-master.py save --file myfile.vdata --notes "This is a note"
--date "2025-01-10 10:00:00" --code 'print("Hello World")'
--data '{"key": "value"}' 

Here is an example to read:  
```python3 vdata-master.py read --file myfile.vdata```
# Notes
Video and website is coming soon...
