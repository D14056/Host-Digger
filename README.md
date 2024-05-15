## Host Digger

A Python script to check the status of IP addresses and perform SSL/TLS handshake verification.

### Author: D14056 (🇱🇰)

### Description:

This script allows you to ping a range of IP addresses and determine if they are active. For active IPs, it attempts an SSL/TLS handshake and reports the result. This can be useful for debugging network issues, identifying active servers, and verifying SSL/TLS configurations.

### Functions:

1. **ping_host(ip, timeout)**
    - Pings a single IP address with a specified timeout.
    - Prints whether the IP is active.
    - Attempts an SSL/TLS handshake on port 443.
    - Prints the result of the handshake (successful or failed).
    - Returns True if the handshake is successful, False otherwise.

2. **ping_range(start_ip, end_ip, timeout)**
    - Pings a range of IP addresses within the specified start and end IPs.
    - Uses the `ping_host` function to check each IP.
    - Prints a list of working IPs.

### Requirements:

- Python 3
- `colorama` package
- `OpenSSL` package

### Installation and Running:

#### 1. Windows:

   1. **Install Python:** Download and install the latest version of Python 3 from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to check the "Add Python to PATH" option during installation.

   2. **Open Command Prompt:** Press the Windows key, type "cmd", and press Enter.

   3. **Install required packages:**
      ```bash
      pip install colorama pyOpenSSL
      ```

   4. **Save the code as a Python file (e.g., `host_digger.py`).**

   5. **Run the script:**
      ```bash
      python host_digger.py
      ```

#### 2. Linux:

   1. **Install Python:** Most Linux distributions come with Python pre-installed. If not, you can install it using your distribution's package manager. For example, on Ubuntu:
      ```bash
      sudo apt-get update
      sudo apt-get install python3
      ```

   2. **Open Terminal:** Use the shortcut Ctrl+Alt+T or search for "Terminal" in your applications menu.

   3. **Install required packages:**
      ```bash
      pip3 install colorama pyOpenSSL
      ```

   4. **Save the code as a Python file (e.g., `host_digger.py`).**

   5. **Run the script:**
      ```bash
      python3 host_digger.py
      ```

#### 3. Android Termux:

   1. **Install Termux:** Download and install Termux from the Play Store.

   2. **Open Termux and update packages:**
      ```bash
      pkg update
      pkg upgrade
      ```

   3. **Install Python and required packages:**
      ```bash
      pkg install python
      pip install colorama pyOpenSSL
      ```

   4. **Save the code as a Python file (e.g., `host_digger.py`).** You can use a text editor within Termux or transfer the file from your computer.

   5. **Run the script:**
      ```bash
      python host_digger.py
      ```

### Input and Output:

Once you run the script, it will prompt you for:

- Start IP address
- End IP address
- Ping timeout (in seconds)

The script will then output:

- A list of working IPs
- For each working IP:
    - The hostname (if available)
    - The result of the SSL/TLS handshake

### Example:

```
Enter the start IP: 192.168.1.1
Enter the end IP: 192.168.1.10
Enter the ping timeout (in seconds): 2

Working IPs: ['192.168.1.1', '192.168.1.10']
IP 192.168.1.1 is working: router.asus.com
SSL/TLS handshake successful: TLS 1.3 - Hostname from cert: router.asus.com
IP 192.168.1.10 is working: my-server.local
SSL/TLS handshake failed: Connection refused
```

![photo_2024-05-15_09-53-22](https://github.com/D14056/Host-Digger/assets/165244003/cd1343a6-6afb-477a-ac49-115bc3de7668)
![photo_2024-05-15_09-53-21](https://github.com/D14056/Host-Digger/assets/165244003/db5ce707-33d1-4ec7-8d45-0600e4aa1c1c)
