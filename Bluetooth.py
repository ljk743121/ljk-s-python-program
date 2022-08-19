import bluetooth

target_name = 'YL-BT'
target_address = None

near_device = bluetooth.discover_devices(lookup_names=True)
for devices in near_device:
    if devices[1] == target_name:
        target_address = devices[0]
        break

print (target_address)
