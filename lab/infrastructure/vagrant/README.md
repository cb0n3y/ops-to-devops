# Install Vagrant

With Vagrant installed, you are able to create, start, stop, and destroy VMs with simple commands.

## Prerequisites

You will need:

- The [Vagrant CLI](https://developer.hashicorp.com/vagrant/tutorials/get-started/install) installed locally on yo

- [VirtualBox_7.1.6](https://www.virtualbox.org/wiki/Downloads) installed as your virtualization provider

## Where to Start?

Well, you can read the documentation and try it on your own, or you can check out [Learn Vagrant get started](https://github.com/hashicorp-education/learn-vagrant-get-started) to see some examples of how it works.

## Commands

```vagrant up``` will start the vms declared on the file. If you want to start only one vm, just use the same command with the vm name: ```vagrant up <vm-name>```.

The same principle applies to the other simple management commands:

- Stop the vm(s) ```vagrant halt [vm-name]```
- Destory vm(s) ```vagrant destroy [vm-name]```
- Reload the config ```