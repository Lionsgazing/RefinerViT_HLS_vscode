# 2025-12-05T21:12:20.550104400
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

