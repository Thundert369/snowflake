pipeline {
    agent any
    
    parameters {
        string(name: 'WAREHOUSE_NAME', defaultValue: '', description: 'Enter the warehouse name')
        string(name: 'WAREHOUSE_SIZE', defaultValue: 'X-Small', description: 'Enter the warehouse size')
    }

    environment {
        GITHUB_REPO = 'https://github.com/Thundert369/snowflake.git'
        GITHUB_SCRIPT_PATH = 'test2.py'
        ACCOUNT = 'gj35654.central-india.azure'
        CREDENTIAL_ID_USER = 'user-id'
        CREDENTIAL_ID_PASSWORD = 'password-id'
        ROLE = 'ACCOUNTADMIN'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: GITHUB_REPO
            }
        }

        stage('Run Python Script') {
            steps {
                withCredentials([string(credentialsId: CREDENTIAL_ID_USER, variable: 'USER'),
                                 string(credentialsId: CREDENTIAL_ID_PASSWORD, variable: 'PASSWORD')]) {
                    script {
                        // Run the Python script with parameters and username/password authentication
                        sh "python3 --version"
                        sh "pip install snowflake-connector-python"
                        sh "pip install snowflake-snowpark-python"
                        sh "python3 ${GITHUB_SCRIPT_PATH} ${ACCOUNT} ${USER} ${PASSWORD} ${ROLE} ${params.WAREHOUSE_NAME} ${params.WAREHOUSE_SIZE}"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
