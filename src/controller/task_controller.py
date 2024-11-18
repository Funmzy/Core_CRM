from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status


from dependencies import UserInDB, get_current_user
from models.taskModel import Task, Task_Validation, TaskUpdate
from fastapi.encoders import jsonable_encoder



router = APIRouter()


@router.post('/')
async def create_task(task:Task_Validation, user: Annotated[UserInDB, Depends(get_current_user)]):
    new_task = Task(
        title=task.title, description=task.description, due_date=task.due_date, task_status=task.task_status,
        priority=task.priority, contact_id=task.contact_id, user=user.id
        )

    await new_task.create()
    return {
        "message":"Task Created Success",
        "data":new_task
        }



@router.get("/")
async def get_all_contacts(user:Annotated[UserInDB, Depends(get_current_user)]):
    print('Get all contacts')
    tasks= await Task.find().to_list()
    return {
        "message":"Task Lists",
        "data":tasks
        }


@router.patch("/{task_id}", response_model=Task)
async def update_contact(task_id:str, tasks:TaskUpdate, user:Annotated[UserInDB, Depends(get_current_user)]):

    task = await Task.get(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    
    update_data = tasks.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task, key, value)

    # Save the updated document
    await task.save()
    return task
