# 2025-12-05T20:48:14.958885100
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

