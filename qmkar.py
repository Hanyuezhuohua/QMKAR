import random
import json

def generate_qmkar_kv_pairs(num_pairs=500, k_range=(100, 300), v_range=(1000, 9999), target_k=None, t=0):
    kv_pairs = []
    
    if target_k is not None and t > 0:
        for _ in range(t):
            v = random.randint(*v_range)
            kv_pairs.append((target_k, v))
    
    while len(kv_pairs) < num_pairs:
        k = random.randint(*k_range)
        v = random.randint(*v_range)

        if k == target_k:
            continue

        kv_pairs.append((k, v))
    
    random.shuffle(kv_pairs)
    return kv_pairs

num_problems = 100
problems = []

for i in range(num_problems):
    num_pairs = 500
    target_k = random.randint(100, 300) 
    t = 3
    kv_pairs = generate_kv_pairs(num_pairs=num_pairs, target_k=target_k, t=t)
    
    target_values = [v for k, v in kv_pairs if k == target_k]
    
    formatted_kv_pairs = "; ".join([f"k: {k}, v: {v}" for k, v in kv_pairs])
    
    problems.append({
        "problem_id": i + 1,
        "num_pairs": num_pairs,
        "target_k": target_k,
        "t": t,
        "kv_pairs": formatted_kv_pairs,
        "ground_truth": target_values,
        "question": f"If k is {target_k}, what are v? Please directly give me all values without other output"
    })

with open("qmkar_problems.json", "w") as f:
    json.dump(problems, f, indent=4)

print("Generated 100 qmkar problems and saved to qmkar_problems.json.")