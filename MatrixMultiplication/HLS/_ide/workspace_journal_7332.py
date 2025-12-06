# 2025-12-05T20:45:33.317236900
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

