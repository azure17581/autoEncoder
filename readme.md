# autoEncoder
指定フォルダ直下の動画ファイルを ffmpeg で圧縮し，直下の `encoded` フォルダに保存するスクリプト。  
（ファイルパスの処理が適切でないためおそらく `windows` でしか動かない）  
iPad や PC でキャプチャしたゲームのプレイ動画などに効果的。動画の品質をほとんど変えることなくファイルサイズを 1/5 程度まで減らせる場合もある。

### 注意
- **元のファイルのメタデータを書き換えることがあります。ファイルに変更を加えたくない場合は使わないでください。**
- パソコンのスペックによっては処理に非常に時間がかかる場合があります。  

## 必要なもの
- [ffmpeg](https://ffmpeg.org/)
- [mutagen](https://pypi.org/project/mutagen/)

## 導入 (Windows)
- ffmpeg を [こちら](https://ffmpeg.org/) からダウンロード/インストール。
- `autoEncoder.py` の `YOUR ffmpeg.exe PATH` を `ffmpeg.exe` のフルパスで置き換える。
- `pip` で `mutagen` をインストール  
```
pip install mutagen
```

## 使い方
- `autoEncoder.py` を実行し，対象のフォルダをそこにドロップして `Enter`。

フォルダ内のすべての動画ファイルが圧縮される。そのフォルダの子フォルダ内の動画は対象としない。  
動画のメタデータの `コメント` が `compressed by ffmpeg` であるものや，`encoded` フォルダに同名のファイルがあるものはスキップする。これによって既に `autoEncoder.py` が圧縮したファイルが再度対象になることを避ける。