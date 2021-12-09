###################################################################
#File Name	    : Vagrantfile                                                                                              
#Description	  : This is a Vagrantfile for an automated
#                 deployment of the project M242 Lb03.                                                                                 
#Args           :                                                                                           
#Author         : Sangeeth Sivakumaran
###################################################################
# Where to sync to on Guest — 'vagrant' is the default user name
#GUEST_PATH = '/var/www/html'
Vagrant.configure("2") do |config|

  config.vm.define "m242-mosquitto" do |mosquitto|
    mosquitto.vm.box = "ubuntu/focal64"
    mosquitto.vm.hostname = "m242-mosquitto"
    mosquitto.vm.network "public_network", bridge: "Intel(R) Wi-Fi 6 AX200 160MHz"
    mosquitto.vm.synced_folder "install/", "/logger"
    mosquitto.vm.provision "shell", path: "install/install.sh"
    mosquitto.vm.network "forwarded_port", guest: 1883, host: 1883
  end
end