import csv
from matplotlib import pyplot as plt
x_list=[]
y_list = []
x_list2=[]
y_list2=[]
def graph_maker():
      plt.rcParams['font.size'] = 14
      plt.rcParams['font.family'] = 'Times New Roman'
      
      # 目盛を内側にする。
      plt.rcParams['xtick.direction'] = 'in'
      plt.rcParams['ytick.direction'] = 'in'
      
      # グラフの上下左右に目盛線を付ける。
      fig = plt.figure()
      ax1 = fig.add_subplot(111)
      ax1.yaxis.set_ticks_position('both')
      ax1.xaxis.set_ticks_position('both')
      
      # スケール設定
      ax1.set_xlim(0, 400)
      ax1.set_ylim(0, 400)
      
      # 軸のラベルを設定する。
      ax1.set_xlabel('x(px)')
      ax1.set_ylabel('y(px)')
      
      # データプロット
      ax1.scatter(x_list2,y_list2, label='Tracking place')
      
      plt.legend()
      fig.tight_layout()
      
      # グラフを表示する。
      plt.show()
      plt.close()

def neograph_maker():
      plt.rcParams['font.size'] = 14
      plt.rcParams['font.family'] = 'Times New Roman'
      
      # 目盛を内側にする。
      plt.rcParams['xtick.direction'] = 'in'
      plt.rcParams['ytick.direction'] = 'in'
      
      # グラフの上下左右に目盛線を付ける。
      fig = plt.figure()

      
      # スケール設定
      plt.yticks(range(0,400))
      
      # 軸のラベルを設定する。
      plt.xlabel('x')
      plt.ylabel('y')
      
      # データプロット
      plt.plot(x_list2,y_list2, label='Tracking place')
      plt.legend()
      fig.tight_layout()
      
      # グラフを表示する。
      plt.show()
      plt.close()

with open("point.csv") as f:
   reader = csv.reader(f)
   for row in reader:
      x_list.append(int(row[0]))
      y_list.append(int(row[1]))
with open("point2.csv") as f:
   reader = csv.reader(f)
   for row in reader:
      x_list2.append(int(row[0]))
      y_list2.append(int(row[1]))
graph_maker()

   