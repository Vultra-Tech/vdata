# vdata
Easily store and ditribute data in a secure way.
> ‼️ **Update**
> We have developed a solution for a vdata application. Beta Testers have gotten access to a early gui product. If you would like to try, sign up for free.
# Files
Myfile.vdata is an example of how Vdata works.   
vdata.py is what you use to read and write to Vdata files, and intergrate it into your system.
# Usage
> ⚠️ **We have changed how to use vdata**  
> Now we have a step by step guide to show you how to use vdata.  

**Step 1**  
Download vdata.py and its dependencies. You can find dependencies and more on INFORMATION.md.  
  
**Step 2**  
Run ```chmod +x vdata.py``` on the script (giving it executable permissions.).  

**Step 3**  
Move it to a location in your PATH such as  
```sudo mv vdata.py /usr/local/bin/vdata```  

**Step 4**  
Rename it to get rid of the .py extension:  
```sudo mv /usr/local/bin/vdata.py /usr/local/bin/vdata```  
#


After completing the steps, you will ned these commands.
Here is an example to write to a vdata file:  

  
vdata save --file myfile.vdata --notes "This is a note"
--date "2025-01-10 10:00:00" --code 'print("Hello World")'
--data '{"key": "value"}' --text "This is text"

Here is an example to read:  
```vdata read --file myfile.vdata```
# Notes
The website is up! Vist it [here.](vultra-tech.infinityfreeapp.com)  
A video wil come out soon.

