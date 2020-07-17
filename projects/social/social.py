import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
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
    
    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

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
        for i in range(num_users):
            self.add_user(i)

        # Create friendships
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendships.append((user, friend))
        
        self.fisher_yates_shuffle(friendships)
        total_friendships = num_users * avg_friendships
        random_friendships = friendships[:total_friendships//2]
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])


        # for user in self.users:
        #     sample_size = random.randint(1, (avg_friendships * 2))

        #     possible_friends = self.users.copy()
        #     del possible_friends[user]

        #     friends = random.sample(set(possible_friends.keys()), sample_size)
        #     for friend in friends:
        #         self.add_friendship(user, friend)
        #     print('User: ', user, self.friendships[user])

    def linear_populate_graph(self, user_id):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set. Add path to visited user
        #BFT with path so that we can get shortest path to each user
        q = Queue()
        q.enqueue([user_id])
        while q.size():
            path = q.dequeue()
            user = path[-1]

            if user not in visited:
                visited[user] = path
                for  friend in self.friendships[user]:
                    newPath = path.copy()
                    newPath.append(friend)
                    q.enqueue(newPath)

        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
