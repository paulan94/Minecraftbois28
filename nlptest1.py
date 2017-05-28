import MalmoPython
import os
import sys
import time
import random
import json
import math
import text_movement
from collections import defaultdict
import classBasedMovement
import displayGUI


sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

items = {'red_flower':'flower',
         'apple':'apple',
         'iron_sword':'sword',
         'iron_pickaxe':'pickaxe',
         'diamond_sword':'sword'
         }

#MOB_TYPE = "Pig"
#spawn_end_tag = ' type="mob_spawner" variant="' + MOB_TYPE + '"/>'

#obj_id = items.keys()[random.randint(0, len(items)-1)]

mission_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <About>
    <Summary>Name the first item you see.</Summary>
  </About>

  <ServerSection>
      <ServerInitialConditions>
            <Time>
                <StartTime>6000</StartTime>
                <AllowPassageOfTime>false</AllowPassageOfTime>
            </Time>
            <Weather>clear</Weather>
            <AllowSpawning>true</AllowSpawning>   <!-- CHANGED TO TRUE --> 
      </ServerInitialConditions>
    <ServerHandlers>
       <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" forceReset="true"/>
        <DrawingDecorator>
            <!-- coordinates for cuboid are inclusive -->
            <!--floor-->
            <DrawCuboid x1="0" y1="40" z1="0" x2="76" y2="50" z2="76" type="grass" /> <!-- limits of our arena -->
            
            <DrawCuboid x1="9" y1="40" z1="0" x2="9" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="19" y1="40" z1="0" x2="19" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="28" y1="40" z1="0" x2="28" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="32" y1="40" z1="0" x2="32" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="38" y1="40" z1="0" x2="38" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="45" y1="40" z1="0" x2="45" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="57" y1="40" z1="0" x2="57" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="66" y1="40" z1="0" x2="66" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="38" x2="76" y2="40" z2="38" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="32" x2="76" y2="40" z2="32" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="9" x2="76" y2="40" z2="9" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="19" x2="76" y2="40" z2="19" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="57" x2="76" y2="40" z2="57" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="66" x2="76" y2="40" z2="66" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="28" x2="76" y2="40" z2="28" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="45" x2="76" y2="40" z2="45" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="0" x2="76" y2="40" z2="0" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="76" x2="76" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="0" x2="0" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="76" y1="40" z1="0" x2="76" y2="40" z2="76" type="glowstone" />
            
            <!--water and lava-->
            <DrawCuboid x1="67" y1="40" z1="1" x2="75" y2="40" z2="8" type="water" /> 
            <DrawCuboid x1="1" y1="40" z1="67" x2="8" y2="40" z2="75" type="lava" /> 
            
            
            <!--air-->
            <DrawCuboid x1="0" y1="41" z1="0" x2="76" y2="50" z2="76" type="air" /> <!-- limits of our arena -->
           
            <!--ceiling-->
            <DrawCuboid x1="0" y1="50" z1="0" x2="76" y2="50" z2="76" type="glowstone" />            <!-- limits of our arena -->   
              <!--house-->
            <DrawBlock type="planks" x="71" y="41" z="70"/>
            <DrawBlock type="planks" x="71" y="41" z="72"/>
            <DrawBlock type="planks" x="70" y="41" z="70"/>
            <DrawBlock type="planks" x="70" y="41" z="72"/>
            <DrawBlock type="planks" x="72" y="41" z="70"/>
            <DrawBlock type="planks" x="72" y="41" z="71"/>
            <DrawBlock type="planks" x="72" y="41" z="72"/>
          
            <DrawBlock type="planks" x="71" y="42" z="70"/>
            <DrawBlock type="planks" x="71" y="42" z="72"/>
            <DrawBlock type="planks" x="70" y="42" z="70"/>
            <DrawBlock type="planks" x="70" y="42" z="72"/>
            <DrawBlock type="planks" x="72" y="42" z="70"/>
            <DrawBlock type="planks" x="72" y="42" z="71"/>
            <DrawBlock type="planks" x="72" y="42" z="72"/>        
          
            <DrawBlock type="planks" x="71" y="43" z="70"/>
            <DrawBlock type="planks" x="71" y="43" z="71"/>
            <DrawBlock type="planks" x="71" y="43" z="72"/>
            <DrawBlock type="planks" x="70" y="43" z="70"/>
            <DrawBlock type="planks" x="70" y="43" z="71"/>
            <DrawBlock type="planks" x="70" y="43" z="72"/>
            <DrawBlock type="planks" x="72" y="43" z="70"/>
            <DrawBlock type="planks" x="72" y="43" z="71"/>
            <DrawBlock type="planks" x="72" y="43" z="72"/>
          
            <DrawBlock type="planks" x="71" y="44" z="71"/>
            
            <!-- place mobs -->
            <DrawEntity x="20"  y="41" z="20" type="Pig" />
            <DrawEntity x="10"  y="41" z="25" type="Cow" />
            <DrawEntity x="25"  y="41" z="10" type="Sheep" />
            <DrawEntity x="20"  y="41" z="60" type="Villager" />
            <DrawEntity x="2"  y="41" z="55" type="EntityHorse" />
            <DrawEntity x="55"  y="41" z="10" type="Wolf" />
            <DrawEntity x="55"  y="41" z="55" type="Chicken" />
            




            
            <!--spawners-->
            <!--DrawCuboid x1="29" y1="40" z1="29" x2="29" y2="40" z2="29" type="mob_spawner" variant="Pig"/-->
            <!--DrawCuboid x1="31" y1="40" z1="31" x2="31" y2="40" z2="31" type="mob_spawner" variant="Chicken"/-->
            <!--DrawCuboid x1="29" y1="40" z1="31" x2="29" y2="40" z2="31" type="mob_spawner" variant="Cow"/-->
            <!--DrawCuboid x1="31" y1="40" z1="29" x2="31" y2="40" z2="29" type="mob_spawner" variant="Sheep"/-->

        </DrawingDecorator>
      <ServerQuitFromTimeUp timeLimitMs="300000"/>
      <ServerQuitWhenAnyAgentFinishes/>
    </ServerHandlers>
  </ServerSection>
  <AgentSection mode="Survival">
    <Name>Chatty</Name>
    <AgentStart>
      <Placement x="4" y="43" z="4" pitch="30" yaw="270"/>
      <Inventory>
        <InventoryItem slot="0" type="diamond_pickaxe"/>
        <InventoryItem slot="1" type="diamond_sword"/>
        <InventoryItem slot="2" type="fishing_rod"/>
        
      </Inventory>
    </AgentStart>
    <AgentHandlers>
      <DiscreteMovementCommands/>
      <ContinuousMovementCommands turnSpeedDegs="180"/>
      <AbsoluteMovementCommands/>
      <!--ObservationFromFullStats/-->
      <ObservationFromRay/>
      <ObservationFromNearbyEntities>
        <Range name="Entities" xrange="75" yrange="10" zrange="75"/>
      </ObservationFromNearbyEntities>
      <ObservationFromGrid>
          <Grid name="floor">
              <min x="0" y ="-1" z="0"/>
              <max x="0" y="-1" z="76"/>
          </Grid>
      </ObservationFromGrid>
      <InventoryCommands/>
      <!--RewardForSendingCommand reward="-1"/-->
    </AgentHandlers>
  </AgentSection>
