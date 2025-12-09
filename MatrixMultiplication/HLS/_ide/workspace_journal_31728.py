# 2025-12-08T20:43:40.273035200
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

