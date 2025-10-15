user2_id, user2_level = input().split()
user2_level = int(user2_level)

class User :
    def __init__(self, user_id="codetree", lv=10) :
        self.user_id = user_id
        self.lv = lv
user1 = User()
user2 = User(user2_id, user2_level)

print(f"user {user1.user_id} lv {user1.lv}")
print(f"user {user2.user_id} lv {user2.lv}")

