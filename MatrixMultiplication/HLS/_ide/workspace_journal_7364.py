# 2025-12-14T20:08:45.062453300
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

