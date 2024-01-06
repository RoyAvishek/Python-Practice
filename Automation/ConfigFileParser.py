# Configuration File Parser: Develop a program that reads a 
# configuration file (e.g., YAML or JSON) and extracts specific settings or parameters.

import yaml

def parse_config_file(config_file, settings):
    # Load the YAML configuration file
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    # Extract specific settings from the configuration
    extracted_settings = {}
    for setting in settings:
        try:
            value = config[setting]
            extracted_settings[setting] = value
        except KeyError:
            extracted_settings[setting] = None

    return extracted_settings

# Specify the path or filename of the configuration file
config_file = "config.yaml"

# Specify the settings or parameters to extract
settings = ["database", "username", "port"]

# Parse the configuration file and extract the desired settings
extracted_settings = parse_config_file(config_file, settings)

# Print the extracted settings
print("Extracted Settings:")
for setting, value in extracted_settings.items():
    print(f"{setting}: {value}")

