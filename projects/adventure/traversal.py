class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def inverse(self, direction_to_flip):
        cardinal_inverse = {
            'n': 's',
            'e': 'w',
            's': 'n',
            'w': 'e'
        }

        return cardinal_inverse[direction_to_flip]

    def dfs(self, starting_vertex, player):
        """
        Return a list containing a path from beginning to end in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()
        directions = []

        while s.size() > 0:
            print(player.current_room.id, directions, self.vertices)
            # path is route through all rooms
            path = s.pop()
            # room is a vertex
            v = path[-1]

            if v not in visited:
                # create a vertices slot for room
                self.vertices[v] = dict()
                # find all exits for room
                room_exits = player.current_room.get_exits()

                # for loop through list and store with unexplored question mark
                for room_directions in room_exits:
                    self.vertices[v][room_directions] = '?'

                # add direction from previous room after first room
                if len(self.vertices) > 1:
                    self.vertices[v][self.inverse(directions[-1])] = path[-2]

                # finished processing add room to visited set
                visited.add(v)

            # end case for 500 main maze
            if len(self.vertices) == 500:
                # entered last room
                return print(f"traversed: {directions}\nvertices: {self.vertices}")

            # insert next room to go to with direction
            for direction, value in self.vertices[v].items():
                if value == '?':
                    # then travel there to direction but add all to stack
                    directions.append(direction)
                    break

            # move player forward
            player.travel(directions[-1])

            # update new num room and last room record
            for direction, value in self.vertices[v].items():
                # find direction traveled and edit only if value is '?'
                if direction == directions[-1] and value == '?':
                    # then edit record with room ventured to
                    self.vertices[v][direction] = player.current_room.id
                    break

            # add new current room to stack with copy of current path
            path_copy = list(path)
            path_copy.append(player.current_room.id)
            s.push(path_copy)

        return directions
