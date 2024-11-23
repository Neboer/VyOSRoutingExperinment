import ipaddress

def is_address_in_network(ip, network):
    # 创建 IPv6 地址和网络对象
    address = ipaddress.IPv6Address(ip)
    net = ipaddress.IPv6Network(network, strict=False)

    # 检查地址是否在网络中
    return address in net

if __name__ == "__main__":
    ip = "2001:3::f4e3:78ff:feb9:35ca"
    network = "2001::/29"

    if is_address_in_network(ip, network):
        print(f"{ip} 在 {network} 网段内。")
    else:
        print(f"{ip} 不在 {network} 网段内。")
