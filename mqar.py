import random
import json

def generate_mqar_kv_pairs(num_pairs=500, k_range=(100, 1000), v_range=(1000, 9999)):
    kv_pairs = []
    used_keys = set()
    
    while len(kv_pairs) < num_pairs:
        k = random.randint(*k_range)
        if k in used_keys:
            continue 
        
        v = random.randint(*v_range)
        kv_pairs.append((k, v))
        used_keys.add(k)
    
    random.shuffle(kv_pairs)
    return kv_pairs

num_problems = 100
problems = []

for i in range(num_problems):
    num_pairs = 500
    kv_pairs = generate_unique_kv_pairs(num_pairs=num_pairs)
    
    target_keys = random.sample(kv_pairs, 3)
    target_ks = ', '.join(str(k) for k, v in target_keys)
    target_vs = ', '.join(str(v) for k, v in target_keys)
    
    formatted_kv_pairs = "; ".join([f"k: {k}, v: {v}" for k, v in kv_pairs])
    
    problems.append({
        "problem_id": i + 1,
        "num_pairs": num_pairs,
        "target_k": target_ks,
        "kv_pairs": formatted_kv_pairs,
        "ground_truth": target_vs,
        "question": f"If k is one of {target_ks}, what are possible v? Please directly give me all values without other output"
    })

# Write to JSON file
with open("mqar_problems.json", "w") as f:
    json.dump(problems, f, indent=4)

print("Generated 100 mqar problems and saved to mqar_problems.json.")