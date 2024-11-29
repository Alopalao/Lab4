import subprocess

def run_command(command_list: list):
    return subprocess.run(
        command_list,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def block_udp_port():
    try:
        result = run_command(["ufw", "status"])

        if result.returncode == 0:
            output = result.stdout.strip()
            if output and output.split(" ")[1].lower() == "inactive":
                result = run_command(["ufw", "enable"])
                print(f"ufw activated: {result.stdout.strip()}")
            command = ["ufw", "deny", "proto", "udp", "from",
                       "any", "to", "any", "port", "631"]
            result = run_command(command)
            
            if result.returncode == 0:
                print(result.stdout.strip())
            else:
                print(f"Error adding rule:\n{result.stderr.strip()}")

        else:
            print(f"Error checking ufw status:\n{result.stderr.strip()}")
    except FileNotFoundError:
        print("ufw is not installed. Run the following command"
              " to install it: sudo apt install ufw")

if __name__ == "__main__":
    block_udp_port()