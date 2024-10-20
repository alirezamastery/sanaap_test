# Setup
Make sure port 8000 is available, then run docker compose:
```bash
sudo docker compose up -d --build
```

because this is a test project the `.env` file is added to git

## Tests
```bash
sudo docker exec farahani_project sh -c 'python manage.py test'
```

# API Interaction
Open the swagger ui in browser: 
`http://127.0.0.1:8000/api/schema/swagger-ui/`

Create a user: 
`POST /api/user/users/`

Get an authentication token: 
`POST /api/user/token/`

Authorize with the generated token and create a task: 
`POST /api/task/tasks/`
