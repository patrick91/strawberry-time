from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from strawberry.fastapi import GraphQLRouter

from api.schema import schema


app = FastAPI()

origins = [
    "https://studio.apollographql.com",
    "https://next-time-one.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


graphql_app = GraphQLRouter(schema, path="/")

app.include_router(graphql_app)
