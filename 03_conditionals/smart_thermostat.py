device_status = "active"
tempresture = 38

if device_status == "active":
    if tempresture > 35:
        print("High Tempreture Alert!")
    else:
        print("Everything is fine")
else:
    print("Device offline")