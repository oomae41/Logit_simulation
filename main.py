import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
m = 20  # 区間の数
num_samples = 10000  # サンプル数
a = 100  # 一様分布の範囲 [-a, a]

# 一様乱数 X_i を生成
# X_i = np.random.uniform(-a, a, num_samples)
X_i = np.random.normal(-1, 1, num_samples)

# ロジスティック関数を適用して Y_i を計算
Y_i = 1 / (1 + np.exp(-X_i))

# Y_i の値を m 等分した区間に振り分けてヒストグラムを作成
plt.hist(Y_i, bins=m, edgecolor='black', density=True)
plt.xlabel('Y_i の値')
plt.ylabel('確率密度')
plt.title(f'Y_i = 1 / (1 + exp(-X_i)) のヒストグラム (区間数: {m}, サンプル数: {num_samples})')
plt.grid(True)
plt.show()
