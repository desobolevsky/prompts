from pydantic import BaseModel


# Shared properties
class PromptBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


# Properties to return on get prompt list
class PromptListItem(PromptBase):
    pass


# Nested example properties
class PromptExample(BaseModel):
    user_message: str | None = None
    system_message: str | None = None


# Properties to return on get single prompt
class PromptGet(PromptBase):
    description: str
    template: str
    examples: list[PromptExample] = []
