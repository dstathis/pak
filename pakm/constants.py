cmds = {
    'install': {
        'dnf': ['dnf install {}'],
        'yum': ['yum install {}'],
        'apt': ['apt-get install {}'],
    },
    'remove': {
        'dnf': ['dnf remove {}'],
        'yum': ['yum remove {}'],
        'apt': ['apt-get purge {}'],
    },
    'search': {
        'dnf': ['dnf search {}'],
        'yum': ['yum search {}'],
        'apt': ['apt-cache search {}'],
    },
    'update': {
        'dnf': ['dnf update'],
        'yum': ['yum update'],
        'apt': ['apt-get update', 'apt-get upgrade'],
    },
    'provides': {
        'dnf': ['dnf provides {}'],
        'yum': ['yum provides {}'],
        'apt': ['apt-file search {}'],
    },
}


def centos_get_package_manager():
    if int(os.environ['VERSION_ID']) < 8:
        return 'yum'
    else:
        return 'dnf'


os_ids = {
    'ubuntu': 'apt',
    'debian': 'apt',
    'fedora': 'dnf',
    'centos': centos_get_package_manager
}
