pulseaudio -D
sleep 5
bluetoothctl << EOF
power on
agent on
pair 08:EB:ED:0B:4E:BD
trust 08:EB:ED:0B:4E:BD
connect 08:EB:ED:0B:4E:BD
quit
EOF
pacmd set-default-sink 0
