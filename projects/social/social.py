import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # maps IDs to User objects (lookup table for User Objects give Ids)
        self.users = {}
        # Adjacency List
        # Maps user_ids to list of other users (who are their friends)
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        # generate all possible friendships
        # avoid duplicate friendships
        possible_friendships = []
        for user_id in self.users: #starts at first balue goes all the way
            for friend_id in range(user_id + 1, self.last_id + 1): #starts at next value after the first loop (last id is being used to count ids one before last)
                # user_id == user_id2 cannot happen
                # if friendship between user_id and user_id_2 already exists
                # don't add friendship between user_id_2 and user_id
                possible_friendships.append((user_id, friend_id))

        # randomly selected X friendships
        # the formula for X is num_users * avg_friendships // 2
        # shuffle the array and pick x elements from the front of it
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        #create a queue
        queue = Queue()
        #create a dictionary of visited (previously seen) verticies
        visited = {}  # Note that this is a dictionary, not a set
        #add first user_id to the queue as path
        queue.enqueue([user_id]) #to store the path - it's a path of one to start
        while queue.size() > 0: 
            #dequeue the current path
            current_path = queue.dequeue()
            #get the current vertex from end of path
            current_vertex = current_path[-1] #current vertex is last element in path
            if current_vertex not in visited: # if it is we've already seen it but if not proceed:
                #add vertex to visited dictionary which we'd usually .add to set, but here access visited at current_vertex
                #Also add the path that brought us to this vertex
                #ie add a key and value to the visited dictionary
                #the key is the current vertex, and the value is the path
                visited[current_vertex] = current_path

                #queue up all neighbors as paths
                for neighbor in self.friendships[current_vertex]:
                    #make a new copy of the current path
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    # sg.add_user("Denise")
    # sg.add_user("Candace")
    # sg.add_user("Bryan")
    # sg.add_user("Magi")
    # sg.add_friendship(0, 1)
    # sg.add_friendship(1, 2)
    # sg.add_friendship(0, 3)
    # sg.populate_graph(10, 2)
    sg.populate_graph(5, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
