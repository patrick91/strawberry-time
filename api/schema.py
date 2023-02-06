import strawberry
from datetime import datetime


@strawberry.type
class CurrentTime:
    id: strawberry.ID
    now: datetime
    note: str = "Default note"


@strawberry.type
class Query:
    @strawberry.field
    def now(self, id: strawberry.ID) -> datetime:
        return datetime.now()

    @strawberry.field
    def current_time(self, id: strawberry.ID) -> CurrentTime:
        return CurrentTime(id=id, now=datetime.now())


@strawberry.type
class Mutation:
    @strawberry.mutation
    def update_current_time(self, id: strawberry.ID, note: str) -> CurrentTime:
        return CurrentTime(id=id, now=datetime.now(), note=note)


schema = strawberry.federation.Schema(
    Query,
    Mutation,
    enable_federation_2=True,
)
