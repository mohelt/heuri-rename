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


parser = ArgumentParser(description='heuri-rename is a ChRIS ds plugin, which copies files from an input directory to an output directory under different names, similar to pl-bulk-rename, but in a more user-friendly manner using heuristics',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='foo',
                    help='argument which sets example output file name')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')


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

    output_file = outputdir / f'{options.name}.txt'
    output_file.write_text('did nothing successfully!')


if __name__ == '__main__':
    main()
