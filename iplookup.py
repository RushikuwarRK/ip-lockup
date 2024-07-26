import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json().get("ip")
        return ip
    except Exception as e:
        print(f"Error getting public IP: {e}")
        return None

def get_ip_location(ip):
    try:
        access_token = 'c549131ea672ad'  # Replace with your ipinfo.io access token
        response = requests.get(f"https://ipinfo.io/{ip}?token={access_token}")
        return response.json()
    except Exception as e:
        print(f"Error getting IP location: {e}")
        return None

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print(f"Public IP Address: {public_ip}")
        location_info = get_ip_location(public_ip)
        if location_info:
            print("Location Information:")
            for key, value in location_info.items():
                print(f"{key}: {value}")
        else:
            print("Failed to get location information.")
    else:
        print("Failed to get public IP address.")
