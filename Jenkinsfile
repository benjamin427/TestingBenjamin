pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extentions: [], userRemoteConfigs: [[url: 'https://github.com/ShadowDancer7/FrameworkAnalysis.git']]])     
            }
        }

        stage('Build'){
            steps {
               git branch: 'master', url: 'https://github.com/ShadowDancer7/FrameworkAnalysis.git'
               bat 'python3 test_loginPage.py'
               bat 'python3 test_registrationPage.py'
               bat 'python3 test_resetPasswordPage.py' 
            }
        }

        stage('Test'){
            steps {
                bat 'python3 -m pytest'
            }
        }
    }
}