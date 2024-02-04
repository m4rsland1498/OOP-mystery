class NPC:
    def __init__(self, npc_name):
        self.name = npc_name
        self.description = None
        self.conversation = None

    def get_name(self):
        return self.name

    def set_conversation(self, convo):
        self.conversation = convo
        # use dictionaries
