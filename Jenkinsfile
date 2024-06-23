pipeline {
    agent any

    tools {
        // Installer le scanner SonarQube configuré
        sonarQubeScanner 'SonarQubeScanner'
    }

    environment {
        // Définir les variables d'environnement
        SONARQUBE_SERVER = 'SonarQube'
    }

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
                // Analyser le code avec SonarQube
                withSonarQubeEnv('SonarQube') {
                    bat 'sonar-scanner.bat'
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 1, unit: 'HOURS') {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
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
