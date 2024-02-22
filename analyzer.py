# analyzer.py

class IDSAnalyzer:
    def __init__(self):
        pass

    def analyze(self, data):
        # Check if the length of the data is above a threshold
        if len(data) > 100:
            return "Suspicious: Data length exceeds threshold"
        else:
            return "Normal: Data length within threshold"

