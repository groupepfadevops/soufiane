pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/groupepfadevops/contr-le-de-moteur.git'
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
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    bat 'sonar-scanner'
                }
            }
        }
        stage('Deploy') {
            steps {
                bat 'deploy.bat'
            }
        }
    }
}
