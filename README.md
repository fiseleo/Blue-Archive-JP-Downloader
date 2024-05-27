# Blue Archive JP downloader
# "Blue Archive" is a registered trademark of NAT GAMES Co., Ltd. and Yostar Co., Ltd. This repository is not affiliated with NEXON Korea Corp., NEXON GAMES Co., Ltd., and Yostar Co., Ltd. All game resources are copyrighted to their respective owners.
A small project that downloads all assets of the Japan-Server version of Blue Archive and extracts them while it's at it.
The script updates the assets and even its own parameters on its own,
so all you have to do is execute the download_assets.py script after every update to get the latest files.


[中文](<https://github.com/fiseleo/Blue-Archive-JP-Downloader/blob/main/README%E4%B8%AD%E6%96%87.md> "Title")

## Requirements

- Python 3.9.13+
- UnityPy 1.7.21
- requests
- xxhash
- pycryptodome
- flatbuffers
- [.NET8.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)

# Scripts

- ``download_assets.py``
  - This script downloads and extracts the latest assets.
  - "Switched to JP Server."
- ``extract_tables.py``
  - Extracts and decrypts the tables from the zip files in ``TableBundles``
  - due to the way it works, this script can take ages, around 15 minutes.
- ``flatbuf_schema_generator.py``
- Cannot use.
  
# Reference & Thank
https://github.com/lwd-temp/blue-archive-spine-production  
Offer my thoughts.  
Report from Pscgylotti.  
https://github.com/K0lb3/Blue-Archive---Asset-Downloader/issues/5

# This project is not updated
please come  [NewDownloader](<https://github.com/fiseleo/BlueArchiveDownloaderJP/tree/main> "Title")
