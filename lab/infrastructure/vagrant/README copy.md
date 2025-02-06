Install Vagrant

With Vagrant installed, you are able to create, start, stop, and destroy VMs with simple commands.

Prerequisites

You will need:

The Vagrant CLI installed locally on your machine.

VirtualBox 7.1.6 installed as your virtualization provider.

Where to Start?

Well, you can read the documentation and try it on your own, or you can check out Learn Vagrant: Get Started to see some examples of how it works.

Commands

vagrant up

Starts the VMs declared in the Vagrantfile.

vagrant up <vm-name>

Starts only the specified VM.

vagrant halt

Stops all running VMs.

vagrant halt <vm-name>

Stops a specific VM.

vagrant destroy -f

Destroys all created VMs.

vagrant ssh <vm-name>

SSH into a specific VM.

vagrant status

Check the current status of the VMs.

Example Vagrantfile

Here’s a simple Vagrantfile to spin up a Rocky Linux 9 VM:

Vagrant.configure("2") do |config|
  config.vm.box = "rockylinux/9"
  config.vm.network "private_network", type: "dhcp"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
end

To start the VM, simply run:

vagrant up

Once the VM is up, access it using:

vagrant ssh

Additional Resources

Vagrant Official Documentation

HashiCorp Vagrant GitHub

Vagrantfile Reference