# 2025-12-19T20:03:07.465897300
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

