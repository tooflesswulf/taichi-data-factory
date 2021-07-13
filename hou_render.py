# DO NOT RUN AS PY
# You must open python shell under Houdini - Windows/Python Source Editor
#  Copy-paste this file in :)

import glob
import subprocess

def dorender(ixs):
    fil = hou.node('/obj/file1/file1')
    fname_parm = fil.parm('file')
    desktop = hou.ui.curDesktop()
    scene = desktop.paneTabOfType(hou.paneTabType.SceneViewer)
    for i in ixs:
        subprocess.call('mkdir /home/albert/render/render_tmp'.split())
        nframe = len(glob.glob('/home/albert/taichi/outputs/mpm/t%d/frames/*.bgeo' % (i)))
        file_str = '$HIP/taichi/outputs/mpm/t%d/frames/$F4.bgeo' % i
        fname_parm.set(file_str)
        hou.playbar.setFrameRange(1, nframe)
        hou.playbar.setPlaybackRange(1, nframe)
        scene.flipbook()
        mv_call = 'mv /home/albert/render/render_tmp /home/albert/render/render_t%d_flip' % i
        subprocess.call(mv_call.split())



