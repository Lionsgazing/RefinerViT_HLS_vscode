# 2025-12-05T20:38:25.321600300
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

