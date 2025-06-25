# assignment one train RL agent to navigate to cross the road with the action right left right 

import numpy as np
import random

road_length=5 # the road will have 5 positions  0,4 our goal is to reach position 4
actions=['left','right'] # possible actions the agent can take

# Q-table initialisation
Qtable=np.zeros((road_length,len(actions)))

# hyper parameters( help to control  the learning process)
learning_rate=0.8 # as the aplha learning rate # how much the agent updates its values based on new values(the higher the learning rate, the higher the agent can update)
gamma= 0.9 # discount factor for high rewards
epsilon=0.3 # help us discover new paths
episodes=1000  # higher epsiodes lead to higher learning rates 

#training loop
for episode in range(episodes):
    state=0 # initial position
    
    while state != road_length - 1:  # goal is position 4
        
        # epsilon greedy action selection
        if random.uniform(0,1)<epsilon:
            actions=random.randint(0,1) # explore my random action
        else:
            actions=np.argmax(Qtable[state]) # exploits the best known action
            
        #actions
        if actions==0:#left
            next_state=max(0,state-1)   # move left
        elif actions==1:#right
            next_state=min(road_length-1,state+1)   # move right

         #reward setup   
        if next_state==road_length-1:
            reward=20
        else:
            reward=-1
            
        #q table update    
        Qtable[state,actions]+= learning_rate *(reward + gamma * np.max(Qtable[next_state])-Qtable[state,actions])
        
        state=next_state# move to the next state
        
print("Q-table")
print(Qtable)

