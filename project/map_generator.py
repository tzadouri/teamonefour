import random
blocktype = ["gold_block", "emerald_block", "redstone_block"]
color = ["WHITE", "ORANGE", "MAGENTA", "LIGHT_BLUE", "YELLOW", "LIME", "PINK", "CYAN", "PURPLE", "BLUE", "BROWN", "GREEN", "RED"]
def GetMissionXML(SIZE):
  myxml = ""
  # bp = 
  for x in range(-20,21):
        for y in range(1,int(SIZE/3)):
            if random.random() < 0.2:
                myxml += "<DrawBlock x='{}' y='10' z='{}' type='{}'/>".format(x,y,random.choice(blocktype))
            if random.random() < 0.2:
                myxml += "<DrawCuboid x1='{}' y1='10' z1='{}' x2='{}' y2='15' z2='{}'  type='{}' />".format(x,y,x,y,random.choice(blocktype))
  return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Hello world!</Summary>
              </About>
              
            <ServerSection>
              <ServerInitialConditions>
                <Time>
                    <StartTime>7000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
              </ServerInitialConditions>
              <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;15*7;1;"/>
                  <DrawingDecorator>''' + \
                    "<DrawCuboid x1='-21' y1='10' z1='-6' x2='21' y2='14' z2='{}' type='wool' colour='{}'/>".format(SIZE+1,random.choice(color)) + \
                    "<DrawCuboid x1='-20' y1='10' z1='-5' x2='20' y2='40' z2='{}' type='air'/>".format(SIZE) + \
                    "<DrawCuboid x1='-20' y1='9' z1='-5' x2='20' y2='9' z2='{}' type='wool' colour='{}'/>".format(SIZE+1,random.choice(color)) + \
                    myxml + \
                  '''</DrawingDecorator>
                  <AnimationDecorator ticksPerUpdate="40">
                    <Linear>
                      <CanvasBounds>
                        <min x='-35' y='9' z='0'/>
                        <max x='35' y='9' z='100'/>
                      </CanvasBounds>
                      <InitialPos x='-35' y='9' z='15'/>
                      <InitialVelocity x='1' y='0' z='0'/>
                    </Linear>
                    <DrawingDecorator>
                      <DrawCuboid x1='0' y1='0' z1='0'  x2='14' y2='0' z2='10' type='diamond_block'/>
                      <DrawCuboid x1='15' y1='0' z1='0'  x2='20' y2='0' z2='10' type='stone'/>
                      <DrawCuboid x1='21' y1='0' z1='0'  x2='34' y2='0' z2='10' type='diamond_block'/>
                      <DrawCuboid x1='35' y1='0' z1='0'  x2='40' y2='0' z2='10' type='stone'/>
                      <DrawCuboid x1='41' y1='0' z1='0'  x2='55' y2='0' z2='10' type='diamond_block'/>
                    </DrawingDecorator>
                  </AnimationDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="30000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>Diablo!</Name>
                <AgentStart>
                    <Placement x="0.5" y="10" z="0.5" yaw="0"/>
                </AgentStart>
                <AgentHandlers>
                  <DiscreteMovementCommands/>
                  <ObservationFromFullStats/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''
