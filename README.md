<!--
    README
 -->

# Pyside Convert Video App

<!-- [![English](https://img.shields.io/badge/English-018EF5.svg?labelColor=d3d3d3&logo=readme)](./README.md) -->
<!-- [![Japanese](https://img.shields.io/badge/Japanese-018EF5.svg?labelColor=d3d3d3&logo=readme)](./README_JA.md) -->
[![Japanese](https://img.shields.io/badge/Japanese-018EF5.svg?labelColor=d3d3d3&logo=readme)](./README.md)
[![license](https://img.shields.io/github/license/r-dev95/pyside-convert-video-app)](./LICENSE)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

[![Python](https://img.shields.io/badge/Python-3776AB.svg?labelColor=d3d3d3&logo=python)](https://github.com/python)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
<!-- [![Sphinx](https://img.shields.io/badge/Sphinx-000000.svg?labelColor=d3d3d3&logo=sphinx&logoColor=000000)](https://github.com/sphinx-doc/sphinx) -->
<!-- [![Pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?labelColor=d3d3d3&logo=pytest)](https://github.com/pytest-dev/pytest) -->

ビデオのフォーマット変換を行うためのPysideを用いたGUIアプリです。

ビデオの変換は、`ffmpeg`コマンドを`subprocess`で実行しています。

## Getting started

### githubからインストール

```bash
git clone https://github.com/r-dev95/pyside-convert-video-app.git
```

### ffmpegのインストール

本アプリは[`ffmpeg`](https://ffmpeg.org/)を使用するので、インストールしてください。

### アイコンの準備

アイコンに[Feather](https://github.com/feathericons/feather)を使用しています。

ダウンロードしたアイコンを`pyside-convert-video-app/src/lib/ui/icons/`に展開してください。

`pyside-convert-video-app/src/lib/ui/icons/feather/***.svg`となっていればOKです。

### 仮想環境の構築

`uv`がインストールされていることが前提です。

pythonの開発環境がまだ整っていない方は、[こちら](https://github.com/r-dev95/env-python)。

```bash
cd pyside-convert-video-app/
uv sync
```

### 実行

```bash
cd src
python app.py
```

## 画面と機能

![アプリ画面](docs/image/demo.gif)

|項目           |機能説明                               |
| ---           | ---                                   |
|選択ボタン     |変換元のファイルを選択。               |
|実行ボタン     |変換後のファイルを選択し、変換を実行。 |
|変換前後ボタン |再生するビデオを選択。                 |
|ビデオ情報欄   |変換元ファイルの情報を表示。           |
|設定欄         |切り抜く時間及び画面範囲を設定。       |
|ログ           |ログを出力。                           |
|自動スクロール |ログを自動スクロール。                 |
|再生ボタン(▷)  |ビデオを再生。                         |
|一時停止ボタン |ビデオを一時停止。                     |

## 使い方

* 選択ボタンを押して、変換元のファイルを選択します。
* 切り抜く時間及び画面範囲を設定します。
* 実行ボタンを押して、変換後のファイルを選択します。

`ffmpeg`コマンドを用いた変換処理が実行されます。

例えば、`.mp4`から`.gif`に変換したい場合、変換後のファイル名に`.gif`をつけると変換されます。(`ffmpeg`の仕様)

## ライセンス

本リポジトリは、[MIT License](LICENSE)に基づいてライセンスされています。
