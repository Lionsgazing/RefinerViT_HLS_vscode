# 2025-12-05T21:01:58.742584100
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

