# 2025-12-17T14:39:40.229942
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

