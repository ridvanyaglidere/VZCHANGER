import os
import sys
import random

def check_root():
    if os.geteuid() != 0:
        print("This script needs to be run as root. Attempting to restart with sudo...")
        os.execlp('sudo', 'sudo', 'python3', *sys.argv)

check_root()

def get_current_mac():
    mac_info = os.popen('ifconfig eth0 | grep "ether"').read()
    mac_address = mac_info.split()[1] if mac_info else 'MAC address not found.'
    return mac_address

def get_current_ip():
    ip_info = os.popen('ifconfig eth0 | grep "inet "').read()
    ip_address = ip_info.split()[1] if ip_info else 'IP address not found.'
    return ip_address

def generate_random_ip():
    return f"10.0.{random.randint(0, 255)}.{random.randint(1, 254)}"

language = input(
    "Choose your language / Elige tu idioma / Wählen Sie Ihre Sprache (1: English, 2: Türkçe, 3: Español, 4: Deutsch): ")

if language == "1":
    os.system('figlet vezir')
    print('''\
Welcome to the MAC and IP Address Changer Tool :)
Follow me on Instagram: https://www.instagram.com/ridvanyaglidere_
Check my GitHub: https://github.com/ridvanyaglidere

1) Set Random MAC Address
2) Set MAC Address Manually
3) Revert to Original MAC Address
4) Show Current MAC Address
5) Set Static IP Address
6) Set Random IP Address
7) Show Current IP Address
Type 'exit' to quit.
''')

elif language == "2":
    os.system('figlet vezir')
    print('''\
MAC ve IP Adresi Degistirme Aracina Hos Geldiniz :)
Instagram hesabımı takip edin: https://www.instagram.com/ridvanyaglidere_
GitHub profilimi kontrol edin: https://github.com/ridvanyaglidere

1) MAC Adresi Random Belirle
2) MAC Adresi Elle Belirle
3) MAC Adresi Orjinale Dondur
4) Mevcut MAC Adresini Göster
5) Statik IP Adresi Belirle
6) Rastgele IP Adresi Belirle
7) Mevcut IP Adresini Göster
Çıkmak için 'exit' yazın.
''')

elif language == "3":
    os.system('figlet vezir')
    print('''\
Bienvenido a la herramienta de cambio de dirección MAC y IP :)
Sígueme en Instagram: https://www.instagram.com/ridvanyaglidere_
Visita mi GitHub: https://github.com/ridvanyaglidere

1) Establecer dirección MAC aleatoria
2) Establecer dirección MAC manualmente
3) Revertir a la dirección MAC original
4) Mostrar dirección MAC actual
5) Establecer dirección IP estática
6) Establecer dirección IP aleatoria
7) Mostrar dirección IP actual
Escriba 'exit' para salir.
''')

elif language == "4":
    os.system('figlet vezir')
    print('''\
Willkommen im vezir :)
Folgen Sie mir auf Instagram: https://www.instagram.com/ridvanyaglidere_
Besuchen Sie mein GitHub: https://github.com/ridvanyaglidere

1) Zufällige MAC-Adresse festlegen
2) MAC-Adresse manuell festlegen
3) Zur ursprünglichen MAC-Adresse zurückkehren
4) Aktuelle MAC-Adresse anzeigen
5) Statische IP-Adresse festlegen
6) Zufällige IP-Adresse festlegen
7) Aktuelle IP-Adresse anzeigen
Geben Sie 'exit' ein, um zu beenden.
''')

else:
    print('Invalid selection. Exiting.')
    exit()

while True:
    operation_number = input(
        'Enter Operation Number / İşlem Numarası Girin: / Introduzca el número de operación: / Geben Sie die Betriebsnummer ein: ')

    if operation_number.lower() == "exit":
        print('Exiting the program. Goodbye!')
        break

    if operation_number == "1":
        current_mac = get_current_mac()
        os.system('ifconfig eth0 down')
        if os.system('macchanger -r eth0') == 0:
            os.system('ifconfig eth0 up')
            new_mac = get_current_mac()
            print(f'Old MAC Address: {current_mac}, New MAC Address: {new_mac}')
        else:
            os.system('ifconfig eth0 up')
            print('Failed to change MAC address. Ensure you have the right permissions.')

    elif operation_number == "2":
        current_mac = get_current_mac()
        new_mac = input('Enter New MAC Address (e.g., 00:11:22:33:44:55): ')
        os.system('ifconfig eth0 down')
        if os.system(f'macchanger -m {new_mac} eth0') == 0:
            os.system('ifconfig eth0 up')
            print(f'Old MAC Address: {current_mac}, New MAC Address: {new_mac}')
        else:
            os.system('ifconfig eth0 up')
            print('Failed to change MAC address. Ensure you have the right permissions.')

    elif operation_number == "3":
        current_mac = get_current_mac()
        os.system('ifconfig eth0 down')
        if os.system('macchanger -p eth0') == 0:
            os.system('ifconfig eth0 up')
            new_mac = get_current_mac()
            print(f'Old MAC Address: {current_mac}, MAC Address reverted to original: {new_mac}')
        else:
            os.system('ifconfig eth0 up')
            print('Failed to revert MAC address. Ensure you have the right permissions.')

    elif operation_number == "4":
        current_mac = get_current_mac()
        print(f'Current MAC Address: {current_mac}')

    elif operation_number == "5":
        current_ip = get_current_ip()
        new_ip = input('Enter New Static IP Address (e.g., 10.0.2.20): ')
        os.system('ifconfig eth0 down')
        os.system('ifconfig eth0 0.0.0.0')
        os.system(f'ifconfig eth0 {new_ip} netmask 255.255.255.0')
        os.system('ifconfig eth0 up')
        updated_ip = get_current_ip()
        print(f'Old IP Address: {current_ip}, New IP Address: {updated_ip}')

    elif operation_number == "6":
        new_ip = generate_random_ip()
        current_ip = get_current_ip()
        os.system('ifconfig eth0 down')
        os.system('ifconfig eth0 0.0.0.0')
        os.system(f'ifconfig eth0 {new_ip} netmask 255.255.255.0')
        os.system('ifconfig eth0 up')
        updated_ip = get_current_ip()
        print(f'Old IP Address: {current_ip}, New Random IP Address: {updated_ip}')

    elif operation_number == "7":
        current_ip = get_current_ip()
        print(f'Current IP Address: {current_ip}')

    else:
        print('Invalid operation number. Please enter a valid option.')
