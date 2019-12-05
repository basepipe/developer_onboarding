import subprocess
import shutil
import os
import click


def launch_pycharm():
    # get the location of pycharm64.exe
    proc = subprocess.Popen(["where", "pycharm64.exe"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.split('\r\n')[0]
    out = "%s" % out
    subprocess.Popen(out, universal_newlines=True, creationflags=subprocess.CREATE_NEW_CONSOLE)


def copy_pycharm_settings():
    home = os.path.expanduser("~")
    path_ = os.path.join(home + "\\.PyCharm2019.2\\config\\options\\")
    source_file1 = '../../resources/colors.scheme.xml'
    shutil.copy(source_file1, os.path.join(path_ + "colors.scheme.xml"))

    source_file2 = '../../resources/keymap.xml'
    shutil.copy(source_file2, os.path.join(path_ + "keymap.xml"))

    source_file3 = '../../resources/laf.xml'
    shutil.copy(source_file3, os.path.join(path_ + "laf.xml"))

@click.command()
@click.option('--pycharm', '-p', default=True, help='set up default pycharm settings for cglumberjack development')
@click.option('--launch', '-l', default=True, help='launch pycharm after changing settings')
def main(pycharm, launch):
    if pycharm:
        copy_pycharm_settings()
    if launch:
        launch_pycharm()


if __name__ == "__main__":
    main()


