import os

class AIService:
    def __init__(self):
        self.provider = "demo"

    def chat(self, employee, message):
        """
        Temporary AI response.
        Later we'll replace this with GPT/Gemini.
        """

        return {
            "reply": f"{employee['name']} ({employee['role']}) says: I received your message: '{message}'."
        }


ai = AIService()
