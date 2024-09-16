import subprocess

# Función para mostrar el menú
def display_menu():
    print("""
     ______                        ______                                     
    (_____ \             _        / _____)                                  
     _____) )__   ____ _| |_ ____( (____   ____ _____ ____  ____  _____  ____ 
    |  ____/ _ \ / ___|_   _|_____)____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
    | |   | |_| | |     | |_      _____) | (___/ ___ | | | | | | | ____| |    
    |_|    \___/|_|      \__)    (______/ \____)_____|_| |_|_| |_|_____)_|    
      
    """)
    print("Types of Scans")
    print("1. Silent Scan")
    print("2. Version Scan")
    print("3. Aggressive Scan")
    print("4. OS Scan")

# Function to select the option
def option():
    while True:
        x = input("\nSelect one option (1-4): ")
        
        if x in ['1', '2', '3', '4']:
            return x
        else:
            print("Please, select a valid option (1-4)")

# Function that decides which scan to execute
def execute_scan(option, ip):
    if option == '1':
        silent_scan(ip)
    elif option == '2':
        version_scan(ip)
    elif option == '3':
        aggressive_scan(ip)
    elif option == '4':
        os_scan(ip)

# Definitions for the types of scans
def silent_scan(ip):
    print(f"Starting Silent Scan on {ip}")
    subprocess.run(["nmap", "-p-", "-sS", "-T5", "-Pn", ip])

def version_scan(ip):
    print(f"Starting Version Scan on {ip}")
    subprocess.run(["nmap", "-p-", "-sV", "-sC", "-T5", "-Pn", ip])

def aggressive_scan(ip):
    print(f"Starting Aggressive Scan on {ip}")
    subprocess.run(["nmap", "-p-", "-A", "-Pn", "-T5", ip])

def os_scan(ip):
    print(f"Starting OS Scan on {ip}")
    subprocess.run(["nmap", "-p-", "-O", "-Pn", "-T5", ip])

if __name__ == "__main__":
    # Display the menu
    display_menu()

    # Store the selected option
    selected_option = option()

    # Ask for the IP
    ip_address = input("Please, enter the IP you want to scan: ")

    # Execute the scan based on the selected option
    execute_scan(selected_option, ip_address)
