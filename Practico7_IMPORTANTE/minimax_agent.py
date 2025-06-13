from tic_tac_toe import TicTacToe
from agent import Agent
import random

class AgentMinimax(Agent):
    def __init__(self, player=1):
        super().__init__(player)

    def next_action(self, board: TicTacToe) -> tuple[int, int]:
        self.idx = 0
        pos, _ = self.minimax(board, self.player)
        return pos

    def heuristic_utility(self, board: TicTacToe) -> int:
        # Completar con función de evaluación
        # La función de evaluación estima el valor de un estado del juego que no es terminal (es decir, cuando no se ha llegado aún al final de 
        # la partida) y sirve para decidir cuál movimiento es mejor cuando el árbol no puede explorarse completamente.
        # Sirve para limitar la altura a evaluar del arbol, cuando la busqueda crece de forma exponencial.
        return 0

    def minimax(self, board: TicTacToe, player: int) -> tuple[tuple[int, int], int]:

        # Caso base
        gameEnded, finalValue = board.is_end() # finalValue = U(s)
        if (gameEnded):
            return None, finalValue

        # Casos no base
        actions = board.get_available_cells()
        random.shuffle(actions)
        action_nodes = []
        for action in actions:
            child_node = board.clone()
            child_node.play(action, player)
            action_nodes.append((action, child_node))

        value = 0
        chosen_action = None

        if player != self.player:  # mini
            # Buscar acción que minimiza el valor
            value = float('inf')
            for child_node in action_nodes:
                node_action = child_node[0]
                node_board = child_node[1]
                _, uAux = self.minimax(node_board, self.next_player(player))
                if uAux < value:
                    chosen_action, value = node_action, uAux

        else:  # max (player == self.player)
            # Buscar acción que maximiza el valor
            value = float('-inf')
            for child_node in action_nodes:
                node_action = child_node[0]
                node_board = child_node[1]
                _, uAux = self.minimax(node_board, self.next_player(player))
                if uAux > value:
                    chosen_action, value = node_action, uAux

        return chosen_action, value
    
    def next_player(self, player: int):
        return (player % 2) + 1