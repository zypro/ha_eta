"""
@name is mandatory, if not defined the original localized name of the variable will be used
@uri is required
@unit is mandatory
@factor is mandatory
"""
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from homeassistant.const import UnitOfTemperature, UnitOfPower, UnitOfMass, UnitOfEnergy

SENSORS_DEFAULT = [
    {
        "uri": "/120/10601/0/0/12197",
        "unit": UnitOfTemperature.CELSIUS
    },
    {
        "uri": "/40/10021/0/0/12077",
        "unit": UnitOfPower.KILO_WATT
    },
    {
        "uri": "/40/10021/0/0/12006",
        "unit": UnitOfTemperature.CELSIUS
    },
    {
        "uri": "/40/10021/0/11109/0",
        "unit": UnitOfTemperature.CELSIUS
    },
    {
        "uri": "/40/10021/0/11110/0",
        "unit": UnitOfTemperature.CELSIUS
    },
    {
        "uri": "/120/10101/0/11125/2121",
        "unit": UnitOfTemperature.CELSIUS
    },
    {
        "uri": "/40/10201/0/0/12015",
        "unit": UnitOfMass.KILOGRAMS
    },
    {
        "uri": "/40/10021/0/0/12016",
        "unit": UnitOfMass.KILOGRAMS
    },
    {
        "name": "Gesamt Energieverbrauch",
        "uri": "/40/10021/0/0/12016",
        "unit": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "factor": 4.8
    },
]
