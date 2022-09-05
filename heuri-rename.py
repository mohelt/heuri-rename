#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from importlib.metadata import Distribution

from chris_plugin import chris_plugin

__pkg = Distribution.from_name(__package__)
__version__ = __pkg.version


DISPLAY_TITLE = r"""
 _                     _                                            
| |                   (_)                                           
| |__   ___ _   _ _ __ _ ______ _ __ ___ _ __   __ _ _ __ ___   ___ 
| '_ \ / _ \ | | | '__| |______| '__/ _ \ '_ \ / _` | '_ ` _ \ / _ \
| | | |  __/ |_| | |  | |      | | |  __/ | | | (_| | | | | | |  __/
|_| |_|\___|\__,_|_|  |_|      |_|  \___|_| |_|\__,_|_| |_| |_|\___|
"""


parser = argparse.ArgumentParser(description='pl-heuri-rename is a ChRIS ds plugin,'
                                 'which copies files from an input directory to '
                                 'an output directory under different names, similar to'
                                 'pl-bulk-rename, but in a more user-friendly manner using heuristics', formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('inputdirectory', type=str,
                    help='required: the input directory')
parser.add_argument('outputdirectory', type=str,
                    help='required: the output directory')
parser.add_argument('-f', '--filetodir', type=str, nargs=1,
                    help="Filename to dirname: renames directory name to the name of a file.Make sure theres only files in you input directory. Example in/a.dat, in/b.dat to out/a/ChangedName.dat, out/b/ChangedName.dat, e.g pl-heuri-rename /input /output -f ChangedName")
parser.add_argument('-r', '--restack', action='store_true',
                    help="Restack directories, e.g ename in/a/b/file.dat, in/1/2/file.dat to out/b/a.dat, out/2/1.dat")

# documentation: https://fnndsc.github.io/chris_plugin/chris_plugin.html#chris_plugin
@chris_plugin(
    parser=parser,
    title='heuri-rename',
    category='',                 # ref. https://chrisstore.co/plugins
    min_memory_limit='100Mi',    # supported units: Mi, Gi
    min_cpu_limit='1000m',       # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0              # set min_gpu_limit=1 to enable GPU
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    print(DISPLAY_TITLE)
    if(args.filetodir):
      path = str(os.curdir) + args.inputdirectory
      files = os.listdir(r'{}'.format(path))
      # Accessing files inside each folder
      for file in files:
          outputdirectory = str(os.curdir) + args.outputdirectory
          mode = 0o770
          print(outputdirectory)
          pathf = str(os.curdir) + args.outputdirectory
          pathfull = os.path.join(pathf, Path(file).stem)
          print(pathfull)
          os.mkdir(pathfull, mode)
          # Getting the file extension
          extension_pos = file.rfind(".")
          print(str(extension_pos) + ":extension_pos")
          extension = file[extension_pos:]
          print(extension + ":extension")
          filename = "filename" + Path(file).suffix
          inputpath = str(os.curdir) + args.inputdirectory
          pathVar1 = pathfull + "/" + ''.join(args.filetodir)
          shutil.copy2(os.path.join(inputpath, Path(file)), pathVar1 + extension)
          print(filename + ":filename")


if __name__ == '__main__':
    main()
