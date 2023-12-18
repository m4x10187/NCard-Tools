# NCard-Tools
Random tools for modifying N-Card (or other clone) DS flashcarts.

Setup
-----
- Install the latest release of Python for your currently installed operating system [here](https://www.python.org/downloads/).
  - As of testing, Python 3.11 works with the scripts provided.

- Next, a GCC compiler is required to build some of the tools provided (i.e., bmp2bm).
  - For Windows users, you will need to install [MingW64](https://www.mingw-w64.org/downloads/).
  - For Linux users, open the Linux Terminal and type: ```sudo apt install gcc``` or ```sudo apt-get install gcc```.

- Install the Pillow image library for Python.
  - For Windows users, type into the Command Prompt: ```py -3 -m pip install pillow```.
  - For Linux users, open the Linux Terminal and type: ```python3 -m pip install pillow```.

- Clone the repository to an empty folder, such as a "source" folder.
  
  ```mkdir "source"```
  
  ```cd "source"```
  
  ```git clone --recursive https://github.com/m4x10187/NCard-Tools.git```

Usage
-----
```
# Convert (.bmp) bitmap image to (.bm).
bmp2bm <input.bmp> <output.bm>

# Convert (.bm) image file back to a (.bmp) bitmap file named "output.bmp".
Windows: py -3 bm2bmp.py <input.bm>
Linux: python3 bm2bmp.py <input.bm>

# Extract "nrio_data.bin" dumped using nrioTool to "output".
Windows: py -3 extract_nrio_data.py <nrio_data.bin>
Linux: python3 extract_nrio_data.py <nrio_data.bin>
```

Credits
-------
- [ApacheThunder](https://github.com/ApacheThunder) for amazing reverse engineering work of the N-Card.
- [Pk11](https://github.com/Epicpkmn11) for making the bm2bmp script (originally was for a DSi camcorder project).

License
-------
The source code is licensed under the CC0 V1.0 license.
