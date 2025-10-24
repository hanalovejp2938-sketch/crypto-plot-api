from flask import Flask, request, send_file, jsonify
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm
import os

app = Flask(__name__)

@app.route("/plot", methods=["POST"])
def plot_crypto():
    # JSONデータを受け取る
    data = request.get_json()

    # データがない場合はエラー
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # データ整形
    df = pd.DataFrame(list(data.items()), columns=["Coin", "Price"])

    # 日本語フォント設定（Render対応）
    font_path = "fonts/IPAexGothic.ttf"
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams["font.family"] = font_prop.get_name()

    # グラフ生成
    plt.figure(figsize=(8, 4))
    df.plot(x="Coin", y="Price", kind="bar", legend=False, color="skyblue")
    plt.title("仮想通貨の価格")
    plt.ylabel("USD")
    plt.tight_layout()
    plt.savefig("crypto_plot.png")

    return send_file("crypto_plot.png", mimetype="image/png")
