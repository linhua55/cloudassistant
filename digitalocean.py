from fabric.api import run,sudo
def regenerate_openssh_host_keys():
    #Not tested
    print "Regenerate OpenSSH Host Keys for safety reason[Debian/Ubuntu only]"
    print "Require ROOT or SUDO Privilege"
    print 'Fingerprint of old keys:'
    print 'RSA Key 2048:'
    run('ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub')
    print 'DSA key 1024:'
    run('ssh-keygen -lf /etc/ssh/ssh_host_dsa_key.pub')
    print 'ECDSA Key 256:'
    run('ssh-keygen -lf /etc/ssh/ssh_host_ecdsa_key.pub')
    print 'Removing old keys'
    sudo('/bin/rm -v /etc/ssh/ssh_host_*')
    print 'Generate new keys'
    sudo('dpkg-reconfigure openssh-server')
    print 'Fingerprint of new keys:'
    print 'RSA Key 2048:'
    run('ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub')
    print 'DSA key 1024:'
    run('ssh-keygen -lf /etc/ssh/ssh_host_dsa_key.pub')
    print 'ECDSA Key 256:'
    run('ssh-keygen -lf /etc/ssh/ssh_host_ecdsa_key.pub')
    print 'You need to update ~/.ssh/known_hosts files on client computers'