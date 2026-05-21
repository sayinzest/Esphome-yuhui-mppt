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

## 接线

| ESP8266 | RS485 模块 | MPPT 端子 |
|---------|------------|-----------|
| TX(GPIO1) | Rx-----A | A+ |
| RX(GPIO3) | TX-----B | B- |
| GND | GND | GND |
| 5V | VCC | 可选 |

波特率：9600 8 N 1

## 使用方法

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
