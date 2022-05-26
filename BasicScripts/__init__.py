from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/{simple}")
def root(simple: str):
    if simple == "hello":
        return {"greeting": "You are welcome"}
    else:
        raise HTTPException(status_code=404, detail="siz neto so'z kiritdiz")
