import asyncio
import os
from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.sign_pythonrsa import PythonRSASigner

# Load default ADB key


def load_adb_key():
    adbkey_path = os.path.expanduser("~/.android/adbkey")
    with open(adbkey_path) as f:
        priv = f.read()
    with open(adbkey_path + ".pub") as f:
        pub = f.read()
    return PythonRSASigner(pub, priv)


signer = load_adb_key()

# Connect to BlueStacks
device = AdbDeviceTcp("127.0.0.1", 5555, default_transport_timeout_s=9)
device.connect(rsa_keys=[signer], auth_timeout_s=0.1)

# Confirm it's working
output = device.shell("echo Hello from BlueStacks")
print(output)

# Tap points
point_a = (516, 877)
point_b = (100, 850)
point_c = (460, 540)

loop_count = 200

# Async tap using connected device


async def adb_tap(x, y):
    device.shell(f"input tap {x} {y}")

# Async swipe using connected device


async def adb_swipe(x1, y1, x2, y2, duration):
    device.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")

# Main logic


async def main():
    for i in range(loop_count):
        await asyncio.sleep(5)
        print(f"\n🔁 Loop {i + 1}/{loop_count}")

        print("Clicking point A...")
        await adb_tap(*point_a)

        print("Waiting 2 seconds...")
        await asyncio.sleep(1)

        print("Clicking point B...")
        await adb_tap(*point_b)

        print("Waiting 2 seconds...")
        await asyncio.sleep(1)

        print("Clicking point C...")
        await adb_tap(*point_c)

        print("Waiting 2 seconds...")
        await asyncio.sleep(1)


        # print("Swiping down...")
        # await adb_swipe(500, 400, 500, 500, 1200)
        # print("Swiping up...")
        # await adb_swipe(500, 1000, 500, 400, 800)

        print("Waiting extra 5 seconds before next loop...")
        await asyncio.sleep(10)

    print("\n✅ All loops complete!")

# Run it
asyncio.run(main())
