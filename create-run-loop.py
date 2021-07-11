import os

for i in range(50, 100):
    os.system(f'python3 config_factory.py configs/t{i}.yaml')
    os.system(f'python3.7 layersim3d_factory.py configs/t{i}.yaml')
