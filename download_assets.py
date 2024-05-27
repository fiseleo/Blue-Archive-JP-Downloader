import os
import requests
from zipfile import ZipFile
import io
import re
import binascii
import UnityPy
import json
import platform
import subprocess
ROOT = os.path.dirname(os.path.realpath(__file__))
RAW = os.path.join(ROOT, "raw")
EXT = os.path.join(ROOT, "extracted")
VERSION = os.path.join(ROOT, "version.txt")
#資源路徑
resource_path = "https://yostar-serverinfo.bluearchiveyostar.com/r67_jjjg51ngucokd90cuk4l.json"
resource_path2 = "https://prod-noticeindex.bluearchiveyostar.com/prod/index.json"

option = {
    "skipExistingDownloadedResource": True,
    "skipExistingAssets": True
}

def main():
    path = ROOT
    app_id = "com.YostarJP.BlueArchive"
    # 獲取版本
    print("Fetching version")
    if os.path.exists(VERSION):
        with open(VERSION, "rt") as f:
            version = f.read()
    else:
        print("No local version found")
        version = update_apk_version(app_id, path)
    print(version)

    game_files_list = getAllGameFiles()
    for index, file_info in enumerate(game_files_list, start=1):
        file_url, path, crc = file_info
        print("="*30)
        filename = file_url.split("/")[-1]
        # 根據文件類型確定目標路徑
        if filename.endswith('.bundle'):
            dest_path = os.path.join(RAW, filename)
        elif 'TableBundles' in file_url:
            dest_path = os.path.join(EXT, 'TableBundles', filename)
        elif 'MediaResources' in file_url:
            dest_path = os.path.join(EXT, 'MediaResources', path)
        else:
            dest_path = os.path.join(EXT, filename)    
        print(filename)
        while True:
            if option["skipExistingDownloadedResource"] and os.path.isfile(dest_path):
                print("Already downloaded. Skipping.")
                break
            downloadFile(file_url, dest_path)
            calculated_crc = calculate_crc32(dest_path)
            if calculated_crc == crc:
                break
            else:
                print(f"WARNING: CRC32 checksum for %7Bdest_path%7D does not match expected value! Retrying...")
# 計算文件的CRC32校驗和的函數
def calculate_crc32(file_path):
    buf = open(file_path, 'rb').read()
    crc32 = binascii.crc32(buf) & 0xFFFFFFFF
    return crc32
def getBaseResourceURL():
    data = requests.get(resource_path).json()
    print(data)
    return data["ConnectionGroups"][0]['OverrideConnectionGroups'][-1]['AddressablesCatalogUrlRoot']
# 獲取所有遊戲文件的函數
def getAllGameFiles():
    data = []
    base_url = getBaseResourceURL()
    # BundleFiles
    bundle_url = base_url + '/Android/bundleDownloadInfo.json'
    resB = requests.get(bundle_url).json()
    for asset in resB["BundleFiles"]:
        data.append((base_url + '/Android/' + asset["Name"], "", asset.get("Crc", 0)))
   # TableBundles
    TableBundles_url = base_url + '/TableBundles/TableCatalog.json'
    resT = requests.get(TableBundles_url).json()
    for key, asset in resT["Table"].items():  #
        data.append((base_url + '/TableBundles/' + asset["Name"], "", asset.get("Crc", 0)))  
    MediaResources_url = base_url + '/MediaResources/MediaCatalog.bytes'
    if not os.path.exists(RAW):
        os.makedirs(RAW)
    input_file_path = os.path.join(RAW, 'MediaCatalog.bytes')
    response = requests.get(MediaResources_url)
    response.raise_for_status()
    with open(input_file_path, 'wb') as file:
        file.write(response.content)
    output_file_path = os.path.join(EXT, 'MediaResources', 'MediaCatalog.json')
    if platform.system() == 'Windows':
        exe_path = os.path.abspath("MemoryPackDeserializer/MemoryPackDeserializer.exe")
    else:
        exe_path = os.path.abspath("MemoryPackDeserializer/MemoryPackDeserializer")
    subprocess.run([exe_path, input_file_path, output_file_path])
    with open(output_file_path, 'r') as f:
        resM = json.load(f)
    for key, value in resM["Table"].items():
        media_url = base_url + '/MediaResources/' + value["Path"]
        data.append((media_url, value["Path"], value.get("Crc", 0)))  
    return data
# 下載文件
def downloadFile(url, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    src = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(src)

    # 計算CRC32校驗和
    crc32 = calculate_crc32(filename)
    print(f"CRC32 checksum for {filename}: {crc32}")
# 更新APK版本的函數
def update_apk_version(app_id, path):
    print("Downloading the latest APK from QooApp")
    apk_data = download_QooApp_apk(app_id)
    with open(os.path.join(path, "current.apk"), "wb") as f:
        f.write(apk_data)
    print("Extracting app version and API version")
    version = extract_apk_version(apk_data)
    with open(VERSION, "wt") as f:
        f.write(version)
    return version
# 提取APK版本的函數
def extract_apk_version(apk_data):
    with io.BytesIO(apk_data) as stream:
        with ZipFile(stream) as zip:
            # devs are dumb shit and keep moving the app version around
            with zip.open("assets/bin/Data/globalgamemanagers", "r") as f:
                env = UnityPy.load(f)
                for obj in env.objects:
                    if obj.type.name == "PlayerSettings":
                        build_version = re.search(
                            b"\d+?\.\d+?\.\d+", obj.get_raw_data()
                        )[0].decode()
                        return build_version
# 從QooApp下載APK的函數
def download_QooApp_apk(apk_id):
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    query = urlencode(
        {
            "supported_abis": "x86,armeabi-v7a,armeabi",
            "sdk_version": "22",
        }
    )
    res = urlopen(
        Request(
            url=f"https://d1.qoo-apk.com/12252/apk/com.YostarJP.BlueArchive-275921-131992259-1713925384.apk",
            headers={
                "accept-encoding": "gzip",
                "user-agent": "QooApp 8.1.7",
                "device-id": "80e65e35094bedcc",
            },
            method="GET",
        )
    )
    data = urlopen(res.url).read()
    return data

if __name__ == "__main__":
    main()