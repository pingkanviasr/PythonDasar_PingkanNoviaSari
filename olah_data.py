from baca_data import data
nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"rata-rata: {rata:.1f}")

lulus= [d["nama"] for d in data 
        if d["nilai"] >= 75]
print("lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("tertinggi:", top["nama"])