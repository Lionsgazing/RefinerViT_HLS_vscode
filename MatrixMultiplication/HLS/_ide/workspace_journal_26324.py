# 2025-12-05T20:35:57.876729900
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

