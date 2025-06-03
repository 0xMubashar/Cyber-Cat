
# FeatureMutator.py

import json
import random

class FeatureMutator:
    def __init__(self):
        self.feature_space = ['entropy', 'api_calls', 'strings', 'packer_flag', 'section_count']

    def mutate(self, features):
        mutated = features.copy()
        for f in self.feature_space:
            if f in mutated:
                mutated[f] = self._apply_mutation(mutated[f])
        return mutated

    def _apply_mutation(self, value):
        if isinstance(value, (int, float)):
            return value + random.uniform(-0.5, 0.5)
        elif isinstance(value, str):
            return ''.join(random.sample(value, len(value)))
        return value

if __name__ == "__main__":
    with open("sample_input.json") as f:
        features = json.load(f)
    mutator = FeatureMutator()
    mutated = mutator.mutate(features)
    with open("mutated_output.json", "w") as f:
        json.dump(mutated, f, indent=2)
