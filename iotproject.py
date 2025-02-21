
'''
APM:

do bar neveshtid get_status function ro
eslah shod mamnon


--> Bale baraye sensor bayad yek class jdoa tarif kard ke yek tabe dashte bashe be name read_data va mitone haal yek adade 
random ya yek adade sabet harbar sedash mizanim befreste

ostad taghirato ijad kardam alan doroste hamechi?



APM:
salam faghat Task1 ro anjam nadadi ke bayad class Device() ro real world ba estefade az
ketabkhone gpio va .. , bayad biayd va yek devcie type e jadid behesh ezafe konid
moafagh bashid

salam ostad
yani hamontor ke khodeton neveshte bodid?

mishe chek konin mamnonm

************************
************************
ostad mamnon az vaghti ke gozashtin man ta jaei ke balad bodam taghirato ijad kardam
mamnon misham chek konin
*************************
***************************




APM:
Ahsant kamelan okeye khaste nabashid

'''

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt


class Device():
    
    def __init__(self,topic):

        self.topic=topic
        self.topic_list=topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.status='off'
        self.gpio_pin = self.get_gpio_pin()
        self.setup_gpio()

     def get_gpio_pin(self):
        gpio_pins = {'lights': 17, 'doors': 27, 'fans': 22}
        return gpio_pins.get(self.device_type, None)

    def setup_gpio(self):
        if self.gpio_pin is not None:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio_pin, GPIO.OUT)


    def turn_on(self):
        if self.gpio_pin is not None:
            GPIO.output(self.gpio_pin, GPIO.HIGH)
        self.status='on'
        
        print(f'{self.name} is turned on')
        

    def turn_off(self):
        if self.gpio_pin is not None:
            GPIO.output(self.gpio_pin, GPIO.LOW)
        self.status='off'
        
        print(f'{self.name} is turned off')
        

    def get_status(self):
        return self.status
        



class Sensor():
    def __init__(self, sensor_type, name):
        self.sensor_type=sensor_type
        self.name=name

    def get_data(self):
        return {"temperature": 25, "humidity": 60}



