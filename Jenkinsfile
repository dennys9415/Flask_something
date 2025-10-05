pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker compose build'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker compose up -d'
                }
            }
        }

        stage('Test App') {
            steps {
                script {
                    // Example health check or test
                    sh 'curl -f http://localhost:80 || (echo "App test failed" && exit 1)'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker compose down'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build and test successful!'
        }
    }
}
