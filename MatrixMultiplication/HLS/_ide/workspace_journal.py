# 2025-11-21T00:18:45.141381900
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

