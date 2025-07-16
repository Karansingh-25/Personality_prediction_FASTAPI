from pydantic import BaseModel,computed_field,Field
from typing import Annotated



class human(BaseModel):

    Time_spent_Alone:Annotated[int,Field(...,gt=-1,ls=12,description="Time spend alone")]
    Stage_fear:Annotated[bool,Field(...,description="Person have Stage fear?")]
    Social_event_attendance:Annotated[int,Field(...,gt=-1,ls=11,description="Attend social events")]
    Going_outside:Annotated[int,Field(...,gt=-1,ls=7,description="Goes outside?")]
    Drained_after_socializing:Annotated[bool,Field(...,description="Tired after metting with people?")]	
    Friends_circle_size:Annotated[int,Field(...,gt=-1,ls=16,description="Number of friends.")]
    Post_frequency:Annotated[int,Field(...,gt=-1,ls=11,description="Activity on social media")]

    @computed_field
    @property
    def private_time(self)->str:
        if self.Time_spent_Alone < 4:
            return "Low"
        elif self.Time_spent_Alone >=4 and self.Time_spent_Alone < 8:
            return "Medium"
        else :
            return "High"
        
    @computed_field
    @property
    def activity_score(self)->str:
        if self.Social_event_attendance+self.Going_outside+self.Post_frequency <=7:
            return "Low"
        elif self.Social_event_attendance+self.Going_outside+self.Post_frequency >=8 and self.Social_event_attendance+self.Going_outside+self.Post_frequency <=14:
            return "Medium"
        else:
            return "High"
        
    @computed_field
    @property
    def making_friends(self)->str:
        if self.Friends_circle_size < 4:
            return "Low"
        elif self.Friends_circle_size >=4 and self.Friends_circle_size < 9:
            return "Medium"
        else:
            return "High"