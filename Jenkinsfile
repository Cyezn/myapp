pipeline {
    agent any // or specify a Docker agent for isolation: agent { docker { image 'python:3.9-slim' } }

    stages {
        stage('Checkout') {
            steps {
                git 'hhttps://github.com/Cyezn/myapp.git' // Replace with your repository URL
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    // Create and activate a virtual environment
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '. venv/bin/activate && pip install -r requirements.txt' // Install project dependencies
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Example: Run a build script if your project requires one
                    sh '. venv/bin/activate && python3 setup.py sdist bdist_wheel' // Or your specific build command
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '. venv/bin/activate && pytest' // Example: Run unit tests with pytest
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/*.whl, dist/*.tar.gz', fingerprint: true // Archive build artifacts
            }
        }
    }

    post {
        always {
            cleanWs() // Clean up the workspace after the build
        }
        failure {
            echo 'Build failed!'
            // Add notifications or further actions on failure
        }
        success {
            echo 'Build successful!'
            // Add notifications or further actions on success
        }
    }
}