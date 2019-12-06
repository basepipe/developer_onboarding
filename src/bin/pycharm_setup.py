import subprocess
import shutil
import os
import click
import glob


def launch_pycharm():
    # get the location of pycharm64.exe
    # proc = subprocess.Popen(["where", "pycharm64.exe"], stdout=subprocess.PIPE, shell=True)
    file = glob.glob(r"C:\Program Files (x86)\JetBrains\*\bin\pycharm64.exe")
    pycharm = file[0]
    pycharm = r"%s" % pycharm
    subprocess.Popen(pycharm, universal_newlines=True, creationflags=subprocess.CREATE_NEW_CONSOLE)


def copy_pycharm_settings():
    print __file__
    resources = os.path.join(__file__.split('src')[0], 'resources', 'pycharm_settings')
    home = os.path.expanduser("~")
    pycharm_dir = ''
    for each in os.listdir(home):
        if '.PyCharm' in each:
            pycharm_dir = each
    if pycharm_dir:
        path_ = os.path.join(home, pycharm_dir, "config", "options")
        if not os.path.exists(path_):
            os.makedirs(path_)
        for each in os.listdir(resources):
            each_path = os.path.join(resources, each)
            to_path = os.path.join(path_, each)
            print 'Copying %s to %s' % (each_path, to_path)
            shutil.copy(each_path, to_path)
        # source_file1 = os.path.join(resources, 'colors.scheme.xml')
        # shutil.copy(source_file1, os.path.join(path_ + "colors.scheme.xml"))
        # print('copied %s to %s' % (source_file1, os.path.join(path_ + "colors.scheme.xml")))
        #
        # source_file2 = os.path.join('keymap.xml')
        # shutil.copy(source_file2, os.path.join(path_ + "keymap.xml"))
        # print('copied %s to %s' % (source_file2, os.path.join(path_ + "keymap.xml")))
        #
        # source_file3 = os.path.join(resources, 'laf.xml')
        # shutil.copy(source_file3, os.path.join(path_ + "laf.xml"))
        # print('copied %s to %s' % source_file3, os.path.join(path_ + "laf.xml"))
    else:
        print 'Could not find .PyCharm* directory'

@click.command()
@click.option('--pycharm', '-p', default=True, help='set up default pycharm settings for cglumberjack development')
@click.option('--launch', '-l', default=False, help='launch pycharm after changing settings')
def main(pycharm, launch):
    if pycharm:
        copy_pycharm_settings()
    if launch:
        launch_pycharm()


if __name__ == "__main__":
    copy_pycharm_settings()


