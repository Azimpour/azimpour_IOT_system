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

st.get_status()
