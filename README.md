# Python Task Manager API

A simple REST API built using Python and Flask for managing tasks.

## Features

- Create tasks
- View all tasks
- View a single task
- Update tasks
- Delete tasks
- Input validation
- Error handling

## Technologies Used

- Python
- Flask
- REST API

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/<id>` | Get one task |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

## Installation

```bash
pip install -r requirements.txt