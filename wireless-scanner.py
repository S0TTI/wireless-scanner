import paramiko

router_ip = "192.168.88.1"
router_username = "admin"
router_password = "admin"

ssh = paramiko.SSHClient()

# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
ssh.connect(hostname=router_ip, username=router_username, password=router_password, allow_agent=False, look_for_keys=False )

# Run command.
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("interface/wireless/scan wlan1 duration=10")
out = ssh_stdout
out = "".join(out)
print("Output command is:\n"+out)
# Close connection.
ssh.close()