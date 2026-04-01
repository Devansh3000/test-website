pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the project...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'C:\\Users\\Devansh\\Miniconda3\\Scripts\\pip.exe install selenium'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium test cases...'
                bat 'C:\\Users\\Devansh\\Miniconda3\\python.exe tests/test_form.py'
            }
        }
    }

    post {
        success {
            echo '✅ All tests passed! Build successful.'
        }
        failure {
            echo '❌ Some tests failed. Check the console output for details.'
        }
    }
}
