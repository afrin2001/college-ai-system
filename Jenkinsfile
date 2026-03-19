pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Start Backend') {
            steps {
                bat 'start cmd /k python backend\\app.py'
            }
        }

        stage('Test Chatbot') {
            steps {
                bat '''
                timeout /t 5
                curl -X POST http://127.0.0.1:5000/chat ^
                -H "Content-Type: application/json" ^
                -d "{\"message\":\"What courses are available?\"}"
                '''
            }
        }

        stage('Deploy Frontend') {
            steps {
                bat 'echo Open frontend/index.html in browser'
            }
        }
    }
}
