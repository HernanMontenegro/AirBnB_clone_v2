#!/usr/bin/python3
""" fabric compress module """

from fabric.api import *
import os
from datetime import datetime

env.hosts = ['35.227.18.212', '35.185.5.35']


def do_pack():
    """ Create a compression """
    local("mkdir -p versions/")
    now = datetime.now()
    name = "versions/web_static_" + now.strftime("%Y%m%d%H%M%S")
    try:
        local("tar -cvzf " + name + ".tgz web_static")
        return "{}.tgz".format(name)
    except:
        return None


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if (not archive_path or not os.path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split('/')[1]
        folder_name = file_name.split('.')[0]
        path = "/data/web_static/releases/" + folder_name
        run("mkdir -p " + path)
        run("tar -xzvf /tmp/" + file_name + " -C " + path)
        run("mv " + path + "/web_static/* " + path)
        run("rm -rf " + path + "/web_static/")
        run("rm /tmp/" + file_name)
        run("rm -rf /data/web_static/current")
        run("ln -s " + path + " /data/web_static/current")
        return True
    except:
        return False


def deploy():
    """ creates and distributes an archive to your web server """
    comp = do_pack()

    if (not comp):
        return False
    return do_deploy(comp)