class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]={'devices': [], 'sensors': []}
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
        
        
    def add_device_to_group(self,group_name,device):
        
        if group_name in self.groups:
            self.groups[group_name]['devices'].append(device)
            print(f'{device.name} was added to the {group_name} group')
   
        else:
            print('your group is not created')

    
    def remove_device_from_group(self,group_name,device_name):  #tabe entekhabi
        if group_name in self.groups:
            devices = self.groups[group_name]['devices']
            for device in devices:
                if device.name == device_name:
                    devices.remove(device)
                    print(f'{device.name} was remove from {group_name}')
                    return
            
            print(f'{device.name} not in {group_name}')
        else:
            print(f'{group_name} has not been created yet')

    
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'device {new_device.name} is created')
            
        else:
            print(f'{group_name} has not been created yet')


    def create_multiple_devices(self,group_name,device_type,number_of_devcies):
        
        if group_name in self.groups:
            
            for i in range(1,number_of_devcies+1):

                device_name=f'{device_type}{i}'
                topic=f'home/{group_name}/{device_type}/{device_name}'
                new_device=Device(topic)
                self.add_device_to_group(group_name, new_device)
                print(f'{device_name} was added to the {group_name} group')

        else:
            print(f'{group_name} has not been created yet')


    def get_devices_in_groups(self,group_name):
        if group_name in self.groups:
            return self.groups[group_name]['devices']
            
        else:
            print(f'the {group_name} group does not exist')
            return []


    def turn_on_all_in_groups(self,group_name):
        
        devices=self.get_devices_in_groups(group_name)
        
        for device in devices:
            device.turn_on()

    def turn_off_all_in_groups(self,group_name):

        devices=self.get_devices_in_groups(group_name)

        for device in devices:
            device.turn_off() 
            
    
    def turn_on_all_devices(self):

        for devices in self.groups.items():
            for device in devices:
                device.turn_on()

    def turn_off_all_devices(self):

        for devices in self.groups.items():
            for device in devices:
                device.turn_off()


    def get_status_in_group(self,group_name):

        devices = self.get_devices_in_groups(group_name)
        if devices:
            for device in devices:
                status = device.get_status()
                print(f'Device {device.name} in group {group_name} is {status}')
                print('-------------------------------------------------------')
 
    
    
    def get_status_in_device_type(self,device_type):
        
        for group_name, devices in self.groups.items():
            for device in devices:
                
                if device.device_type.strip().lower() == device_type:
                    status = device.get_status()
                    print(f'{device.name} in {group_name} is {status}')



    def create_sensor(self, group_name, sensor_type, name):
        if group_name in self.groups:
            sensor=Sensor(sensor_type, name)
            self.add_sensor_in_group(group_name, sensor)
            print(f'Sensor {sensor.name} of type {sensor_type}  is created in group {group_name}')
        else:
            print(f'{group_name} has not been created yet')

    
    def add_sensor_in_group(self,group_name,sensor):
        if group_name in self.groups:
           self.groups[group_name]['sensors'].append(sensor)
           print(f'{sensor.name} was added to the {group_name} group')
        else:
           print(f'{group_name} has not been created yet')


    #ahsant 
    def get_data_from_sensor_in_group(self, group_name): 
        if group_name in self.groups:
            sensors = self.groups[group_name]['sensors']
            if not sensors:
               print(f"No sensors found in group '{group_name}'.")
               return []
        
            sensor_data = {sensor.name: sensor.get_data() for sensor in sensors}
            print(f"Sensor data from group '{group_name}': {sensor_data}")
            return sensor_data
        else:
            print(f'{group_name} has not been created yet')
            return []
            
                #injaa mire tooye group harchi peyda krd ro .get_data() mikone
                #ma too yek group momkene ma device dashte bashim , sensor va ..
                #aval bayad ba yek if check kone ke sensoree ya na
                #age sensor bashe haal mitonim sensor_get_data bashe
                #bad bejaye return --> print kone
    

    def find_device_location(self, device_name, device_type): #tabe entekhabi
        for group_name, group_data in self.groups.items():
            for device in group_data['devices']:
                if device.name == device_name and device.device_type == device_type:
                   print(f"Device '{device_name}' of type '{device_type}' is in group '{group_name}'.")
                   return group_name 
        print(f"Device '{device_name}' of type '{device_type}' not found in any group.")
        return None


    def show_menu(self):
        while True:
            print("\n1. Create Group")
            print("2. Add Device")
            print("3. Turn On All Devices in Group")
            print("4. Turn Off All Devices in Group")
            print("5. Add Sensor")
            print("6. Get Sensor Data")
            print("7. Create Multiple Devices")
            print("8. Find Device Location")
            print("9. Remove Device from Group")
            print("10. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                group_name = input("Enter group name: ").strip()
                self.create_group(group_name)
           
            elif choice == "2":
                group_name = input("Enter group name: ").strip()
                device_type = input("Enter device type: ").strip()
                device_name = input("Enter device name: ").strip()
                self.create_device(group_name, device_type, device_name)
           
            elif choice == "3":
                group_name = input("Enter group name: ")
                self.turn_on_all_in_group(group_name)
           
            elif choice == "4":
                group_name = input("Enter group name: ")
                self.turn_off_all_in_group(group_name)
           
            elif choice == "5":
                group_name = input("Enter group name: ")
                sensor_type = input("Enter sensor type: ")
                sensor_name = input("Enter sensor name: ")
                self.create_sensor(group_name, sensor_type, sensor_name)
           
            elif choice == "6":
                group_name = input("Enter group name: ")
                self.get_data_from_sensors_in_group(group_name)
           
            elif choice == "7":
                group_name = input('Please enter group name for multiple devices: ').strip()
                device_type = input('Please enter device type: ').strip()
                number_of_devices = int(input('Please enter the number of devices you want to create: '))
                self.create_multiple_devices(group_name, device_type, number_of_devices)
            
            elif choice == "8":  
                device_name = input('Please enter the device name to find its location: ').strip()
                device_type = input('Please enter the device type: ').strip()
                self.find_device_location(device_name, device_type)

            elif choice == "9":  
                group_name = input("Enter group name: ").strip()
                device_name = input("Enter the device name to remove: ").strip()
                self.remove_device_from_group(group_name, device_name)

            elif choice == "10":
                break

            else:
                print("Invalid option, try again")


admin=admin_panel()
admin.show_menu()
GPIO.cleanup()


