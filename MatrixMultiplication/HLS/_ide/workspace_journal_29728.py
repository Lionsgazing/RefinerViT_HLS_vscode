# 2025-12-20T15:14:05.959850300
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

