from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status


from dependencies import UserInDB, get_current_user
from models.taskModel import Task, Task_Validation
from fastapi.encoders import jsonable_encoder



router = APIRouter()


# @router.post('/')
# async def create_task(task:Task_Validation, user: Annotated[UserInDB, Depends(get_current_user)]):
#     # title, description, due_date, task_status, priority = task
#     print('task:', task)
#     new_task = Task(title=task.title, description=task.description, due_date=task.due_date, task_status=task.task_status, priority=task.priority)

#     await new_task.create()
#     return {
#         "message":"Task Created Success",
#         "data":new_task
#         }

