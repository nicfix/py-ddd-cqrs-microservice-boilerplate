# Use Domain Specific Exceptions

# Status

approved

# Context

As in life, also when developing APIs things do not always go as planned :)
In such cases there are several approaches to handle failures in a function.

Some of these are:

* Return objects
* Return None
* Raise exceptions

There's no such thing as the right or wrong approach, and the discussion on using or not exceptions went so far that is
honestly impossible to declare a "clear winner" in the industry.

My personal opinion (and approach) is to:

1. Use exceptions when things do not go as planned
2. Wrap every "expected" exception with Domain Specific Exceptions
3. Use the `raise ... from e` functionality in python to carry the entire stack of exceptions
4. Allow "unexpected" exceptions to bubble up
5. DO NOT use wide exception handling, let the webserver throw a 500, get notified for unhandled exceptions
    1. if the error should be "expected" create a Domain Specific Exception for it
    2. If not then the problem is somewhere else in the architecture, let it be unhandled, the code should fail fast and
       scream loud.

# Decision

Use Domain Specific Exceptions, wrap all the expected cases, let the other exceptions bubble up and wrap them when
encountered.

# Example

Let's suppose to have the following:

```python

class PetNotFoundError(Exception):
    pass


def get_pet_from_db(pet_id: UUID) -> Pet:
    try:
        return db.query(Pet).get(id=pet_id)
    except mydblibrary.errors.RowNotFoundError as e:
        raise PetNotFoundError() from e
```

`PetNotFoundError` is the Domain Specific Exception, it represents what happened in the domain, and has no connection
with any specific technology.
`mydblibrary.errors.RowNotFoundError` is the "expected" technology specific exception.
Let's now imagine the usage of this function from the api.

```python
@app.get("/pet/{pet_id}")
def get_pet_api(pet_id: UUID) -> Dict:
    try:
        pet = get_pet_from_db(pet_id)
    except PetNotFoundError as e:
        return HttpResponse(f"Pet {pet_id} was not found", status_code=404)

    return HttpResponse(to_json(pet), status_code=200)
```

Now let's suppose to receive an "unexpected" `mydblibrary.errors.ConnectionFailedError`, in this
scenario `get_pet_from_db` will fail and whoever is using it will receive the `ConnectionFailedError`.
In the case of the API use a mechanism to respond with a 500 to this exception, set in place a mechanism to notify the
team when this happens and approach the situation as follows.

If the problem is due to some temporary problem, solve that problem and let the api fail fast and notify the team.
If instead is an error that should be "expected", create another Domain Specific Exception and handle the error with a
consistent return code.