pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/groupepfadevops/soufiane.git'
            }
        }
        stage('Setup') {
            steps {
                bat 'python -m ensurepip --upgrade || echo Pip already installed'
            }
        }
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt --user'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m unittest discover -s src'
            }
        }
        stage('Deploy') {
            steps {
                bat 'deploy.bat'
            }
        }
    }
}
