from search_agent import SearchAgent
from priority_queue import PriorityQueue


class UCSAgent(SearchAgent):

    def __init__(self, env, initial_state, end_state, model):
        super().__init__(env, initial_state, end_state, model)
        self.action_list = []

    def _next_action(self):
       #Usar action_list o llamar a ucs para actualizar self.action_list
       raise NotImplementedError

    def ucs(self):
        #Algoritmo de ucs que retorna la lista de acciones para llegar al destino
        raise NotImplementedError
