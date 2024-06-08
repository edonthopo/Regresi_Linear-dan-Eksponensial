# Data
NL = [1, 2, 2, 2, 5]
NT = [91, 65, 45, 36, 66]

# Fungsi untuk menghitung logaritma natural (ln) secara manual
def log(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

# Fungsi untuk menghitung eksponensial secara manual
def exp(x):
    n = 1000.0
    return (1 + x/n) ** n

# Transformasi logaritmik dari NT
log_NT = [log(y) for y in NT]

# Hitung mean dari NL dan log_NT
mean_NL = sum(NL) / len(NL)
mean_log_NT = sum(log_NT) / len(log_NT)

# Hitung slope (b) dan intercept (log(a))
numerator = sum((NL[i] - mean_NL) * (log_NT[i] - mean_log_NT) for i in range(len(NL)))
denominator = sum((NL[i] - mean_NL)**2 for i in range(len(NL)))
b = numerator / denominator
log_a = mean_log_NT - b * mean_NL
a = exp(log_a)

# Membentuk persamaan regresi eksponensial
print(f"Persamaan regresi: NT = {a:.4f} * e^({b:.4f} * NL)")

# Prediksi nilai NT berdasarkan model regresi eksponensial
predicted_NT = [a * exp(b * x) for x in NL]

# Fungsi untuk menghitung galat RMS secara manual
def rms_error(actual, predicted):
    return ((sum((actual[i] - predicted[i])**2 for i in range(len(actual))) / len(actual)) ** 0.5)

# Hitung galat RMS
error = rms_error(NT, predicted_NT)

# Output hasil prediksi dan galat
for i in range(len(NL)):
    print(f"NL = {NL[i]}, NT aktual = {NT[i]}, NT prediksi = {predicted_NT[i]:.2f}")
    
print(f"Galat RMS = {error:.4f}")
