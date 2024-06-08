# Data
NL = [1, 2, 2, 2, 5]
NT = [91, 65, 45, 36, 66]

# Menghitung rata-rata
mean_NL = sum(NL) / len(NL)
mean_NT = sum(NT) / len(NT)

# Menghitung koefisien regresi
numerator = sum((NL[i] - mean_NL) * (NT[i] - mean_NT) for i in range(len(NL)))
denominator = sum((NL[i] - mean_NL)**2 for i in range(len(NL)))
slope = numerator / denominator
intercept = mean_NT - slope * mean_NL

# Mencetak persamaan regresi
print(f"Persamaan regresi: NT = {slope:.2f} * NL + {intercept:.2f}")

# Menghitung prediksi nilai NT
predicted_NT = [slope * nl + intercept for nl in NL]

# Fungsi untuk menghitung galat RMS
def rms_error(actual, predicted):
    return ((sum((actual[i] - predicted[i])**2 for i in range(len(actual))) / len(actual)) ** 0.5)

# Menghitung galat RMS
error = rms_error(NT, predicted_NT)

# Output hasil prediksi dan galat RMS
for i in range(len(NL)):
    print(f"NL = {NL[i]}, NT aktual = {NT[i]}, NT prediksi = {predicted_NT[i]:.2f}")

print(f"Galat RMS = {error:.4f}")
