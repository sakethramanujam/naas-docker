sudo groupadd docker &&
sudo usermod -aG docker $USER &&
echo "The system will reboot after this message" &&
sudo reboot