# yuhui-mppt
Made for mppt charginger for Yuhui or Jvyuan ,esphome base on Homeassistant systems
# ESPHome 钰辉 MPPT 控制器组件

[![ESPHome](https://img.shields.io/badge/ESPHome-2026.4.5-blue)](https://esphome.io)

这是为钰辉/聚源 MPPT 太阳能充电控制器编写的 ESPHome 外部组件，支持读取实时数据和设置参数。
欢迎大家TEST,ESPHome Device Builder 当前版本：2026.4.5 测试通过。
## 功能

- 读取 PV 电压、电池电压、充电电流、充电功率、内部温度、外部温度
- 读取设备日发电量、总发电量（kWh）
- 控制：禁止充电开关、DC 输出开关
- 手动设置最大充电电流（0.1A~130A，步进 0.1A）
  
## 修正历史(没有tag分支，只有Main)
 v1.2, 修正mppt的功率计算错误。
 
 v1.1, 修正重启会将充电电流清零默认；
 
 v1.0，第一次发布，带调节电流功能；

## 接线

| ESP8266 | RS485转TTL模块 | MPPT 端子 |
|---------|------------|-----------|
| TX(GPIO1) | Rx-----A | A+ |
| RX(GPIO3) | TX-----B | B- |
| GND | GND | GND |
| 5V | VCC | 可选 |

波特率：9600 8 N 1

## 设备报错：
如果连接正常，读出来的数据为“未知”，esphome窗口传回错误为B3,重点查485转TTL硬件，正常两点灯都亮。

## 更新ESPhome设备版本方法：
 如果以前安装成功的，要更新最新的版本，要重新清理以前的缓存文件，在ESPHome Builder应用里面，找到你的设备卡片，点击卡片右侧或下方的 三个点 ⋮（更多操作），在弹出菜单里找到：
中文界面：“清理构建文件” 或 “清除构建文件”
英文界面：Clean Build Files
清理文件，重新下载编译就行。如果不行，则加一行代码强制更新  refresh: 0s 。

external_components:
  - source: github://sayinzest/Esphome-yuhui-mppt@main
    components: [ yuhui_mppt ]
    refresh: 0s   # 强制每次编译都拉取最新



## 配置Yaml使用方法：

在您的 ESPHome YAML 配置中添加：

```yaml
external_components:
  - source: github://sayinzest/Esphome-yuhui-mppt@main
    components: [ yuhui_mppt ]

uart:
  tx_pin: GPIO1
  rx_pin: GPIO3
  baud_rate: 9600

# 定义传感器、开关、number 等（详见 examples 目录）
