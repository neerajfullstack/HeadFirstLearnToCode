import random

verbs = [
    'Leverage',
    'Sync',
    'Target',
    'Gamify',
    'Offline',
    'Crowd-Sourced',
    '24/7',
    'Lean-In',
    '30,000 Foot'
    ]

adjectives = [
    'A/B Tested',
    'Freemium',
    'Hyperlocal',
    'Siloed',
    'B-to-B',
    'Oriented',
    'Cloud-Based',
    'API-Based'
    ]

nouns = [
    'Early Adopter',
    'Low-Hanging Fruit',
    'Pipeline',
    'Splash Page',
    'Production',
    'Process',
    'Tipping Point',
    'Paradigm'
    ]

# Choose one verb, adjective and noun randomly from lists

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# Now build the phrase by "Adding words" together

phrase = verb + ' ' + adjective + ' ' + noun

#output the phrase
print(phrase)
