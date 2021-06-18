# taichi-data-factory
Using taichi's legacy mls-mpm method for fast fluid sim.

## Install
Requirements: python3.5, python3.6, or python3.7 (3.8 and 3.9 do not work)

The following instructions pulled from: https://taichi.readthedocs.io/en/stable/legacy_installation.html

I'll assume you're using python3.7. Oh, and also I was unable to get this dumb thing working through pyenv either.

This is how you install the taichi legacy library. It'll compile the thing from source.

```
python3.7 -m pip install colorama numpy Pillow flask scipy pybind11 flask_cors GitPython yapf distro requests PyQt5 psutil
wget https://raw.githubusercontent.com/yuanming-hu/taichi/legacy/install.py
python3.7 install.py
```

Restart your shell (or `source ~/.bashrc`). Then install the fluid library https://github.com/yuanming-hu/taichi_mpm
```
ti install mpm
```

You can verify the install by running an example script.
