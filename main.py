from plantman.devices import WaterFlowController
from plantman.command import Command, CommandType

def main():
    
    close_cmd = Command(CommandType.CLOSE)
    open_cmd = Command(CommandType.OPEN)
    swap_cmd = Command(CommandType.TOGGLE)
    
    waterflow1 = WaterFlowController("Main Water")
    waterflow1.connect()
    
    waterflow1.status_update()
    waterflow1.run_command(open_cmd)
    
    waterflow1.status_update()
    waterflow1.run_command(swap_cmd)
    
    waterflow1.status_update()
    
    waterflow1.disconnect()
    
if __name__ == "__main__":
    main()
