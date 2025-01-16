from flask import Flask, render_template, request
from math import exp, factorial

app = Flask(__name__)

# Fungsi untuk menghitung distribusi Poisson
def poisson_probability(mean, k):
    return (exp(-mean) * (mean ** k)) / factorial(k)

@app.route("/", methods=["GET", "POST"])
def index():
    lambda_value = None
    k_range = None
    probabilities = []
    percentages = []

    if request.method == "POST":
        try:
            # Ambil input dari pengguna
            lambda_value = float(request.form.get("lambda_value"))
            k_range = int(request.form.get("k_range"))

            # Hitung peluang untuk setiap nilai k (dari 0 sampai k_range)
            for k in range(0, k_range + 1):
                prob = poisson_probability(lambda_value, k)
                probabilities.append(round(prob, 4))
                percentages.append(round(prob * 100, 2))
        except (ValueError, TypeError):
            probabilities = None

    return render_template(
        "index.html",
        lambda_value=lambda_value,
        k_range=k_range,
        probabilities=probabilities,
        percentages=percentages,
    )

if __name__ == "__main__":
    app.run(debug=True, port=7001)
