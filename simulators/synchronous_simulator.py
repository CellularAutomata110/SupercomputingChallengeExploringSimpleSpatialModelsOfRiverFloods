from UpdateRule import updateRule4
from simulators.event import Event
import random as rand
from simulators.transition_rule import TransitionRule
from simulators.heightneighbors import neighbours_of

class SynchronousSimulator:
    '''
    Simulator for synchronous cellular automata. Updates according to
    update_rule, which is a function taking parameters "neighbor_states" and
    "current_state" and returning the next state for that node, based on the
    neighbors' states and the node's own state.
    '''


    def __init__(self, surface = None, heightgrid = None, seed = None,
                 simulation_duration = 100):


        #print(surface)
        self.debugging = False

        self.seed = rand.seed(seed)
        self.simulation_duration = simulation_duration

        self.surface = surface
        self.init_state = surface.get_global_state()

        self.heightgrid = heightgrid


        self.initialize()

    def initialize(self):
        '''
        Start the simulation from the initial condition.
        '''

        self.time = 0
        self.surface.set_global_state(self.init_state)

    def done(self):
        '''
        True iff the simulation has reached final time.
        '''
        return self.time >= self.simulation_duration

    def process_next_reaction(self):
        '''
        Update the surface one clock tick according to the rule given in
        update_rule
        '''
        changed_nodes = []
        #print(self.heightgrid[2][2])
        #print(self.surface)
        for node in self.surface:

            x = node.position[0]
            y = node.position[1]
            node_height = self.heightgrid[x][y]
            neighbor_states = list(map(lambda tup:tup[0].state, node.neighbors))
            neighbor_heights = neighbours_of(self.heightgrid,x,y)
            new_state = updateRule4(neighbor_states, node.state, neighbor_heights, node_height)
            if node.state != new_state:
                changed_nodes.append(node)
                node.new_state = new_state

        # Have to make a second pass, because we can't make any changes until
        # all nodes have been checked.
        for node in changed_nodes:
            node.state = node.new_state

        '''inputs_and_outputs'''

        rule = TransitionRule(inputs=[0] * len(changed_nodes),
                              outputs=[1] * len(changed_nodes))

        new_event = Event(time=self.time,
                          rule = rule,
                          participants=changed_nodes,
                          time_issued=self.time)

        self.time += 10
        return new_event
    #end def process_next_reaction
# end class SynchronousSimulator
