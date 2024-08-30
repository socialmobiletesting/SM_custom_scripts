import subprocess
import time
import os


def capture_screenshot(device_id, iteration):
    try:
        # Define the local file path to save the screenshot
        screenshot_dir = "C:/Dropbox/Logs/T100-82/"
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{device_id}_iter_{iteration}.png")

        # Capture the screenshot from the device and save it to the local PC
        with open(screenshot_path, "wb") as f:
            subprocess.run(['adb', '-s', device_id, 'exec-out', 'screencap', '-p'], stdout=f)

        print(f"Screenshot saved to {screenshot_path}")
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")


def capture_logcat(device_id, iteration):
    try:
        # Define the local file path to save the logcat output
        logcat_dir = "C:/Dropbox/Logs/T100-82/"
        logcat_path = os.path.join(logcat_dir, f"logcat_{device_id}_iter_{iteration}.txt")

        # Capture the logcat output from the device and save it to the local PC
        with open(logcat_path, "w") as f:
            subprocess.run(['adb', '-s', device_id, 'logcat', '-d'], stdout=f, text=True)

        print(f"Logcat saved to {logcat_path}")
    except Exception as e:
        print(f"Failed to capture logcat: {str(e)}")


def reboot_device(device_id):
    i = 0
    while i < 50:
        time.sleep(25)
        try:
            # Execute the adb devices command and capture the output
            adb = subprocess.run(['adb', 'devices'], capture_output=True, text=True)

            # Parse the output to check if the specified device ID is listed
            device_list = adb.stdout.strip().splitlines()
            print(device_list)
            connected_devices = [line.split()[0] for line in device_list if '\tdevice' in line]
            print(connected_devices)

            if device_id in connected_devices:
                print(f"Device found: {device_id}. Capturing screenshot and logcat, then proceeding with reboot...")

                # Wake up the device
                subprocess.run(['adb', '-s', device_id, 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'])

                # Capture a screenshot before rebooting
                capture_screenshot(device_id, i)

                # Capture the logcat before rebooting
                capture_logcat(device_id, i)

                # Execute the adb reboot command
                result = subprocess.run(['adb', '-s', device_id, 'reboot'], capture_output=True, text=True)

                # Check if the command was successful
                if result.returncode == 0:
                    print("Device rebooted successfully. Iteration:", i)
                else:
                    print(f"Failed to reboot the device. Error: {result.stderr}")
            else:
                print(f"Device {device_id} not found. Skipping reboot.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
        time.sleep(25)

        i = i + 1


if __name__ == "__main__":
    # Specify the device ID here
    device_id = "494346"

    # Call the reboot_device function with the specified device ID
    reboot_device(device_id)
