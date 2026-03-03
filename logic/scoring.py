import numpy as np

def calculate_user_vector(answers, questions):
    total = [0,0,0,0,0]
    for i, choice in enumerate(answers):
        vec = questions[i]["options"][choice]["vector"]
        total = [t+v for t,v in zip(total, vec)]
    return np.array(total) * 5

def cosine_similarity(a, b):
    return np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b))

def match_stars(user_vector, star_vectors, selected_position):
    results = []
    for name, data in star_vectors.items():
        if data["position"] == selected_position:
            sim = cosine_similarity(user_vector, np.array(data["vector"]))
            results.append((name, sim))
    results.sort(key=lambda x: x[1], reverse=True)
    return results