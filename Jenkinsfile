pipeline {
    agent any

    environment {
        APP_DIR   = "/home/ubuntu/flask-app"
        VENV_DIR = "venv"
        FLASK_PORT = "5000"
        FLASK_EC2 = "ubuntu@13.201.55.230"
        // FLASK_EC2 = "ubuntu@NEW IP"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mohamedfazil2315/Jenkins-CI-CD-Pipeline.git'
            }
        }

        stage('Install Dependencies (Jenkins Test)') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Basic Test') {
            steps {
                sh '''
                . venv/bin/activate
                python -c "import flask; print('Flask OK')"
                '''
            }
        }

        stage('Deploy to Flask EC2') {
            steps {
                sh '''
                # Ensure app directory exists
                ssh ${FLASK_EC2} "mkdir -p ${APP_DIR}"

                # Copy only required files (NO venv)
                #scp app.py requirements.txt dev_flask.sh -r ${FLASK_EC2}:${APP_DIR}
                scp -r app.py requirements.txt dev_flask.sh ubuntu@13.201.55.230:/home/ubuntu/flask-app

                
                # Install deps and restart Flask cleanly
                ssh ${FLASK_EC2} "
                  cd ${APP_DIR} &&
                  rm -rf venv &&
                  python3 -m venv venv &&
                  . venv/bin/activate &&
                  pip install --upgrade pip &&
                  pip install -r requirements.txt &&
                  chmod +x dev_flask.sh &&
                  ./dev_flask.sh restart
                "
                '''
            }
        }
    }
}
