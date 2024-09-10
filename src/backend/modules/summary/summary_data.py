from dataclasses import dataclass
from traceback import StackSummary

@dataclass 
class Summary:
    text: str
    
    @property
    def word_count(self):
        return len(self.text.split())
