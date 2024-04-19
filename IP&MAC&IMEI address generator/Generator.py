import random

class AddressGenerator:
    def __init__(self):
        self.used_ips = set()
        self.used_macs = set()
        self.used_imeis = set()

    def generate_unique_ip(self):
        ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
        while ip in self.used_ips:
            ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
        self.used_ips.add(ip)
        return ip

    def generate_unique_mac(self):
        while True:
            mac = ":".join("%02x" % random.randint(0, 255) for _ in range(6))
            if mac not in self.used_macs:
                self.used_macs.add(mac)
                return mac

    def generate_unique_imei(self):
        while True:
            imei = "".join(str(random.randint(0, 9)) for _ in range(15))
            if imei not in self.used_imeis:
                self.used_imeis.add(imei)
                return imei

if __name__ == "__main__":
    try:
        num_ipv4 = int(input("Enter the number of unique IPv4 addresses to generate: "))
        num_mac = int(input("Enter the number of unique MAC addresses to generate: "))
        num_imei = int(input("Enter the number of unique IMEI numbers to generate: "))
        
        if num_ipv4 <= 0 or num_mac <= 0 or num_imei <= 0:
            print("Please enter numbers greater than zero.")
        else:
            generator = AddressGenerator()
            print("Generated IPv4 addresses:")
            for _ in range(num_ipv4):
                ip = generator.generate_unique_ip()
                print(ip)

            print("\nGenerated MAC addresses:")
            for _ in range(num_mac):
                mac = generator.generate_unique_mac()
                print(mac)

            print("\nGenerated IMEI numbers:")
            for _ in range(num_imei):
                imei = generator.generate_unique_imei()
                print(imei)
                
    except ValueError:
        print("Please enter valid numbers.")
