if [ "$(id -u)" -ne 0 ]; then
        echo 'This script must be run by root' >&2
        exit 1
fi

sudo mkdir ~/scripts/zoomjoin
sudo cp * ~/scripts/zoomjoin/
mkdir ~/bin
sudo cp zm ~/bin/

echo 'export PATH=$PATH:/home/{username}/bin MUST be added to your shell (.bashrc/.zshrc/etc) to use command zm!'
echo 'Once this is done zoomjoin will be fully installed and can be used with zm [command]'