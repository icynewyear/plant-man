from plantman.devices import Thermostat, Valve, Thermometer
from plantman.command import Command, CommandType, SWITCH_CMDS


def main():

    close_cmd = Command(CommandType.CLOSE)
    open_cmd = Command(CommandType.OPEN)
    swap_cmd = Command(CommandType.TOGGLE)
    temp_poll_cmd = Command(CommandType.POLL, 'temp_sensor')
    temp_inc_cmd = Command(CommandType.ADJUST, '-10')

    cmds = [CommandType.OPEN, CommandType.CLOSE, CommandType.POLL, ]
    therm_cmds = [CommandType.POLL, CommandType.ADJUST, CommandType.SET, ]

    waterflow1 = Valve(SWITCH_CMDS, "Main Water")
    therm1 = Thermometer(fahrenheit=True)
    thermostat1 = Thermostat(therm_cmds)

    thermostat1.run_command(Command(CommandType.POLL, 'dial'))

    thermostat1.run_command(temp_inc_cmd)

    thermostat1.run_command(Command(CommandType.POLL, 'dial'))

    thermostat1.run_command(Command(CommandType.SET, '42'))
    thermostat1.run_command(Command(CommandType.POLL, 'dial'))

    waterflow1.connect()
    therm1.connect()

    waterflow1.run_command(Command(CommandType.POLL, 'switch'))
    waterflow1.run_command(swap_cmd)

    waterflow1.run_command(open_cmd)
    waterflow1.run_command(Command(CommandType.POLL, 'allowedCommands'))

    therm1.run_command(temp_poll_cmd)

    waterflow1.status_update()
    therm1.status_update()

    therm1.disconnect()
    waterflow1.disconnect()


if __name__ == "__main__":
    main()
