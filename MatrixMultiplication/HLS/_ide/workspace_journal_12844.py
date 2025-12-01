# 2025-11-24T16:11:08.905870700
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

