pulseaudio -D
sudo killall bluealsa

pulseaudio --start
sleep 5
bluetoothctl << EOF
power on
agent on
pair 08:EB:ED:0B:4E:BD
trust 08:EB:ED:0B:4E:BD
connect 08:EB:ED:0B:4E:BD
quit
EOF

pacmd set-card-profile 1 a2dp_sink
pacmd set-default-sink 1
