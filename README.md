# OctoPrint-Filamentloading

Scans gcode to find first layer temperatures for the bed and hot end and creates variables that can be used in a startup script.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/ian2000611/OctoPrint-Filamentloading/archive/master.zip


## Configuration

In your startup g-gcode script use {{ event.bedFirstLayerTemperature }} and/or {{ event.headFirstLayerTemperature }} as needed
