# 2025-12-08T21:48:12.805680900
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

