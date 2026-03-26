import json

input_path = "./dataset_clean/steam_games_reviews.json"
output_path = "./dataset_clean/steam_reviews_reduced.jsonl"

count_in = 0
count_out = 0
data = []

with open(input_path, "r", encoding="utf-8", errors="ignore") as fin:
    for line in fin:
        count_in += 1

        try:
            review = json.loads(line)
        except json.JSONDecodeError:
            continue

        user_id = review.get("user_id")
        product_id = review.get("product_id")
        text = review.get("text")
        date = review.get("date")   # 👈 AGGIUNTO

        # scarta record incompleti
        if not user_id or not product_id or not text or not date:
            continue

        data.append({
            "user_id": user_id,
            "product_id": product_id,
            "text": text,
            "date": date
        })
        count_out += 1

        if count_in % 1_000_000 == 0:
            print(f"Processate {count_in} righe...")

# 🔑 ORDINAMENTO:
# 1) per user_id
# 2) per data (cronologico) all'interno dello stesso utente
data.sort(key=lambda x: (x["user_id"], x["date"]))

with open(output_path, "w", encoding="utf-8") as fout:
    for r in data:
        fout.write(json.dumps(r, ensure_ascii=False) + "\n")

print("Righe lette:", count_in)
print("Righe scritte:", count_out)
print("File ordinato per user_id e data")