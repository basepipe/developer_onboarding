import subprocess
import shutil
import os
import click
import glob


def launch_pycharm(repo='cg_lumberjack'):
    # get the location of pycharm64.exe
    # proc = subprocess.Popen(["where", "pycharm64.exe"], stdout=subprocess.PIPE, shell=True)
    pycharm = get_pycharm_path()
    home = os.path.expanduser("~")
    command = '"%s" "%s"' % (pycharm, os.path.join(home, 'PycharmProjects', repo))
    print command
    subprocess.Popen(command, universal_newlines=True, creationflags=subprocess.CREATE_NEW_CONSOLE)


def get_pycharm_path():
    file_ = glob.glob(r"C:\Program Files (x86)\JetBrains\*\bin\pycharm64.exe")[0]
    return file_


def get_pycharm_hidden_folder():
    file_ = get_pycharm_path()
    os.path.split(file_)
    if '\\' in file_:
        sep = '\\'
    else:
        sep = '/'
    for each in file_.split(sep):
        if 'PyCharm' in each:
            return '.%s' % each.replace(' ', '')
    return None


def create_dot_pycharm_dir():
    pycharm_dir = get_pycharm_hidden_folder()
    dot_PyCharm = os.path.join(__file__.split('src')[0], 'resources', 'dot_PyCharm')
    home = os.path.expanduser("~")
    to_path = os.path.join(home, pycharm_dir)
    if not os.path.exists(to_path):
        print 'Copying %s to %s' % (dot_PyCharm, to_path)
        shutil.copytree(dot_PyCharm, to_path)


def copy_pycharm_settings():
    create_dot_pycharm_dir()
    resources = os.path.join(__file__.split('src')[0], 'resources', 'pycharm_settings')
    home = os.path.expanduser("~")
    pycharm_dir = get_pycharm_hidden_folder()
    if pycharm_dir:
        path_ = os.path.join(home, pycharm_dir, "config", "options")
        if not os.path.exists(path_):
            os.makedirs(path_)
        for each in os.listdir(resources):
            each_path = os.path.join(resources, each)
            to_path = os.path.join(path_, each)
            print 'Copying %s to %s' % (each_path, to_path)
            shutil.copy(each_path, to_path)
    else:
        print 'Could not find dot_PyCharm* directory'

@click.command()
@click.option('--settings', '-s', default=False, help='set up default pycharm settings for cglumberjack development')
@click.option('--launch', '-l', default=False, help='launch pycharm after changing settings')
def main(settings, launch):
    if settings:
        copy_pycharm_settings()
    if launch == 'cgl':
        launch_pycharm()
    if launch == 'dev':
        launch_pycharm(repo='developer_onboarding')


if __name__ == "__main__":
    main()
    # create_dot_pycharm_dir()

