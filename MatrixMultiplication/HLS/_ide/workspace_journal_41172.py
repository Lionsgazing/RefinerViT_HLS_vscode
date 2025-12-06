# 2025-12-05T20:32:58.070169400
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

