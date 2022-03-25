from plantman.devices import Thermostat, Valve, Thermometer
from plantman.command import Command, CommandType, SWITCH_CMDS
from plantman.manager import DeviceManager


def main():

    cmds = [CommandType.OPEN, CommandType.CLOSE, CommandType.POLL, ]
    therm_cmds = [CommandType.POLL, CommandType.ADJUST, CommandType.SET, ]

    valve = Valve()
    thermo = Thermostat()
    therm = Thermometer()

    dman = DeviceManager()

    valve_id = dman.register_device(valve)
    therm_id = dman.register_device(therm)
    thermo_id = dman.register_device(thermo)

    valve_program = [
        Command(valve_id, CommandType.OPEN),
        Command(valve_id, CommandType.CLOSE),
        Command(valve_id, CommandType.TOGGLE),
    ]
    thermo_program = [
        Command(thermo_id, CommandType.ADJUST, "8"),
        Command(thermo_id, CommandType.SET, "20"),
    ]
    therm_program = [
        Command(therm_id, CommandType.POLL, "temp_sensor"),
    ]

    dman.run_commands(valve_program)
    dman.run_commands(thermo_program)
    dman.run_commands(therm_program)

    dman.unregister_device(valve_id)
    dman.unregister_device(thermo_id)
    dman.unregister_device(therm_id)


if __name__ == "__main__":
    main()
