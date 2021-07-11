import yaml
import sys
import os
import random
import hashlib

def hsh(s):
    return int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)

def rand_scale(s=1):
    return 10**random.uniform(-s, s)

if __name__ == '__main__':
  if len(sys.argv) < 2:
      print('Need name pls')
      exit(0)

  filename = sys.argv[1]
  name = os.path.splitext(os.path.basename(filename))[0]

  if len(sys.argv) == 3:
      random.seed(hsh(sys.argv[1]))
  else:
      random.seed(hsh(name))


  # motion params

  # range [.25, .38]
  seg_len = random.uniform(.25, .5)
  #seg_len = .36

  pause_len = .08  # shouldn't really change too much

  #y0 = .02  # [.01 - .1]
  y0 = random.uniform(.01, .1)
  dy = .05  # shouldn't really change this too much
  #x0 = .43  # [.4, .48]
  x0 = random.uniform(.42, .48)
  dx = .5 - x0

  # fluid
  fluid = {
    'type': 'snow',
    'density': 1000,
    'friction': .3,
    'hardening': random.uniform(8, 10),
    'mu_0': 58333.3 * rand_scale(1),
    'lambda_0': 38888.9 * rand_scale(1),
    'theta_c': 2.5e-2 * rand_scale(.5),
    'theta_s': 7.3e-3 * rand_scale(.5),
  }

  # extrusion
  #fl_scale = .3  # [.2, .5]
  fl_scale = random.uniform(.2, .5)

  r = random.random()
  v0 = r*r  # [-1, 0], weighted to 0


  data ={
    'name': name,
    'friction': .3,
    'walls': [
      {
        'pos': (.5, .41, .5),
        'scale': (3.5, .5, 3.5),
        'sticky': True,
        'floor': .45,
      },
      {
        'pos': (.35, .5, .5),
        'scale': (.5, 2.3, 3.5),
      },
      {
        'pos': (.65, .5, .5),
        'scale': (.5, 2.3, 3.5),
      },
      {
        'pos': (.5, .5, .35),
        'scale': (3.5, 2.3, .5),
      },
      {
        'pos': (.5, .5, .65),
        'scale': (3.5, 2.3, .5),
      },
    ],

    'res': 150,
    'seg_len': seg_len,
    'pause_len': pause_len,
    'motion': {
      'y0': .45 + y0,
      'dy': dy,
      'x0': x0,
      'dx': dx
    },

    'fluid': fluid,
    'fluid_scale': fl_scale,
    'v0': v0,
  }

  with open(filename, 'w') as o:
      yaml.dump(data, o, default_flow_style=False)
