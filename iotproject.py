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
