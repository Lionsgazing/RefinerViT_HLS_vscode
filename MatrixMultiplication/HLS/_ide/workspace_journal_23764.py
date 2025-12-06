# 2025-12-05T20:52:04.244585700
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

