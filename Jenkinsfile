pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
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
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest .
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Build or tests failed.'
            cleanWs()
        }
        success {
            echo '✅ Build and tests passed!'
        }
    }
}
