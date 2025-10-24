from flask import Flask, request, send_file
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Meiryo'

app = Flask(__name__)

@app.route("/plot", methods=["GET"])
def plot_crypto():
    # クエリパラメータから取得
    coins = ["btc", "eth", "sol", "doge", "xrp"]
    data = {
        coin.upper(): float(request.args.get(coin, 0))
        for coin in coins
        if request.args.get(coin)
    }

    # データフレーム化
    df = pd.DataFrame(list(data.items()), columns=["Coin", "Price"])

    # グラフ生成
    plt.figure(figsize=(8, 4))
    df.plot(x="Coin", y="Price", kind="bar", legend=False, color="skyblue")
    plt.title("仮想通貨の価格")
    plt.ylabel("USD")
    plt.tight_layout()
    plt.savefig("crypto_plot.png")

    return send_file("crypto_plot.png", mimetype="image/png")

# 🔽 これを追加！
if __name__ == "__main__":
    app.run(debug=True)