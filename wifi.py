import pywifi

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.scan()
results = iface.scan_results()

for result in results:
    print("SSID:", result.ssid)
    print("Signal Strength:", result.signal)

    # Determine the encryption type based on available information
    encryption_type = "WEP" if "WEP" in result.akm else "WPA/WPA2"
    print("Encryption Type:", encryption_type)

    # Print available attributes and methods of the result object
    print("Available Attributes and Methods:", dir(result))

    # Check for available attributes to retrieve channel information
    if hasattr(result, 'channel'):
        print("Channel:", result.channel)
    print("Address:", result.bssid)
    # Check for available attributes to retrieve frequency information
    if hasattr(result, 'frequency'):
        print("Frequency:", result.frequency)
    # Check for available methods to retrieve bitrate information
    if hasattr(result, 'get_bitrates'):
        print("Bitrates:", result.get_bitrates())
    print()


