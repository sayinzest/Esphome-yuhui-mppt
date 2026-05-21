import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor, switch, number
from esphome.const import CONF_ID, CONF_ADDRESS, CONF_UPDATE_INTERVAL

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "switch", "number"]

yuhui_mppt_ns = cg.esphome_ns.namespace("yuhui_mppt")
YuhuiMppt = yuhui_mppt_ns.class_("YuhuiMppt", cg.PollingComponent, uart.UARTDevice)

# 传感器
CONF_PV_VOLTAGE_ID = "pv_voltage_id"
CONF_BATTERY_VOLTAGE_ID = "battery_voltage_id"
CONF_CHARGING_CURRENT_ID = "charging_current_id"
CONF_CHARGING_POWER_ID = "charging_power_id"
CONF_INTERNAL_TEMPERATURE_ID = "internal_temperature_id"
CONF_EXTERNAL_TEMPERATURE_ID = "external_temperature_id"
CONF_DAILY_ENERGY_ID = "daily_energy_id"
CONF_TOTAL_ENERGY_ID = "total_energy_id"

# 开关
CONF_DISABLE_CHARGE_SWITCH_ID = "disable_charge_switch_id"
CONF_DC_OUTPUT_SWITCH_ID = "dc_output_switch_id"

# Number
CONF_MAX_CURRENT_NUMBER_ID = "max_current_number_id"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(YuhuiMppt),
    cv.Optional(CONF_ADDRESS, default=1): cv.uint8_t,
    cv.Optional(CONF_UPDATE_INTERVAL, default="5s"): cv.update_interval,
    # 传感器
    cv.Optional(CONF_PV_VOLTAGE_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_BATTERY_VOLTAGE_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_CHARGING_CURRENT_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_CHARGING_POWER_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_INTERNAL_TEMPERATURE_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_EXTERNAL_TEMPERATURE_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_DAILY_ENERGY_ID): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_TOTAL_ENERGY_ID): cv.use_id(sensor.Sensor),
    # 开关
    cv.Optional(CONF_DISABLE_CHARGE_SWITCH_ID): cv.use_id(switch.Switch),
    cv.Optional(CONF_DC_OUTPUT_SWITCH_ID): cv.use_id(switch.Switch),
    # Number
    cv.Optional(CONF_MAX_CURRENT_NUMBER_ID): cv.use_id(number.Number),
}).extend(uart.UART_DEVICE_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
    cg.add(var.set_address(config[CONF_ADDRESS]))

    # 传感器映射
    if CONF_PV_VOLTAGE_ID in config:
        sens = await cg.get_variable(config[CONF_PV_VOLTAGE_ID])
        cg.add(var.set_pv_voltage_sensor(sens))
    if CONF_BATTERY_VOLTAGE_ID in config:
        sens = await cg.get_variable(config[CONF_BATTERY_VOLTAGE_ID])
        cg.add(var.set_battery_voltage_sensor(sens))
    if CONF_CHARGING_CURRENT_ID in config:
        sens = await cg.get_variable(config[CONF_CHARGING_CURRENT_ID])
        cg.add(var.set_charging_current_sensor(sens))
    if CONF_CHARGING_POWER_ID in config:
        sens = await cg.get_variable(config[CONF_CHARGING_POWER_ID])
        cg.add(var.set_charging_power_sensor(sens))
    if CONF_INTERNAL_TEMPERATURE_ID in config:
        sens = await cg.get_variable(config[CONF_INTERNAL_TEMPERATURE_ID])
        cg.add(var.set_internal_temperature_sensor(sens))
    if CONF_EXTERNAL_TEMPERATURE_ID in config:
        sens = await cg.get_variable(config[CONF_EXTERNAL_TEMPERATURE_ID])
        cg.add(var.set_external_temperature_sensor(sens))
    if CONF_DAILY_ENERGY_ID in config:
        sens = await cg.get_variable(config[CONF_DAILY_ENERGY_ID])
        cg.add(var.set_daily_energy_sensor(sens))
    if CONF_TOTAL_ENERGY_ID in config:
        sens = await cg.get_variable(config[CONF_TOTAL_ENERGY_ID])
        cg.add(var.set_total_energy_sensor(sens))

    # 开关映射
    if CONF_DISABLE_CHARGE_SWITCH_ID in config:
        sw = await cg.get_variable(config[CONF_DISABLE_CHARGE_SWITCH_ID])
        cg.add(var.set_disable_charge_switch(sw))
    if CONF_DC_OUTPUT_SWITCH_ID in config:
        sw = await cg.get_variable(config[CONF_DC_OUTPUT_SWITCH_ID])
        cg.add(var.set_dc_output_switch(sw))

    # Number 映射
    if CONF_MAX_CURRENT_NUMBER_ID in config:
        num = await cg.get_variable(config[CONF_MAX_CURRENT_NUMBER_ID])
        cg.add(var.set_max_current_number(num))