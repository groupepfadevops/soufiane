groovy
pipeline {
    agent any
    
    triggers {
        githubPush()
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/groupepfadevops/soufiane.git'
            }
        }
        
        stage('Setup') {
            steps {
                bat 'python -m ensurepip --upgrade || echo Pip already installed'
                bat 'python -m pip install --upgrade pip'
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
            post {
                always {
                    junit '**/TEST-*.xml'
                }
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
            when {
                branch 'master'
            }
            steps {
                bat 'deploy.bat'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
