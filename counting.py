import random
import json

def generate_values(num_values=500, v_range=(0, 50)):
    values = [random.randint(*v_range) for _ in range(num_values)]
    random.shuffle(values)  # Shuffle to ensure randomness
    return values

# Generate 100 problems
num_problems = 100
problems = []

for i in range(num_problems):
    num_values = 500
    values = generate_values(num_values=num_values)
    
    # Randomly select three target values
    target_v = random.choice(values)
    count_target_v = values.count(target_v)
    
    formatted_values = ", ".join([f"{v}" for v in values])
    
    problems.append({
        "problem_id": i + 1,
        "num_values": num_values,
        "values": formatted_values,
        "ground_truth": str(count_target_v),
        "question": f"What is the count of values equal to {target_v}? Please answer this question without using any external tool"
    })

# Write to JSON file
with open("counting_problems.json", "w") as f:
    json.dump(problems, f, indent=4)

print("Generated 100 problems with values only and saved to counting_problems.json.")
