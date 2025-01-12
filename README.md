# vdata
Easily store and ditribute data in a secure way.
# Files
Myfile.vdata is an example of how Vdata works.  
vdata.py is the file you would need to easily intergrate vdata into your program or other thing.  
vdata-master is what you use to read and write to Vdata files.
# Usage
> ⚠️ **Important:**
If you want to be able to globally use these commands, you will have to add the location of the program to your PATH. We are currently working on a executable file so if you would like the beta, please [join our waitlist.](https://forms.gle/Swbwiny33DwH5HAH9) 

To use vdata-master you would need the following commands:  
Here is an example to write to a vdata file:  

  
python vdata-master.py save --file myfile.vdata --notes "This is a note"
--date "2025-01-10 10:00:00" --code 'print("Hello World")'
--data '{"key": "value"}' 

Here is an example to read:  
```python3 vdata-master.py read --file myfile.vdata```
# Notes
The website is up! Vist it [here.](vultra-tech.infinityfreeapp.com)  
A video wil come out soon.

