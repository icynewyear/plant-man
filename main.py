from plantman.devices import Thermostat, Valve, Thermometer
from plantman.command import Command, CommandType, SWITCH_CMDS
from plantman.manager import DeviceManager


def main():

  
    cmds = [CommandType.OPEN, CommandType.CLOSE, CommandType.POLL, ]
    therm_cmds = [CommandType.POLL, CommandType.ADJUST, CommandType.SET, ]
    
    
    valve = Valve(cmds)


    dman = DeviceManager()

    valve_id = dman.register_device(valve)
    
    valve_program = [
        Command(valve_id,CommandType.OPEN),
        Command(valve_id,CommandType.POLL, "switch"),
        Command(valve_id,CommandType.CLOSE)
    ]
    
    dman.run_commands(valve_program)
    
    dman.unregister_device(valve_id)
    
if __name__ == "__main__":
    main()
