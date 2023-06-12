# To Do app

This is my implementation of the backend for the To Do app.

I have used FastAPI with python.

# Requirements

- Python 3.10
- Docker Desktop 4.20
- Install FastAPI and uvicorn modules

# How to run

The docker-compose builds an image for the python backend using the Dockerfile and then creates a PostgreSQL database on the same network.

```
docker-compose up
```
NOTE: the first time, as the DB takes more time, you would need to do that command twice :(

If you want to just start the backend without the docker-compose just run:

```
$Env:DB_HOST="localhost"
$Env:DB_DATABASE="db"
$Env:DB_USER="username"
$Env:DB_PASSWORD="example"

python -m uvicorn main:app
```

You will need a database properly setup.

# Things to improve

1. Pagination for the GET items/items endpoint, something like getting 100 items per page. Getting the data with this kind of format:
```
{
    "data": [...],
    "page": 0,
    "total": 1305,
    "count": 100
}
```
2. Integration testing, I think on two ways. The first one is to use mocks (unittest.mock?) so that the ItemRepository class instantiates a mock version and each of their methods return the values we want for each test. The second one is with docker compose and create a database at the start of the battery of tests, with each test clean up and reset the database state and at the end do a teardown of the docker container.
3. The POST and PUT can return the entity modified instead of an empty body. This is not a standard on Rest APIs but I find it useful for the frontend developers.