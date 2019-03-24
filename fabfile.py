from fabric.api import *
# needs fabric3 installed
# pip install fabric3


env.user = 'dtat'
env.hosts = ['dtat.hampl.space']

def pack():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist

    # pack all files
    local('tar --exclude="__pycache__" --exclude="*.pyc" -czvf dist/%s ./cmd ./services ./conf.py ./conf_exmple.py  ./dtat_discord.py  ./README.md ./setup.py' % filename)

def deploy():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist

    # upload the package to the temporary folder on the server
    put('dist/%s' % filename, '/home/dtat/tmp/%s' % filename)

    # unpack files
    run('tar -xvf /home/dtat/tmp/%s -C /home/dtat/www/dtat_discord_bot/' % filename)

    # install requirements
    run('cd /home/dtat/www/dtat_discord_bot/ && /home/dtat/www/dtat_discord_bot/venv/bin/pip install -e .')

    # remove the uploaded package
    run('rm -r /home/dtat/tmp/%s' % filename)

    #restart supervisor's subprocess
    sudo('sudo supervisorctl restart dtat-discord-bot')