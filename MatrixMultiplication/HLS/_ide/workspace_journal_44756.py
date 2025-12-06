# 2025-12-05T20:56:12.371088400
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

