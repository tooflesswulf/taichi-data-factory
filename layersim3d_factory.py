import taichi as tc
from math import *
from random import *
import yaml
import sys

if len(sys.argv) < 2:
    print('Need path to config file')
    exit(0)

with open(sys.argv[1], 'r') as f:
    params = yaml.load(f)

r = params['res']
friction = params['friction']
def lerp(p0, p1, t):
    x0, y0, z0 = p0
    x1, y1, z1 = p1

    xr = x0 * (1-t) + x1 * t
    yr = y0 * (1-t) + y1 * t
    zr = z0 * (1-t) + z1 * t
    return (xr, yr, zr)


def endpoints(i):
    x0 = params['motion']['x0']
    dx = params['motion']['dx']
    y0 = params['motion']['y0']
    dy = params['motion']['dy']

    if i == 0:
        return (x0,      y0, x0),      (x0+2*dx, y0, x0)
    elif i == 1:
        return (x0+2*dx, y0, x0 + dx), (x0,      y0, x0 + dx)
    elif i == 2:
        return (x0,      y0, x0+2*dx), (x0+2*dx, y0, x0+2*dx)

    elif i == 3:
        return (x0+2*dx, y0+dy, x0+2*dx), (x0+2*dx, y0+dy, x0)
    elif i == 4:
        return (x0 + dx, y0+dy, x0),      (x0 + dx, y0+dy, x0+2*dx)
    elif i == 5:
        return (x0     , y0+dy, x0+2*dx), (x0     , y0+dy, x0)



def motion(t):
    period = params['seg_len'] + params['pause_len']

    for i in range(6):
        ti = i * period
        if ti <= t < ti + params['seg_len']:
            tnorm = (t - ti) / params['seg_len']
            return lerp(*endpoints(i), tnorm)
    return None


if __name__ == '__main__':
    tmax = int(6*(params['seg_len'] + params['pause_len']) * 100) + 50

    mpm = tc.dynamics.MPM(
        res=(r + 1, r + 1, r + 1),
        gravity=(0, -10, 0),
        pushing_force=0,
        penalty=1e3,
        rigid_penalty=1e4,
        task_id=params['name'],
        friction=0,
        num_frames=tmax)
    
    for wall in params['walls']:
        pos = tc.Vector(*wall['pos'])
        scale = tuple(wall['scale'])
        fric = friction
        if 'sticky' in wall and wall['sticky']:
            fric = -1

        mpm.add_particles(
            type='rigid',
            density=100000,
            friction=fric,
            scale=scale,
            scripted_position=tc.constant_function13(pos),
            scripted_rotation=tc.constant_function13(tc.Vector(0, 0, 0)),
            codimensional=False,
            mesh_fn='$mpm/cube_smooth_coarse.obj',
        )
    
    r2 = params['fluid_scale']
    fp = params['fluid']
    def frame_update(t, frame_dt):
        trans = motion(t)
        tex1 = tc.Texture(
          'mesh',
          translate=trans,
          scale=(r2, r2, r2),
          filename='$mpm/cylinder_jet.obj') * 10
        mpm.add_particles(
          pd_source=True,
          delta_t=frame_dt,
          density_tex=tex1.id,
          initial_velocity=(0, params['v0'], 0),
          **fp
          )
    
    mpm.simulate(
        clear_output_directory=True,
        update_frequency=2,
        frame_update=frame_update,
        print_profile_info=True,
    )
    
