# taichi-data-factory
Using taichi's legacy mls-mpm method for fast fluid sim.

## Install
Requirements: python3.5, python3.6, or python3.7 (3.8 and 3.9 do not work)

The following instructions pulled from: https://taichi.readthedocs.io/en/stable/legacy_installation.html

I'll assume you're using python3.7. Oh, and also I was unable to get this dumb thing working through pyenv either.

This is how you install the taichi legacy library. It'll compile the thing from source. (I recommend you put `install.py` in your home directory)

```shell
python3.7 -m pip install colorama numpy Pillow flask scipy pybind11 flask_cors GitPython yapf distro requests PyQt5 psutil
wget https://raw.githubusercontent.com/yuanming-hu/taichi/legacy/install.py
python3.7 install.py
```

Restart your shell (or `source ~/.bashrc`). Then install the fluid library https://github.com/yuanming-hu/taichi_mpm
```shell
ti install mpm
```

## Running
You can verify the install by running an example script.
```shell
python3.7 layersim3d_factory.py configs/test1.yaml
```

The output should look like:
```
[T 06/18/21 11:05:07.494] [logging.cpp:Logger@67] Taichi core started. Thread ID = 17990
Loading module mpm
delta_x = 0.006622516556291391
task_id = test1
[T 06/18/21 11:05:07.795] [/home/albert/taichi/python/taichi/dynamics/mpm.py:__init__@52] log_fn = /home/albert/taichi/outputs/mpm/test1/log.txt
[D 06/18/21 11:05:07.810] [mpm.cpp:initialize@28] 
grid_block_size(): {
  vec: (4, 4, 8)
}
[T 06/18/21 11:05:07.810] [mpm.cpp:initialize@29] BaseParticle size: 208 B
[I 06/18/21 11:05:07.811] [mpm.cpp:initialize@54] Created SPGrid of size 256
[I 06/18/21 11:05:07.824] [mesh.h:operator()@94] Adding mesh, fn=$mpm/cube_smooth_coarse.obj
[T 06/18/21 11:05:07.851] [rigid_body.cpp:operator()@108] Adding a solid rigid body
[D 06/18/21 11:05:07.852] [rigid_body.cpp:initialize_mass_and_inertia@142] 
this->mass: 594.49
```

## Output
The outputs will be stored in the taichi legacy source folder. (the same place you ran the `install.py` script). For me:

`~/taichi/outputs/mpm/`

The output data is in the `frames/*.bgeo` files. You can visualize them using [Houdini Apprentice](https://www.sidefx.com/products/houdini-apprentice/)

## More examples

There are more examples here:
https://github.com/yuanming-hu/taichi_mpm/tree/master/scripts/mls-cpic

