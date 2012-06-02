from fabric.api import run, sudo, cd, env, task
from fabric.colors import green

from ..literals import OS_UBUNTU, OS_FEDORA
import linux, ubuntu, fedora


@task
def install_dependencies():
    """
    Install OS dependencies
    """
    print(green('Installing dependencies for %s' % env.os_name, bold=True))
    
    if env.os == OS_UBUNTU:
        ubuntu.install_dependencies()
    elif env.os == OS_FEDORA:
        fedora.install_dependencies()


@task
def install_mayan():
    """
    Install Mayan EDMS
    """
    
    print(green('Installing Mayan EDMS from git repository', bold=True))

    if env.os in [OS_UBUNTU, OS_FEDORA]:
        linux.install_mayan()


@task
def install_database_manager():
    """
    Install the selected database manager
    """
    
    print(green('Installing database manager: %s' % env.database_manager_name, bold=True))
    
    if env.os == OS_UBUNTU:
        ubuntu.install_database_manager()
    elif env.os == OS_FEDORA:
        fedora.install_database_manager()


@task
def fix_permissions():
    """
    Fix installation files' permissions
    """

    print(green('Fixing installation files\' permissions', bold=True))

    if env.os == OS_UBUNTU:
        ubuntu.fix_permissions()
    elif env.os == OS_FEDORA:
        fedora.fix_permissions()


@task
def install_webserver():
    """
    Installing the OS packages for the webserver
    """
    
    print(green('Installing webserver: %s' % env.webserver_name, bold=True))
    
    if env.os == OS_UBUNTU:
        ubuntu.install_webserver()
    elif env.os == OS_FEDORA:
        fedora.install_webserver()

        
@task
def delete_mayan():
    """
    Delete Mayan EDMS from the OS
    """
    
    print(green('Deleting Mayan EDMS files', bold=True))

    if env.os in [OS_UBUNTU, OS_FEDORA]:
        linux.delete_mayan()
        

@task
def post_install():
    """
    Perform post install operations
    """            
    if env.os == OS_UBUNTU:
        ubuntu.post_install()
    elif env.os == OS_FEDORA:
        fedora.post_install()
