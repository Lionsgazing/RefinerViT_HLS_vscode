# 2025-12-05T21:04:21.972115
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

