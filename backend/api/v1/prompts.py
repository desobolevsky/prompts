from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api import deps
from crud import crud_prompt
from schemas.prompts import PromptListItem, PromptGet

router = APIRouter()


@router.get("/", response_model=list[PromptListItem])
async def list_prompts(*, db: Session = Depends(deps.get_db)) -> list:
    """List prompts."""
    return crud_prompt.get_multi(db)


@router.get("/{prompt_id}", response_model=PromptGet)
async def get_prompt(*, db: Session = Depends(deps.get_db), prompt_id: int) -> dict:
    """Get prompt by ID."""
    prompt = crud_prompt.get(db, id=prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt
