from tic_tac_toe import TicTacToe
from agent import Agent


class AgentExpectimax(Agent):
    def __init__(self, player=1, max_depth: int = 10):
        super().__init__(player)
        self.max_depth = max_depth

    def next_action(self, board: TicTacToe) -> tuple[int, int]:
        self.idx = 0
        pos, _ = self.expectimax(board, self.player, self.max_depth)
        return pos

    def heuristic_utility(self, board: TicTacToe) -> int:
        # Completar con función de evaluación
        return 0

    def expectimax(
        self, board: TicTacToe, player: int, depth: int
    ) -> tuple[tuple[int, int], int]:


        # TODO: Completar
        # Caso base
        gameEnded, finalValue = board.is_end() # finalValue = U(s)
        if (gameEnded):
            return None, finalValue
        
        # Casos no base
        actions = board.get_available_cells()
        action_nodes = []
        for action in actions:
            child_node = board.clone()
            child_node.play(action, player)
            action_nodes.append((action, child_node))

        value = 0
        chosen_action = None
        if player != self.player:  # Expecti
            # Calcular valor promedio de las acciones del oponente
            total_value = 0
            for child_node in action_nodes:
                node_action = child_node[0]
                node_board = child_node[1]
                _, uAux = self.expectimax(node_board, self.next_player(player), depth - 1)
                total_value += uAux
            #  la función pol_prob(s, a) representa la probabilidad de que en el estado s se elija la acción a

            value = total_value / len(action_nodes)
            # print("Current Value", value)
        else:  # max
            # Buscar acción que maximiza el valor
            value = float('-inf')
            for child_node in action_nodes:
                node_action = child_node[0]
                node_board = child_node[1]
                _, uAux = self.expectimax(node_board, self.next_player(player), depth - 1)
                if uAux > value:
                    chosen_action, value = node_action, uAux

        # pol_prob(s, a) representa la probabilidad de que en el estado s se elija la acción a
        # juego.suc(s, a) devuelve el nuevo estado que resulta de aplicar la acción a sobre el estado s.

        return chosen_action, value

    def next_player(self, player: int):
        return (player % 2) + 1