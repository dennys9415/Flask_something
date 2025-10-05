# 🐍 Flask Meme App

A simple Flask-based web application that serves memes using the [Meme API](https://meme-api.com).  
This project supports local development, Docker containers, CI/CD pipelines with **Jenkins** and **GitHub Actions**.

---

## 🚀 Getting Started

### 🧩 Requirements
Make sure you have installed:
- [Python 3.11+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- (Optional) [Jenkins](https://www.jenkins.io/) if you want to run the CI locally

---

## 🧠 Run Locally (Without Docker)

Clone the repository:
```bash
git clone https://github.com/yourusername/flask-meme-app.git
cd flask-meme-app
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask app:

```bash
python app.py
# or
flask run
```

Open your browser:
👉 http://127.0.0.1:5000

🐳 Run with Docker
Build image
```bash
docker build -t flask-meme-app .
```
Run container

```bash
docker run -dt --name flask-container -h flask -p 5000:80 flask-meme-app
```

Access in your browser:

http://localhost:5000

http://localhost:5000/response

http://localhost:5000/meme

🧰 Run with Docker Compose
```bash
docker compose up --build
```
Then open:
👉 http://localhost

To stop containers:

```bash
docker compose down
```

⚙️ Continuous Integration (CI/CD)
🧱 Jenkins Pipeline
This repository includes a Jenkinsfile that:

* Checks out the repository

* Builds the Docker image

* Runs the container

* Tests the app endpoint

* Cleans up the environment

Command example (inside Jenkins pipeline):

```bash
docker compose build
docker compose up -d
curl -f http://localhost:80
docker compose down
```

🧩 GitHub Actions
Located at:

```bash
.github/workflows/docker-build.yml
```

It runs automatically on each push or pull request to the main branch.

Workflow steps:

* Checkout repository

* Build Docker image

* Run Flask container

* Test endpoint (curl -f http://localhost:80)

* Stop and remove containers

🗂 Project Structure

```
flask-meme-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── .github/
│   └── workflows/
│       └── docker-build.yml
└── README.md
```

🧪 Example Endpoints

Endpoint	    Description
* /	Main        page
* /meme	        Returns a random meme
* /response	    Example JSON response

🧑‍💻 Author
Dennys Cedeño Ramos
📍 New York, USA
💼 Singularity Box
🚀 Networking • Cloud • DevOps • Python • Docker

📄 License
This project is open source and available under the MIT License.

```yaml

---

Would you like me to make it bilingual (English + Spanish in sections) so it looks professional for both audiences?
```