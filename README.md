# Naviguider-SimpleSerial

**Naviguider-SimpleSerial** is a library for encoding commands and decoding responses using the PNI Sensor SimpleSerial ASCII protocol used by their Naviguider-UART and Headway products. It is a simple library for wrapping commands with more memorable function names and converting responses into dataclasses for easier handling.

```python
>>> from serial import Serial
>>> from naviguider_simpleserial import (
...     decode_line,
...     encode_set_rotation_vector_sensor_rate,
...     encode_system_restart,
... )
>>> serial_port = Serial("/dev/ttyUSB0", 115200)
>>> serial_port.write(encode_system_restart().encode())
1
>>> serial_port.write(encode_set_rotation_vector_sensor_rate(30).encode())
7
>>> while True:
...     data = serial_port.readline().decode("utf-8").strip()
...     if data:
...             event = decode_line(data)
...             if event:
...                     print(event)
... 
WakeupEvent(ticks=342)
SampleRateChangedMetaEvent(ticks=2372, sensor=<Sensor.ACCELEROMETER: 2>)
DynamicRangeChangedMetaEvent(ticks=2392, sensor=<Sensor.ACCELEROMETER: 2>)
DynamicRangeChangedMetaEvent(ticks=2392, sensor=<Sensor.LINEAR_ACCELERATION: 11>)
DynamicRangeChangedMetaEvent(ticks=2392, sensor=<Sensor.GRAVITY: 10>)
DynamicRangeChangedMetaEvent(ticks=2392, sensor=<Sensor.TEMPERATURE: 5>)
DynamicRangeChangedMetaEvent(ticks=2447, sensor=<Sensor.MAGNETOMETER: 1>)
SampleRateChangedMetaEvent(ticks=2456, sensor=<Sensor.MAGNETOMETER: 1>)
DynamicRangeChangedMetaEvent(ticks=2447, sensor=<Sensor.MAGNETOMETER_UNCALIBRATED: 13>)
MagnetometerSensorEvent(ticks=2685, x=-24.536133, y=-21.655273, z=-39.477539, accuracy=0.0)
SampleRateChangedMetaEvent(ticks=4214, sensor=<Sensor.GYROSCOPE: 3>)
DynamicRangeChangedMetaEvent(ticks=4287, sensor=<Sensor.GYROSCOPE: 3>)
DynamicRangeChangedMetaEvent(ticks=4287, sensor=<Sensor.GYROSCOPE_UNCALIBRATED: 15>)
MagnetometerSensorEvent(ticks=4436, x=-23.339844, y=-22.265625, z=-39.111328, accuracy=0.0)
MagnetometerSensorEvent(ticks=6181, x=-23.266602, y=-21.118164, z=-39.575195, accuracy=0.0)
MagnetometerSensorEvent(ticks=7927, x=-24.145508, y=-20.751953, z=-39.916992, accuracy=0.0)
GyroscopeSensorEvent(ticks=9129, x=0.0, y=0.002131, z=0.0, accuracy=3.0)
MagTransientMetaEvent(ticks=296700, transient_detected=True)
RotationVectorSensorEvent(ticks=298544, qx=0.064392, qy=-0.100464, qz=-0.843201, qw=0.524231, accuracy=-2.49617)
RotationVectorSensorEvent(ticks=299188, qx=0.064392, qy=-0.100464, qz=-0.843201, qw=0.524231, accuracy=-2.49617)
RotationVectorSensorEvent(ticks=299831, qx=0.064453, qy=-0.100464, qz=-0.843201, qw=0.524231, accuracy=-2.49617)
RotationVectorSensorEvent(ticks=300474, qx=0.064392, qy=-0.100464, qz=-0.843201, qw=0.524231, accuracy=-2.49617)
RotationVectorSensorEvent(ticks=301117, qx=0.064392, qy=-0.100464, qz=-0.843201, qw=0.524231, accuracy=-2.49617)

```

## Installation

Naviguider-SimpleSerial is not available on PyPI, but it can be installed from the GitHub repository:

```console
$ python -m pip install git+ssh://git@github.com/pnisensor/lib-naviguider-simpleserial-py
```

## Device Support

This library is intended for use with the following devices from [PNI Sensor](https://www.pnicorp.com):

* Naviguider-UART
* Headway

## API Documentation

API documentation can be found on [readthedocs](https://lib-naviguider-simpleserial-py.readthedocs.io/en/latest/).
