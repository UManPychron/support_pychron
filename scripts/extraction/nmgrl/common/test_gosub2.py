# Auto Generated Gosub
# Source: from /Users/ross/Pychron_dev/scripts/extraction/jan_air_x1.py
# Date: 02-23-2015 01:01
def main():
    gosub('common:FillPipette2')
    gosub('jan:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    close(description='Outer Pipette 2')
