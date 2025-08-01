pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python Env') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }

        stage('Build App') {
            steps {
                // Replace this with your actual build logic
                sh '. venv/bin/activate && python setup.py build'
            }
        }
    }

    post {
        success {
            echo '✅ Build and tests completed successfully.'
        }
        failure {
            echo '❌ Build or tests failed.'
        }
        always {
            cleanWs()
        }
    }
}