</Mission>
'''
# <RewardForSendingMatchingChatMessage>
#   <ChatMatch reward="100.0" regex="'''+items[obj_id]+'''" description="Anything that matches the object."/>
# </RewardForSendingMatchingChatMessage>

# Create default Malmo objects:



agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

my_mission = MalmoPython.MissionSpec(mission_xml, True)
my_mission_record = MalmoPython.MissionRecordSpec("chat_reward.tgz")

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print "Error starting mission:",e
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print "Waiting for the mission to start ",
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission running ",
switcherCommand = classBasedMovement.switcherCommand(agent_host)
displayGUI = displayGUI.commandWindow( agent_host, switcherCommand)
displayGUI.my_mission = my_mission;
displayGUI.my_mission_record = my_mission_record;
displayGUI.window.mainloop()

def get_chatty(observation):
    if 'Entities' in observation:
        entities = observation["Entities"]
        for ent in entities:
            if ent["name"] == "Chatty":
                chatty = ent
    return chatty

def find_closest_animal(observation, chatty, animal):
    closest_animal = None
    distanceToChattyFromAnimal = -999

    if 'Entities' in observation:
        entities = observation['Entities']
        animalList = []
        # get the pig and chatty entities
        # chatty is the user
        for ent in entities:
            if ent["name"] == animal:
                animalList.append(ent)
        # if chatty is not None, get the x and z coordinates
        if chatty != None:
            chatty_x = chatty["x"]
            chatty_z = chatty["z"]
            distanceList = []

            for a in animalList:
                animal_x = a["x"]
                animal_z = a["z"]

                # distance formula to get distance from any pig to chatty
                distanceToChattyFromAnimal = math.sqrt(abs((abs(chatty_x - animal_x) ** 2) + (abs(chatty_z - animal_z) ** 2)))
                distanceList.append(distanceToChattyFromAnimal)
                if distanceToChattyFromAnimal == min(distanceList):
                    closest_animal = a
    
    return closest_animal

def found_pig(los_type, los_x, closest_pig_x):
    return ((los_type == "Pig") and (los_x == closest_pig_x))

def piggy_in_range(obs, animal):
    return obs['inRange'] and obs['type'] == animal

def turn_pitch_discrete_move(command, number):
    agent_host.sendCommand(command + " " + number)
    time.sleep(1)
    agent_host.sendCommand(command + " 0")

def load_grid():
    latest_ws = agent_host.peekWorldState()

    if latest_ws.number_of_observations_since_last_state > 0:
        observation = json.loads(latest_ws.observations[-1].text)
        grid = observation.get(u'floor', 0) 
    return grid

def findAnimal(animal):
    counter = 0
    agent_host.sendCommand('setPitch 30')

    while True:
        counter += 1
        latest_ws = agent_host.peekWorldState()

        if latest_ws.number_of_observations_since_last_state > 0:
            observation = json.loads(latest_ws.observations[-1].text)

            if 'LineOfSight' in observation:
                if piggy_in_range(observation['LineOfSight'], animal):
                    return True

        if counter % 10 == 0:
            return False
        
        chatty = get_chatty(observation)
        closest_animal = find_closest_animal(observation, chatty, animal)

        if closest_animal == None:
            return True
    
        x = int(chatty["x"])
        z = int(chatty["z"])
        a = int(closest_animal["x"])
        b = int(closest_animal["z"])

        agent_host.sendCommand("setYaw 270")

        if (x <= a):
            agent_host.sendCommand("setYaw 270")
            for i in range(x, a):
                agent_host.sendCommand("tp {} 41 {}".format(i, z))
                time.sleep(0.15)

        else:
            agent_host.sendCommand("setYaw 90")
            for i in range(x, a, -1):
                agent_host.sendCommand("tp {} 41 {}".format(i, z))
                time.sleep(0.15)

        if (z <= b):
            agent_host.sendCommand("setYaw 0")
            for i in range(z, b):
                agent_host.sendCommand("tp {} 41 {}".format(a, i))
                time.sleep(0.15)
        else:
            agent_host.sendCommand("setYaw 180")
            for i in range(z, b,-1):
                agent_host.sendCommand("tp {} 41 {}".format(a, i))
                time.sleep(0.15)

def attack():
    agent_host.sendCommand("attack 1")
    time.sleep(0.5)
    agent_host.sendCommand("attack 0")
            
def kill(animal):
    agent_host.sendCommand('hotbar.2 1')
    agent_host.sendCommand('hotbar.2 0')
    originalEnts = defaultdict(int)

    latest_ws = agent_host.peekWorldState()

    if latest_ws.number_of_observations_since_last_state > 0:
        observation = json.loads(latest_ws.observations[-1].text)
        
        for ent in observation['Entities']:
            if ent['name'] in ["Pig", "Sheep", "Villager", "Horse", "Cow", "Wolf", "Chicken"]:
                originalEnts[ent['name']] += 1
    counter = 0           
    while True:
        if not findAnimal(animal):
            counter += 1
        if counter >= 10:
            break
        attack()
        ents = defaultdict(int)
        latest_ws = agent_host.peekWorldState()

        if latest_ws.number_of_observations_since_last_state > 0:
            observation = json.loads(latest_ws.observations[-1].text)
            for ent in observation['Entities']:
                if ent['name'] in ["Pig", "Sheep", "Villager", "Horse", "Cow", "Wolf", "Chicken"]:
                    ents[ent['name']] += 1

        if ents != originalEnts:
            break

def fish():
    flag = False
    agent_host.sendCommand('hotbar.3 1')
    agent_host.sendCommand('hotbar.3 0')

    agent_host.sendCommand('setPitch 25')

    start = time.time()
    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(3)
    latest_ws = agent_host.peekWorldState()
        
    if latest_ws.number_of_observations_since_last_state > 0:
        observation = json.loads(latest_ws.observations[-1].text)

    while True:
        current = time.time()
        latest_ws = agent_host.peekWorldState()

        if current-start >= 45:
            agent_host.sendCommand('use 1')
            agent_host.sendCommand('use 0')
            break
        
        if latest_ws.number_of_observations_since_last_state > 0:
            last = observation
            observation = json.loads(latest_ws.observations[-1].text)
            
        if abs(filter(lambda ent: ent[u'name'] == u'unknown', observation['Entities'])[0][u'y'] - filter(lambda ent: ent[u'name'] == u'unknown', last['Entities'])[0][u'y']) > 0.02:
##            print("-----------")
##            print(last['Entities'])
##            print("***********")
##            print(observation['Entities'])
            agent_host.sendCommand('use 1')
            agent_host.sendCommand('use 0')
            break
            
       
    # Loop until mission ends:
while world_state.is_mission_running:

    time.sleep(0.5)
    sys.stdout.write(".")

    while True:
        command = raw_input()
        tokens = command.split()
        if tokens[0] == "find":
            if tokens[1].lower().title() in ["Pig", "Sheep", "Villager", "Horse", "Cow", "Wolf", "Chicken"]:
                animal = tokens[1].lower().title()
                findAnimal(animal)
            elif tokens[1].lower() == "water":
                latest_ws = agent_host.peekWorldState()
                if latest_ws.number_of_observations_since_last_state > 0:
                    observation = json.loads(latest_ws.observations[-1].text)
                chatty = get_chatty(observation)

                x = int(chatty["x"])
                z = int(chatty["z"])
                a = 66
                b = 4
                
                agent_host.sendCommand("setYaw 270")
                        
                if (x <= a):
                    agent_host.sendCommand("setYaw 270")
                    for i in range(x, a):
                        agent_host.sendCommand("tp {} 41 {}".format(i, z))
                        time.sleep(0.15)

                else:
                    agent_host.sendCommand("setYaw 90")
                    for i in range(x, a, -1):
                        agent_host.sendCommand("tp {} 41 {}".format(i, z))
                        time.sleep(0.15)

                if (z <= b):
                    agent_host.sendCommand("setYaw 0")
                    for i in range(z, b):
                        agent_host.sendCommand("tp {} 41 {}".format(a, i))
                        time.sleep(0.15)
                else:
                    agent_host.sendCommand("setYaw 180")
                    for i in range(z, b,-1):
                        agent_host.sendCommand("tp {} 41 {}".format(a, i))
                        time.sleep(0.15)

                agent_host.sendCommand("setYaw 270")

            
        elif tokens[0] == "kill":
            animal = tokens[1].title()

            kill(animal)
        elif tokens[0] == "fish":
            fish()
  

    for error in world_state.errors:
        print "Error:",error.text


print
print "Mission ended"
# Mission has ended.
