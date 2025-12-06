# 2025-12-05T20:28:33.298297600
import vitis

client = vitis.create_client()
client.set_workspace(path="HLS")

vitis.dispose()

