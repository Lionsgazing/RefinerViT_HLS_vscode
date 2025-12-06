# 2025-12-05T20:30:29.909782
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

