
from flask import Flask, render_template, request
from hybrid import hybrid_recommend

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = None
    error = None

    if request.method == "POST":
        interests = request.form.get("interests", "").strip()
        career_goal = request.form.get("career_goal", "").strip()
        student_id = request.form.get("student_id", "").strip()

        if not interests or not career_goal or not student_id:
            error = "Please fill in all fields."
        else:
            try:
                recommendations = hybrid_recommend(
                    interests,
                    career_goal,
                    student_id,
                    top_n=5
                )
            except ValueError as exc:
                error = str(exc)

    return render_template(
        "index.html",
        recommendations=recommendations,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
