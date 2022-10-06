from batteryModule import batteryModule
from serialUtility import Ser, inst

class batteryPack:
    def __init__(self):
        pass

    def reset(self):
        # broadcast to set the address of boards to 0
        # and then assign address start from 1
        command = bytes([0x3F << 1]) + bytes([0x3C]) + bytes([0xA5])
        for _ in range(3): # give 3 attemps
            response = Ser.query(command, 4, True)
            if response[0]==0x7F and response[1]==0x3c and response[2]==0xa5:
                print("Reset successful")
                break
        self.setBoardAddr()

    def setBoardAddr(self):
        pass

    def clearFaults(self):
        # broadcast to clear the faults and alerts caused by reset
        field0 = 0x7f                       # broadcast
        field1 = inst['REG_ALERT_STATUS']   # alert status
        field2 = 0xff                       # cause reset
        command = bytes([field0]) + bytes([field1]) + bytes([field2])
        Ser.query(command, 4, True) 

        field2 = 0x00                       # write 0 to register
        command = bytes([field0]) + bytes([field1]) + bytes([field2])
        Ser.query(command, 4, True) 

        field0 = 0x7f                       # broadcast
        field1 = inst['REG_FAULT_STATUS']   # fault status
        field2 = 0xff;                       # cause reset
        command = bytes([field0]) + bytes([field1]) + bytes([field2])
        Ser.query(command, 4, True) 

        field2 = 0x00                       # write 0 to register
        command = bytes([field0]) + bytes([field1]) + bytes([field2])
        Ser.query(command, 4, True) 

        print("Clear faults")

