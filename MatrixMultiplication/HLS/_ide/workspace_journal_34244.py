# 2025-12-05T20:59:41.041351500
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

