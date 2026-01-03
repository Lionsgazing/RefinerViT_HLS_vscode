# 2025-12-20T16:38:23.676584600
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

