# 2025-12-05T21:08:27.813663300
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

