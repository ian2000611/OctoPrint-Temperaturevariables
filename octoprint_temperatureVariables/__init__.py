# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin
import re

class TemperaturevariablesPlugin(octoprint.plugin.EventHandlerPlugin,
                                 octoprint.plugin.TemplatePlugin):

	def __init__(self):
		self.bedFirstLayer=0
		self.headFirstLayer=0
	
	def get_template_vars(self):
		return {'bedFirstLayerTemperature':self.bedFirstLayer,'headFirstLayerTemperature':self.headFirstLayer}

	def on_event(self, event, payload):
		if (event=='PrintStarted'):
			if (self.bedFirstLayer!=0):
				payload['bedFirstLayerTemperature'] = self.bedFirstLayer
			if (self.headFirstLayer!=0):
				payload['headFirstLayerTemperature'] = self.headFirstLayer
		if (event=='FileSelected'):
			self.bedFirstLayer=0
			self.headFirstLayer=0
			if (payload['origin']=='local'):
				pattern = re.compile("(M1[09][09]).*[SR]([0-9]+)")
				with open(self._file_manager.path_on_disk(payload['origin'],payload['path']),'r') as file:
					while (self.bedFirstLayer==0 or self.headFirstLayer==0):
						line = file.readline()
						match = pattern.search(line)
						if (match!=None):
							if (match.group(1)=="M190"):
								self.bedFirstLayer=match.group(2)
							if (match.group(1)=="M109"):
								self.headFirstLayer=match.group(2)
				file.close()

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			temperatureVariables=dict(
				displayName="Temperature Variables Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="ian2000611",
				repo="OctoPrint-Temperaturevariables",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/ian2000611/OctoPrint-Temperaturevariables/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Temperaturevariables Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = TemperaturevariablesPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

