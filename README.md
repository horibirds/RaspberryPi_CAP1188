# RaspberryPi_CAP1188
CAP1188 module simple test

multitap test

## setup

### Raspberry Pi
参考　https://qiita.com/hishi/items/8bdfd9d72fa8fe2e7573
```
git clone https://github.com/RayViljoen/Raspberry-PI-SD-Installer-OS-X.git
cd Raspberry-PI-SD-Installer-OS-X
ここからimgダウンロード https://www.raspberrypi.org/downloads/raspbian/
sudo ./install 201X-XX-XX-raspbian-stretch.img
できたらSDカード抜いて再び差し込む
touch /Volumes/boot/ssh
vim /Volumes/boot/cmdline.txt
  modules-load=dwc2,g_ether を追加
echo "dtoverlay=dwc2" >> /Volumes/boot/config.txt
SDカードを抜き、raspberry piに挿入。USBでPCとつなぐ(内側のUSBとつなぐ)
mac側のインターネット共有ON
ssh pi@raspberrypi.local
passはraspberry
sudo raspi-config
  passwordを変更
vim pass.txt
  wifiのパスワードを書く
sudo sh -c 'wpa_passphrase "wifiのアクセスポイント名" < pass.txt >> /etc/wpa_supplicant/wpa_supplicant.conf'
sudo wpa_cli reconfigure
```

### i2c
https://diyprojects.io/activate-i2c-bus-raspberry-pi-3-zero/#.Wk-PM1SFjOR
```
sudo apt update 
sudo apt upgrade -y
sudo apt-get install -y python-smbus i2c-tools
pi@raspberrypi:~ $ lsmod | grep i2c_
```

### bluetooth
- sudo apt-get update
- sudo apt-get install -y pi-bluetooth blueman pulseaudio pavucontrol pulseaudio-module-bluetooth
- sudo reboot
- pulseaudio -D
- bluetoothctl
- power on
- agent on
- pair <BluetoothスピーカーのMACアドレス>
- scan onでスピーカーのIDを探せる
- trust <BluetoothスピーカーのMACアドレス>
- connect <BluetoothスピーカーのMACアドレス>
- quit
- pactl set-card-profile 1 a2dp
- paplay <sinkの名前> /usr/share/sounds/alsa/Front_Center.wav
- sinkの名前はpactl listで一覧表示可能

## datasheet & pin assign
http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
