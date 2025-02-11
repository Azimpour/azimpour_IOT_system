
'''
APM:

do bar neveshtid get_status function ro
eslah shod mamnon



--> Bale baraye sensor bayad yek class jdoa tarif kard ke yek tabe dashte bashe be name read_data va mitone haal yek adade 
random ya yek adade sabet harbar sedash mizanim befreste


'''


class Device():
    
    def __init__(self,topic):

        self.topic=topic
        self.topic_list=topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.status='off'


    def turn_on(self):
        
        self.status='on'
        
        print(f'{self.name} is turned on')
        

    def turn_off(self):

        self.status='off'
        
        print(f'{self.name} is turned off')
        

    def get_status(self):
        return self.status
        
    
topic=input('please enter (location/group/device_type/name):')
dev=Device(topic)
print(f' {topic} is created')


name_device=input('please enter your device name:')
st=input('turn off or turn on?')

if st=='turn on':
   topic.turn_on()
elif st=='turn off':
    topic.turn_off()

print(f'status{dev.name}: {dev.get_status}')


class Sensor():
    def __init__(self, name):
        self.name=name

    def get_data(self):
        return 25

'''
mitoonid az in estefade konid
class Sensor():
    def __init__(self, name):
        self.name=name


    def get_data(self):
        return 25


'''

class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
        
        
    def add_device_to_group(self,group_name,device):
        
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'{device} was added to the {group_name} group')
   
        else:
            print('your group is not created')

    
    def remove_device_from_group(self,group_name,device):
                if group_name in self.groups:
                    if device in self.groups[group_name]:
                        self.groups[group_name].remove(device)
                        print(f'{device} was remove from {group_name}')
                    else:
                        print(f'{device} not in {group_name}')
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
            return self.groups[group_name] 
            
            
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
                #****** APM: inja bayad turn_off bezanid bejaye turn_on
                #eslah shod mamnon
                device.turn_off()


    def get_status_in_group(self,group_name):

        devices = self.get_devices_in_groups(group_name)
        if devices:
            for device in devices:
                status = device.get_status()
                #yek print ezafe kardam visible tar beshe
                #mamnon
                print(f'Device {device.name} in group {group_name} is {status}')
                print('-------------------------------------------------------')
 
    
    
    def get_status_in_device_type(self,device_type):
        
        for group_name, devices in self.groups.items():
            for device in devices:
                #inja mitonid bejaye device_type biadyd benevisid device_type.strip().lower() k user eshtebah ham kard in javab bede
                #eslah shod mamnon
                if device.device_type.strip().lower() == device_type:
                    status = device.get_status()
                    print(f'{device.name} in {group_name} is {status}')

#baraye sensor bayad class joda tarif konam ?




    def create_sensor(self, group_name, sensor_name):
        if group_name in self.groups:
            #age oon bala sensor ro avaz kridd inja ham havasetoon b vorodi ha bashe ****
            new_sensor=Sensor(sensor_name)
            self.add_sensor_in_group(group_name, new_sensor)
            print(f'Sensor {new_sensor} of type {sensor_type}  is created in group {group_name}')
        else:
            print(f'{group_name} has not been created yet')

    
    def add_sensor_in_group(self,group_name,sensor):
        if group_name in self.groups:
           self.groups[group_name].append(sensor)
           print(f'{sensor.name} was added to the {group_name} group')
        else:
           print(f'{group_name} has not been created yet')

    def get_data_from_sensor_in_group(self, group_name):  #injaro nmidonm doroste ya na
        if group_name in self.groups:
            for sensor in self.groups[group_name]:
                #injaa mire tooye group harchi peyda krd ro .get_data() mikone
                #ma too yek group momkene ma device dashte bashim , sensor va ..
                #aval bayad ba yek if check kone ke sensoree ya na
                #age sensor bashe haal mitonim sensor_get_data bashe
                #bad bejaye return --> print kone
                sensor_data = [sensor.get_data()]
            return sensor_data
            
        else:
           print(f'{group_name} has not been created yet')
        return []


admin=admin_panel()

group_name=input('please enter group name: ').strip()
admin.create_group(group_name)


device_type=input('please enter device type: ').strip()
device_name=input('please enter device name: ').strip()
admin.create_device(group_name,device_type,device_name)


group_to_turn_on=input('please enter name of group you want to turn on the devices: ').strip()
admin.turn_on_all_in_groups(group_to_turn_on)

group_to_turn_off=input('please enter name of group you want to turn off the devices: ').strip()
admin.turn_off_all_in_groups(group_to_turn_off)


sensor_name=input('please enter sensor name: ').strip()
admin.create_sensor(group_name, sensor_name)

group_to_get_data=input('please enter the name of group you want to get sensor data: ').strip()
admin.get_data_from_sensor_in_group(group_to_get_data)
