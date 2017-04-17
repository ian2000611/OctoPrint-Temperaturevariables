# temperatureVariables

Scans gcode to find first layer temperatures for the bed and hot end and create
s variables that can be used in a startup script.

In startup gcode use {{ event.bedFirstLayerTemperature }} and {{ event.headFirstLayerTemperature }}

