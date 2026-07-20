import subprocess


def send_gmt_message(message):
    """Send a Telegram message."""

    try:
        subprocess.run(
            ["/usr/local/bin/hermes", "send", "--to", "telegram", message],
            capture_output=True,
            text=True,
            check=True,
        )

        print("Telegram message sent.")

    except subprocess.CalledProcessError as e:
        print("Failed to send Telegram message.")
        print(e.stderr)