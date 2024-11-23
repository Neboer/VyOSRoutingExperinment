sudo sysctl -w net.ipv6.conf.virbr1.disable_ipv6=0
sudo ip addr add 100.100.1.10/24 dev virbr1
sudo ip -6 addr add 3fff:1::10/112 dev virbr1
sudo ip route add 100.100.0.0/16 via 100.100.1.1
sudo ip -6 route add 3fff::/16 via 3fff:1::1
