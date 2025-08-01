pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3-tk
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '. ${VENV}/bin/activate && pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t inventory-app:latest .'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo '❌ Build or tests failed.'
        }
    }
}
