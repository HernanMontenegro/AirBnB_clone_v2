#!/usr/bin/python3
""" fabric compress module """

from fabric.api import local, put, env, run
from fabric.contrib import files
from datetime import datetime

env.hosts = ['35.227.18.212', '	35.185.5.35']
env.user = "ubuntu"

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
    if (not files.exists(archive_path)):
        return False
    put(archive_path, "/tmp/")
    folder_name = archive_path.split('/')[1].split('.')[0]
    path = "data/web_static/releases/" + folder_name
    run("mkdir " + path)
    run("tar -xzvf /tmp/" + archive_path.split('/')[1] + " -C " + path)
    run("rm /tmp/" + archive_path.split('/')[1])
    run("rm -rf /data/web_static/current")
    run("ln -s " + path + " /data/web_static/current")
    print("New version deployed!")
    return True
