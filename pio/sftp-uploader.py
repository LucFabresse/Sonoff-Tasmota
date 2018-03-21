Import("env")
from base64 import b64decode
# from pprint import pprint

env.Replace(UPLOADER="scp")
env.Replace(UPLOADERFLAGS="")
# env.Replace(UPLOADCMD="$UPLOADER $SOURCES " + b64decode(ARGUMENTS.get("UPLOAD_PORT")))
OTAFirmwareName = b64decode(ARGUMENTS.get("PIOENV")) + ".bin"
OTAScpFullPath = b64decode(ARGUMENTS.get("UPLOAD_PORT")) + "/" + OTAFirmwareName
OTAUrl = b64decode(ARGUMENTS.get("OTA_URL_PREFIX")) + "/" + OTAFirmwareName
env.Replace(UPLOADCMD="$UPLOADER $SOURCES " + OTAScpFullPath + "&& echo To " + OTAScpFullPath + "&& echo "+OTAUrl)
