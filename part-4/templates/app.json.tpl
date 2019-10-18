[
  {
    "essential": true,
    "memory": 256,
    "name": "myapp",
    "cpu": 256,
    "image": "${REPOSITORY_URL}:1",
    "workingDirectory": "/app",
    "command": ["python", "micro-1.py"],
    "portMappings": [
        {
            "containerPort": 3000,
            "hostPort": 3000
        }
    ]
  }
]

